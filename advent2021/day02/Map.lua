--[[
    Contains tile data and necessary code for rendering a tile map to the
    screen.
]]

require 'Util'

Map = Class{}

-- a speed to multiply delta time to scroll map; smooth value
local SCROLL_SPEED = 62

-- constructor for our map object
function Map:init()
    -- associate player with map
    self.player = Player(self)
    
    -- camera offsets
    self.camX = 0
    self.camY = -3
end

-- return whether a given tile is collidable
function Map:collides(tile)
end

-- function to update camera offset with delta time
function Map:update(dt)
    self.player:update(dt)
    
    -- keep camera's X coordinate following the player, preventing camera from
    -- scrolling past 0 to the left and the map's width
    self.camX = math.max(0, math.min(self.player.x - VIRTUAL_WIDTH / 2,
        math.min(VIRTUAL_WIDTH, self.player.x)))
end

-- renders our map to the screen, to be called by main's render
function Map:render()

    self.player:render()
end
