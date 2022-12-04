inspect = require('inspect')

Class = require 'class'
push = require "push"

require 'Map'
require 'Player'

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

fileContent = read_file("D:/Work/Code/adventofcode/advent2021/day02/input2.txt");

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
VIRTUAL_WIDTH = WINDOW_WIDTH
VIRTUAL_HEIGHT = WINDOW_HEIGHT

-- an object to contain our map data
map = Map()

function love.load()
    FORWARD = 0
    DEPTH = 0
    RESULT = 0

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = true
    })
    
    gameState = 'stop'
end

-- called every frame, with dt passed in as delta in time since last frame
function love.update(dt)
    map:update(dt)
end

function love.draw()
    -- begin virtual resolution drawing
    push:apply('start')
    
    -- for _, line in ipairs(fileContent) do
    --     love.graphics.print(line)
    -- end
    data = string.format("Day 02! X: %d | Y: %d | RESULT: %d", FORWARD, DEPTH, RESULT)
    
    -- clear screen using Mario background blue
    love.graphics.clear(108/255, 140/255, 255/255, 255/255)
    
    -- renders our map object onto the screen
    love.graphics.translate(math.floor(-map.camX + 0.5), math.floor(-map.camY + 0.5))
    map:render()

    -- end virtual resolution
    push:apply('end')
    
end

function displayUI()
    -- love.graphics.setFont(smallFont)
    love.graphics.setColor(125, 125, 135, 125)
    -- love.graphics.print('Count: ' .. tostring(collisioncount), 45, 2)
    love.window.setTitle(title)
end