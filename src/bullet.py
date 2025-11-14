import random



class Bullet:
    def __init__(self, pos_x,  pos_y):
        self.size = random.randint(10, 30)
        self.x = pos_x
        self.y = pos_y

    def handle_frame(self, dt):
        self.x += 3000 * dt

        
