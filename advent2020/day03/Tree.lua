Tree = Class{}

function Tree:init(x, y,width, height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.collide = {}
    self.collide['a'] = false
    self.collide['b'] = false
    self.collide['c'] = false
    self.collide['d'] = false
    self.collide['e'] = false
    self.collided = false
end

function Tree:reset()
    self.collide['a'] = false
    self.collide['b'] = false
    self.collide['c'] = false
    self.collide['d'] = false
    self.collide['e'] = false
    self.collided = false
end

function Tree:render()
    love.graphics.rectangle('fill', self.x, self.y, self.width, self.height)
end

function Tree:collides(man, count, name)
    if math.floor(man.x) == self.x and math.floor(man.y) == self.y then
        if not self.collide[name] then 
            self.collide[name] = true
            count = count + 1
        end
        if not self.collided then
            self.collided = true
        end
    end
    return count

end

-- function Tree:brown()
--     love.graphics.setColor(255,0,0,255)
--     love.graphics.rectangle('fill', self.x, self.y, self.width, self.height)
--     love.graphics.setColor(255,255,255,255)
-- end