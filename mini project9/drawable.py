from abc import ABC, abstractmethod 

class Drawable(ABC):

    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible
    
    @abstractmethod
    def draw(self, surface):
        pass
    
    @abstractmethod   
    def get_rect(self):
        pass
        
    # Optional extra methods
    def move_to(self, newx, newy):
        self.x = newx
        self.y = newy
    
    def get_pos(self):
        return self.x, self.y