Man = Class{}

function Man:init(x, y,width, height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
end

function Man:reset(x, y)
    self.x = x
    self.y = y
end

function Man:update(dt)
    self.x = self.x + self.dx
    self.y = self.y + self.dy
end

function Man:render()
    love.graphics.rectangle('fill', self.x, self.y, self.width, self.height)
end


