import pygame
import sys
import random
import time
import threading
from threading import * 
from random import randint 



bg = pygame.image.load("/home/bis/Documents/repository/python-snakegame/test.jpg")


score = 0 

class Block:
    def __init__(self,x_pos,y_pos):
        self.x = x_pos
        self.y = y_pos



class Bomb:
    def __init__(self): 
        x = random.randint(0,NB_COL-1)
        y = random.randint(0,NB_ROW-1)
        
        self.block = Block(x, y)
        
        
    def draw_bomb(self):
         rect = pygame.Rect(self.block.x *CELL_SIZE,self.block.y * CELL_SIZE,CELL_SIZE,CELL_SIZE)
         pygame.draw.rect(screen,(255,0,90),rect) 












class Food:
    def __init__(self): 
        x = random.randint(0,NB_COL-1)
        y = random.randint(0,NB_ROW-1)
        self.block = Block(x, y)
    
    def draw_food(self):
         rect = pygame.Rect(self.block.x *CELL_SIZE,self.block.y * CELL_SIZE,CELL_SIZE,CELL_SIZE)
         pygame.draw.rect(screen,(72,212,90),rect)






class Snake:
    def __init__(self):
        self.body = [Block(2,6),Block(3,6),Block(4,6)]
        self.direction = "RIGHT"
    
    def draw_snake(self):
        for block in self.body:
            x_coord = block.x * CELL_SIZE
            y_coord = block.y * CELL_SIZE
            block_rect = pygame.Rect(x_coord,y_coord,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,(219,73,235),block_rect)

    def move_snake(self):
        snake_block_count = len(self.body)
        old_head = self.body[snake_block_count -1]

        if self.direction =="RIGHT":
            new_head = Block( old_head.x+1 , old_head.y)
            self.body.append(new_head)
            
        
        elif self.direction =="LEFT":
            new_head = Block( old_head.x-1 , old_head.y)
            self.body.append(new_head)
            
        
        elif self.direction =="TOP":
            new_head = Block( old_head.x , old_head.y -1)
            self.body.append(new_head)
            

        else:
            
            new_head = Block( old_head.x , old_head.y +1)
            self.body.append(new_head)
            

    def reset_snake(self):
        self.body = [Block(2,6),Block(3,6),Block(4,6)]
        self.direction = "RIGHT"
        global score
        score = 0 
        global tick
        tick = 300
        pygame.time.set_timer(SCREEN_UPDATE,300)









class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.bomb = Bomb()
        
        self.generate_food()
        
        

    def update(self):
        self.snake.move_snake()
        self.check_head_on_food()
        self.game_over()
       
        

    def draw_game_element(self):
        self.food.draw_food()
        self.snake.draw_snake()
        self.bomb.draw_bomb()
        
    def generate_bomb(self):
        count = 0  
        should_generate_bomb= True
        while should_generate_bomb:
            count += 1 
            
            if count > 10 :
                should_generate_bomb = False
            else:
                
                self.bomb = Bomb()



    
    def check_head_on_food(self):
        snake_length = len(self.snake.body)
        snake_head_block = self.snake.body[snake_length-1]
        food_block = self.food.block
        if snake_head_block.x == food_block.x and snake_head_block.y == food_block.y:
            self.generate_food()


            enemies = []
            maxenemies = 2
            for i in range(maxenemies):
                enemies.append(Bomb())
                print(enemies)


            global score 
            score += 10 
        else:
            self.snake.body.pop(0)
        


    def generate_food(self):
        
        should_generate_food = True
        while should_generate_food:
            count = 0 
            for block in self.snake.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count +=1
            if count == 0:
                should_generate_food = False
            else:
                self.food = Food()
                
             
    


    def game_over(self):
        snake_length = len(self.snake.body)
        snake_head = self.snake.body[snake_length -1]
        if snake_head.x not in range (0,NB_COL) or snake_head.y not in range(0,NB_ROW):
            self.snake.reset_snake()
            
        for block in self.snake.body[0:snake_length -1]:
            if block.x == snake_head.x and block.y == snake_head.y:
                self.snake.reset_snake()
                
        if snake_head.x == self.bomb.block.x and snake_head.y == self.bomb.block.y:
            self.snake.reset_snake()
            







pygame.init()


NB_COL = 20
NB_ROW = 20
CELL_SIZE = 40

screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE))

timer = pygame.time.Clock()


game = Game()







tick = 300
SCREEN_UPDATE = pygame.USEREVENT
def speed():
    global tick
    print(tick)
    threading.Timer(7, speed).start()
    tick -= 25
    if tick == 50:
        tick = 75
    pygame.time.set_timer(SCREEN_UPDATE,tick)
    
speed()






def show_grid():
    for i in range(0,NB_COL):
        for j in range(0,NB_ROW):
            rect = pygame.Rect(i * CELL_SIZE , j * CELL_SIZE , CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen,pygame.Color("black"),rect,width=1)




game_on = True


while game_on:
    

   
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                
        if event.type == SCREEN_UPDATE:
            game.update()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if game.snake.direction != "DOWN":
                    game.snake.direction ="TOP"
            if event.key == pygame.K_s:
                if game.snake.direction != "UP":
                    game.snake.direction ="DOWN"
            if event.key == pygame.K_q:
                if game.snake.direction != "RIGHT":
                    game.snake.direction ="LEFT"
            if event.key == pygame.K_d:
                if game.snake.direction != "LEFT":
                    game.snake.direction ="RIGHT"


                        
                    
    




    text1 = "score : " + str(score)
    screen.blit(bg, (0, 0))
    #screen.fill((110,11,11))
    show_grid()
    game.draw_game_element()
    font = pygame.font.Font(None, 40)
    text = font.render(text1, 1, "white")
    screen.blit(text, (50,50))
    pygame.display.update()
    timer.tick(60)
   




