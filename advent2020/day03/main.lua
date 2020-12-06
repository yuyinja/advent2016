inspect = require('inspect')

Class = require "class"
push = require "push"

require "Man"
require "Tree"

local open = io.open

local function read_file(path)
    local file = open(path, "rb") -- r read mode and b binary mode
    if not file then return nil end
    local lines = {}
    while true do
        line = file:read()
        if line == nil then break end
        lines[#lines + 1] = line
        end
    file:close()
    return lines
end

fileContent = read_file("D:/Work/Code/adventofcode/advent2020/day03/input.txt");
map_length, map_width = #fileContent, #fileContent[1];

WINDOW_WIDTH = map_width * 6 + 25
WINDOW_HEIGHT = map_length * 3 + 50
VIRTUAL_WIDTH = map_width
VIRTUAL_HEIGHT = map_length / 2

SIM_SPEED = 0.01

timer = 0

function love.load()
    COLLISION_COUNTA = 0
    COLLISION_COUNTB = 0
    COLLISION_COUNTC = 0
    COLLISION_COUNTD = 0
    COLLISION_COUNTE = 0

    -- change texture scaling filter so it isn't blurry
    love.graphics.setDefaultFilter('nearest', 'nearest')
    love.window.setTitle("Day 03!")

    -- score tree collisions


    smallFont = love.graphics.newFont('font.ttf', 8)

    manA = Man(1, 1, 1, 1)
    manB = Man(1, 1, 1, 1)
    manC = Man(1, 1, 1, 1)
    manD = Man(1, 1, 1, 1)
    manE = Man(1, 1, 1, 1)

    trees = {}

    for i=1, map_length
    do
        for j=1, map_width
        do
            char = string.sub(fileContent[i], j, j)
            if char == "#" then 
                key = string.format("%d-%d", tostring(j), tostring(i))
                trees[key] = Tree(j, i, 1, 1)
            end
        end 
    end

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = true
    })
    
    gameState = 'stop'

end

function love.keypressed(key)

    if key == 'escape' then
        gameState = 'stop'
        manA:reset(1,1)
        manB:reset(1,1)
        manC:reset(1,1)
        manD:reset(1,1)
        manE:reset(1,1)
        for k,tree in pairs(trees) do
            tree:reset()
        end
        COLLISION_COUNTA = 0
        COLLISION_COUNTB = 0
        COLLISION_COUNTC = 0
        COLLISION_COUNTD = 0
        COLLISION_COUNTE = 0
        -- love.event.quit()
    end

    if key == 'enter' or key == 'return' then
        if gameState == 'stop' then
            gameState = 'go'
        elseif gameState == 'go' then
            gameState = 'stop'
        end
    end

end

function moveman(man, ix, iy, count, name)
    if man.y < map_length then
        man.x = man.x + ix
        man.y = man.y + iy
    end 
    if man.x > map_width then
        man.x = man.x % map_width
    end

    key = string.format("%d-%d", tostring(man.x), tostring(man.y))
    tree = trees[key]
    if tree then
        return tree:collides(man, count, name)
    end
    return count 

end

function love.resize(w, h)
    push:resize(w, h)
end

function manupdate(dt, man, ix, iy, count, name)
    man.dy = 0
    man.dx = 0
    
    timer = timer + dt
    if timer >= SIM_SPEED then
        count = moveman(man, ix, iy, count, name)
        timer = 0
    end
    man:update(dt)

    return count

end

function love.update(dt)
    if gameState == 'go' then 
        COLLISION_COUNTA = manupdate(dt, manA, 1, 1, COLLISION_COUNTA, "a")
        COLLISION_COUNTB = manupdate(dt, manB, 3, 1, COLLISION_COUNTB, "b")
        COLLISION_COUNTC = manupdate(dt, manC, 5, 1, COLLISION_COUNTC, "c")
        COLLISION_COUNTD = manupdate(dt, manD, 7, 1, COLLISION_COUNTD, "d")
        COLLISION_COUNTE = manupdate(dt, manE, 1, 2, COLLISION_COUNTE, "e")

        if (manA.y >= map_length) and (manB.y >= map_length) and (manC.y >= map_length) and (manD.y >= map_length) and (manE.y >= map_length) then
            print (manA.y,manB.y,manC.y,manD.y,manE.y)
            print ("End Reached!")
            print ("COUNT A: ".. tostring(COLLISION_COUNTA))
            print ("COUNT B: ".. tostring(COLLISION_COUNTB))
            print ("COUNT C: ".. tostring(COLLISION_COUNTC))
            print ("COUNT D: ".. tostring(COLLISION_COUNTD))
            print ("COUNT E: ".. tostring(COLLISION_COUNTE))
            print ("TOTAL MULT: ".. tostring(COLLISION_COUNTA * COLLISION_COUNTB * COLLISION_COUNTC * COLLISION_COUNTD *COLLISION_COUNTE))
            gameState = 'stop'
            love.event.quit()
        end
    end
end


function love.draw()
    -- background color
    love.graphics.clear(40/255, 45/255, 52/255, 255/255)

    -- render using push
    push:apply("start")
    
    -- tree
    love.graphics.setColor(0, 255, 0, 255)
    for k,tree in pairs(trees) do
        if tree.collided then
            love.graphics.setColor(255,0,0,255)
        end
        tree:render()
        love.graphics.setColor(0, 255, 0, 255)
    end

    love.graphics.setColor(255, 255, 255, 122)
    -- man
    manA:render()
    manB:render()
    manC:render()
    manD:render()
    manE:render()
    -- love.graphics.setColor(0, 0, 0, 0)
    -- stop rendering using push

    displayCount()

    push:apply("end")
end

function displayCount()
    -- love.graphics.setFont(smallFont)
    -- love.graphics.setColor(255, 255, 255, 255)
    -- love.graphics.print('Count: ' .. tostring(collisioncount), 45, 2)
    title = string.format("Day 03! A: %d | B: %d | C: %d | D : %d | E: %d || -- %d --", COLLISION_COUNTA,COLLISION_COUNTB,COLLISION_COUNTC,COLLISION_COUNTD,COLLISION_COUNTE, (COLLISION_COUNTA * COLLISION_COUNTB * COLLISION_COUNTC * COLLISION_COUNTD *COLLISION_COUNTE))
    love.window.setTitle(title)
end
