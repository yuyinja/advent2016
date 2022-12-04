--[[
    Represents our player in the game, with its own sprite.
]]

Player = Class{}

local SPEED = 100

function Player:init()
    
    self.x = 0
    self.y = 0
    self.width = 128
    self.height = 128

    -- offset from top left to center to support sprite flipping
    self.xOffset = 0 --8
    self.yOffset = 0 --10

    -- reference to map for checking tiles
    self.map = map
    self.texture = love.graphics.newImage('sprite.png')

    -- determines sprite flipping
    self.direction = 'left'

    -- x and y velocity
    self.dx = 0
    self.dy = 0


end

function Player:update(dt)
    self.x = self.x + self.dx * dt
    -- apply velocity
    self.y = self.y + self.dy * dt
end

function Player:render()
    local scaleX

    -- set negative x scale factor if facing left, which will flip the sprite
    -- when applied

    if self.direction == 'right' then
        scaleX = 1
    else
        scaleX = -1
    end

    -- draw sprite with scale factor and offsets
    love.graphics.draw(self.texture, math.floor(self.x + self.xOffset),
        math.floor(self.y + self.yOffset), 0, scaleX, 1, self.xOffset, self.yOffset)
end