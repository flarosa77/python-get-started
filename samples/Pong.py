import sys
import pygame
import config
import random

def collisionDetection(rect1, rect2):
  collision = False

  condition = rect2["x"] + rect2["width"] >= rect1["x"]
  condition1 = rect2["y"] > rect1["y"]
  
  somma1 = rect2["y"] + rect2["height"]
  somma = rect1["y"] + rect1["height"]

  condition2 = (somma1 < somma)

  if condition and condition1 and condition2:
    collision = True 
    
  return collision

def collisionDetection2(rect1, rect2):
  collision = False

  condition = rect2["x"] <= rect1["x"] + rect1["width"]
  condition1 = rect2["y"] > rect1["y"]

  somma1 = rect2["y"] + rect2["height"]
  somma = rect1["y"] + rect1["height"]

  condition2 = (somma1 < somma)

  if condition and condition1 and condition2:
    collision = True 

  return collision

def collisionBorder(ball, config):
  collision = False

  if ball["y"] + ball["height"] >= config.height or ball["y"] <= 0 :
    collision = True

  return collision
  


def nextStep(ball,i,level):

  if(i >= 10 - level):
    ball["x"] = ball["x"] + ball["dx"]
    ball["y"] = ball["y"] + ball["dy"]
    i = 0
  else:
    i = i + 1 
    
  return (ball, i)

def startBall(ball,config):

  ball["x"] = config.width / 2 - ball["width"] / 2
  ball["y"] = config.height / 2 - ball["height"] / 2
  ball["dx"] = random.randint(1,3)
  ball["dy"] = random.randint(-3,3)
  return ball

level = config.level
step = 1
i=0

score_pc = 0
score_my = 0
disp_y = config.disp_y



pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([config.width, config.height])

pygame.display.set_caption("Pong")
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(f"PC: {score_pc} - 3F: {score_my}", True, (0,255,0), (0,0,255))
textRect = text.get_rect()
textRect.center = (300, 50)





bar1 = {"x": config.disp,"y": 60, "width": config.b_width,"height": config.b_height}

bar2 = {"x": config.width - config.disp,"y": 200, "width": config.b_width,"height": config.b_height}

ball = {"x": 0,"y": 0,"dx": 0,"dy": 0,"width": 10,"height": 10}

ball = startBall(ball,config)

# Run until the user asks to quit
running = True
while running:

  # Did the user click the window close button?
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      running = False
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
      bar2["y"] = bar2["y"] - disp_y
      
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
      bar2["y"] = bar2["y"] + disp_y
      

  pygame.draw.rect(screen, (255, 255, 255),(bar1["x"], bar1["y"], bar1["width"], bar1["height"]))
  pygame.draw.rect(screen, (255, 255, 255),(bar2["x"], bar2["y"], bar2["width"], bar2["height"]))
  pygame.draw.rect(screen, (255, 255, 255), (ball["x"], ball["y"], ball["width"], ball["height"]))


  screen.blit(text, textRect)
  pygame.display.flip()
  
  
 
  if collisionDetection(bar2,ball) or collisionDetection2(bar1,ball):
    ball["dx"] = -ball["dx"]
    ball["x"] = ball["x"] + ball["dx"] 
    
  if collisionBorder(ball, config):
    ball["dy"] = -ball["dy"]
    ball["y"] = ball["y"] + ball["dy"] 
  
  (ball,i) = nextStep(ball,i,level)
    

  if ball["x"] >= config.width:
    ball = startBall(ball,config)
    score_pc = score_pc + 1
  elif ball["x"] <= 0:
    ball = startBall(ball,config)
    score_my = score_my + 1
    
  text = font.render(f"PC: {score_pc} - 3F: {score_my}", True, (0,255,0), (0,0,255))
    

  screen.fill((0, 0, 0))
  
# Done! Time to quit.
pygame.quit()
sys.exit()
