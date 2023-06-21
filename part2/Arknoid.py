import pygame
pygame.init()
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()
#variables responsible for platform coordinates
platform_x = 200
platform_y = 330
#variables responsible for the ball's direction of movement
dx = 3
dy = 3
#flags responsible for the movement of the platform to the right/left
move_right = False
move_left = False
#flag for the end of the game
game_over = False
#a class from a previous project
class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      '''area: a rectangle in the right place and the right color'''
      #memorize the rectangle:
      self.rect = pygame.Rect(x, y, width, height)
      #fill color - either the passed parameter or the overall background color
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
platform = Picture('platform.png', platform_x, platform_y, 100, 30)
#creating enemies
start_x = 5
start_y = 5
count = 9
monsters = []
for j in range(3):
  y = start_y + (55 * j)
  x = start_x + (27.5 * j)
  for i in range (count):
      d = Picture('enemy.png', x, y, 50, 50)
      monsters.append(d)
      x = x + 55
  count = count - 1
while not game_over:
  ball.fill()
  platform.fill()
    
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          game_over = True
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT: #if the key is pressed
              move_right = True # raising the flag
          if event.key == pygame.K_LEFT:
              move_left = True # raising the flag
      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_RIGHT:
              move_right = False #lowering the flag
          if event.key == pygame.K_LEFT:
              move_left = False #lowering the flag
    
  if move_right: #right movement flag
      platform.rect.x +=3
  if move_left: #left movement flag
      platform.rect.x -=3
  #giving constant acceleration to the ball at x and y
  ball.rect.x += dx
  ball.rect.y += dy
   # if the ball reaches the borders of the screen, change the direction of its movement
  if  ball.rect.y < 0:
      dy *= -1
  if ball.rect.x > 450 or ball.rect.x < 0:
      dx *= -1
  # if the ball has touched the racket, change the direction of movement
  if ball.rect.colliderect(platform.rect):
      dy *= -1
  for m in monsters:
      m.draw()
  platform.draw()
  ball.draw()
  pygame.display.update()
  clock.tick(40)
