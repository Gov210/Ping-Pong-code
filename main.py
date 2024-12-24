#import modules
import pygame
import random

#initalize game
pygame.init()

#create screen dimensions
screen_width = 800
screen_height = 600

#create screen and name
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2 player Ping Pong")

#set game clock
clock = pygame.time.Clock()

#colors
white = (255,255,255)
black = (0,0,0)

#create paddles and ball
paddle_width = 15
paddle_height = 80
paddle_speed = 7
increment_speed = 0.5

ball_width = 12
ball_height = 12
ball_speed_x = 5
ball_speed_y = 5

#create the rects
paddle1 = pygame.Rect(10, screen_height // 2, paddle_width, paddle_height)
paddle2 = pygame.Rect(775, screen_height // 2, paddle_width, paddle_height)

ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_width, ball_height)

center = screen.get_rect().center

#score and font
score1 = 0
score2 = 0
max_score = 1
font = pygame.font.Font(None, 60)

#move ball function
def move_ball():
  global ball_speed_y, ball_speed_x, score1, score2
  ball.x += ball_speed_x
  ball.y += ball_speed_y

  if ball.top <= 0 or ball.bottom >= screen_height: 
    ball_speed_y *= -1
  
  if ball.x >= screen_width:
    reset_ball()
    score1 += 1

  if ball.x <= 0:
    reset_ball()
    score2 += 1

def reset_ball():
  global ball_speed_x, ball_speed_y
  ball.x = screen_width // 2
  ball.y = screen_height // 2
  ball_speed_x = 5
  ball_speed_y = 5
  ball_speed_x *= random.choice([-1,1])
  ball_speed_y *= random.choice([-1,1])

#function to display the score
def display_score():
  global score1, score2
  #score text
  score_text1 = font.render(str(score1), True, white)
  score_text2 = font.render(str(score2), True, white)

  #display score
  screen.blit(score_text1, (50,50))
  screen.blit(score_text2, (725,50))

#function to end game
def end_game():
  global max_score, ball_speed_x, ball_speed_y
  if max_score == score1 or max_score == score2:
    #create new screen
    screen.fill(black)
    #stop everything
    ball_speed_x = 0
    ball_speed_y = 0

    display_winner()

def display_winner():
  global score1, score2
  #player 1
  if score1 == max_score:
    win = font.render("Player 1 Wins!", True, white)
    screen.blit(win, win.get_rect(center=center))
  
  #player 2
  if score2 == max_score:
    win = font.render("Player 2 Wins", True, white)
    screen.blit(win, win.get_rect(center=center))


def move_paddles(keys):
  global paddle1, paddle2

  #up p1
  if keys[pygame.K_w] and paddle1.top > 0:
    paddle1.y -= paddle_speed
  
  #down p1
  if keys[pygame.K_s] and paddle1.bottom < screen_height:
    paddle1.y += paddle_speed

  #up p2
  if keys[pygame.K_UP] and paddle2.top > 0:
    paddle2.y -= paddle_speed
  
  #down p2
  if keys[pygame.K_DOWN] and paddle2.bottom < screen_height:
    paddle2.y += paddle_speed

  #collide function
def ball_collide():
  global ball, ball_speed_x
  if ball.colliderect(paddle1) or ball.colliderect(paddle2):
    ball_speed_x *= -1
    increase_speed()

#increase speed function
def increase_speed():
  global ball_speed_x, ball_speed_y
  if ball_speed_x > 0 and ball_speed_y > 0:
    ball_speed_x += increment_speed
    ball_speed_y += increment_speed
  
  else:
    ball_speed_y -= increment_speed
    ball_speed_x -= increment_speed

#create draw function
def draw():
  pygame.draw.rect(screen, white, paddle1)
  pygame.draw.rect(screen, white, paddle2)
  pygame.draw.rect(screen, white, ball)


#create running variable
running = True

while running:
  #create loop for game handles
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  keys = pygame.key.get_pressed()
  move_paddles(keys)

  
  #add background color
  screen.fill(black)



  #score function
  display_score()

  #ball collide with paddles
  ball_collide()

  #move the ball
  move_ball()

  #draw everything
  draw()

  #call end game function
  end_game()

  #update game
  pygame.display.update()

  #set fps
  clock.tick(60)
