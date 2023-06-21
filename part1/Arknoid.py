import pygame
pygame.init()


back = (200, 255, 255) #background color
mw = pygame.display.set_mode((500, 500)) #main window
mw.fill(back)
clock = pygame.time.Clock()


#variables responsible for platform coordinates
racket_x = 200
racket_y = 330


#flag for the end of the game
game_over = False
#a class from a previous project
class Area():
   def __init__(self, x=0, y=0, width=10, height=10, color=None):
       self.rect = pygame.Rect(x, y, width, height)
       self.fill_color = back
       if color:
           self.fill_color = color


   def color(self, new_color):
       self.fill_color = new_color


   def fill(self):
       pygame.draw.rect(mw, self.fill_color, self.rect)


   def collidepoint(self, x, y):
       return self.rect.collidepoint(x, y)       


   def colliderect(self, rect):
       return self.rect.colliderect(rect)


#class for image objects
class Picture(Area):
   def __init__(self, filename, x=0, y=0, width=10, height=10):
       Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
       self.image = pygame.image.load(filename)
      
   def draw(self):
       mw.blit(self.image, (self.rect.x, self.rect.y))


#creating a ball and the platform   
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)


#creating enemies
start_x = 5 #coordinates of the creation of the first monster
start_y = 5
count = 9 #number of monsters in the top row
monsters = [] #list for storing monster objects
for j in range(3): #cycle through columns
   y = start_y + (55 * j) #coordinate of the monster in each following column will be offset by 55 pixels in y
   x = start_x + (27.5 * j) #и 27.5 по x
   for i in range (count):#a cycle through rows (lines) creates a number of monsters in a row equal to count
       d = Picture('enemy.png', x, y, 50, 50) #creating a monster
       monsters.append(d) #adding to the list
       x = x + 55 #increasing the coordinate of the next monster
   count = count - 1 #for the next row, reduce the number of monsters


while not game_over:
   ball.fill()
   platform.fill()
      
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           game_over = True


   #drawing all the monsters from the list
   for m in monsters:
       m.draw()


   platform.draw()
   ball.draw()


   pygame.display.update()


   clock.tick(40)
