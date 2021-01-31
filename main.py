import pygame as pg

FPS = 60

class Window:
    width = 640
    height = 480
    center_x = width/2
    center_y = height/2
    
pg.init()
screen = pg.display.set_mode((Window.width, Window.height))
clock = pg.time.Clock()

class Button:
    # Конструктор
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_over(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and \
           self.y <= mouse_y <= self.y + self.height
          
    def jumpto(self, x, y):
        self.x = x
        self.y = y
        
VIOLET = (204, 0,255)
AQUA = (102, 255, 255)

distance_to_center_x = 30
Button.width = 100
Button.height = 30
view_x = Window.center_x - Button.width - distance_to_center_x
view_y = Window.center_y;

btn_yes = Button(VIOLET, view_x, view_y, Button.width, Button.height)
btn_no = Button(VIOLET, view_x + Button.width + distance_to_center_x*2, view_y, Button.width, Button.height)

running = True
while running:
    clock.tick(FPS)
    screen.fill(AQUA)
    
    list_events = pg.event.get()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            print(btn_no.jumpto(mouse_x, mouse_y))
            if btn_no.is_over(mouse_x, mouse_y):
                btn_no.jumpto(10, 160)
    
    btn_yes.draw(screen)
    btn_no.draw(screen)
    
    pg.display.update()
pg.quit()