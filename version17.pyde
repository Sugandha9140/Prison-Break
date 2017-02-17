#We have to create maze because DON FUCKING DIDNT DO IT (use maze6)


import random
import os
import time
add_library('sound')
path = os.getcwd()





#game.complete is used to check the last game.state, and you can enter the next door when if game.state == "prison" and game.complete = "last game's game.state"
#you can also say else: text(This door is still locked) or something like that
#for level3, we need to use the memo picture, and common background coler
#popup of unlocked also
#SHUNYA has to set the boundaries of prison!
#######################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
##
class Game:
    def __init__ (self):
        self.w = 1000
        self.h = 750
        self.x = 0
        self.g = 0
        self.marioX = self.w/2
        self.marioY = self.h/2
        self.header = 40
        self.state = "welcome"
        self.complete = "none"

        # self.r = Room()
        #self.mario = Mario(50,10,40)
        
    def create(self):
        self.r = Room(80)
        self.d = Door(self.w/2, 0+game.header, 0, 0, 78, 62)
        self.d2 = Door2(self.w-game.r.l+19, self.h/2, 96, 32, 64, 0)
        self.d3 = Door(self.w/2, self.h-119+game.header, 0, 62, 78, 0)
        self.d4 = Door2(18, self.h/2, 64, 0, 96, 32)
        self.mario = Mario(self.marioX, self.marioY,40, self.g)
        
        
    def display (self):
        self.r.display()
        self.d.display()
        self.d2.display()
        self.d3.display()
        self.d4.display()
        self.mario.display()
        
#######################################################################################################################
#######################################################################################################################

class Fight:
    def __init__ (self):
        self.w= game.w
        self.h= game.h
        self.g=game.h-100
        self.platforms = []
        self.x=0
        self.state = 'instruction'
        self.name=""
        self.score=0
        self.timer=0
        self.t=0
        self.life = 5

    def create(self):
        for step in range(70, -30, -50):
            self.platforms.append(Platform(150+4*step,400-3*step+game.header+150,150,10))
        
        # for step in range(100, -50, -50):
        #     self.enemies.append(Enemy(200+4*step,30,20,self.g,150+4*step,150+4*step+150))
        self.ball = Sphere(650, 30, 30, 0)
        self.fire = Fire(game.w-300, self.g, 50, self.g)
        self.fire2 = Fire(game.w-400, self.g, 50, self.g)
        self.fire3 = Fire(game.w-500, self.g, 50, self.g)
        self.enemy = Enemy(game.w-100, 30, 50, self.g, 650, 750)
        self.mario = Mario(50,10,40,self.g)
    
    def display(self):
        self.t=(self.t+1)%60
        
        if self.t==0:
            self.timer+=1
        
        line(0,self.g,self.w,self.g)
        for p in self.platforms:
            p.display()
        self.fire.display()
        self.fire2.display()
        self.fire3.display()
        # for e in self.enemies:
        #     e.display()
        self.enemy.display()
        game.mario.display()
        self.ball.display()

#######################################################################################################################
#######################################################################################################################
    
class Room:
    def __init__ (self, l):
        self.l = l
        
    def display (self):
        background(120)
        line(0, game.header, self.l, self.l+game.header)
        line(game.w, game.header, game.w-self.l, self.l+game.header)
        line(0, game.h, self.l, game.h-self.l)
        line(game.w, game.h, game.w-self.l, game.h-self.l)
        line(self.l, self.l+game.header, game.w-self.l, self.l+game.header)
        line(self.l, game.h-self.l, game.w-self.l, game.h-self.l)
        line(self.l, self.l+game.header, self.l, game.h-self.l)
        line(game.w-self.l, self.l+game.header, game.w-self.l, game.h-self.l)

#######################################################################################################################
#######################################################################################################################
class Door:
    def __init__ (self, x, y, x1, y1, x2, y2):
        self.x = x
        self.y = y
        self.r = 62
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.img = loadImage("171-Door02.png")
        
    def display (self):
        image(self.img, self.x-self.r, self.y, game.r.l+20, game.r.l, self.x1, self.y1, self.x2, self.y2)

class Door2:
    def __init__ (self, x, y, x1, y1, x2, y2):
        self.x = x
        self.y = y
        self.r = 36
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.img = loadImage("door_tiles.png")
        
    def display (self):
        image(self.img, self.x-self.r/2, self.y-game.header, game.r.l, game.r.l, self.x1, self.y1, self.x2, self.y2)
#######################################################################################################################
#######################################################################################################################

class Platform:
    def __init__ (self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def display(self):
        stroke(255)
        fill (255)
        rect (self.x-fight.x,self.y,self.w,self.h)
        
#######################################################################################################################
#######################################################################################################################

class Creature:
    def __init__ (self,x,y,r,g):
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.r=r
        self.g=g
        self.jumps=0

        
    def gravity(self):
        if self.y+self.r < self.g:
            self.vy+=0.1
        else:
            self.vy=0
            self.jumps = 0
            self.y = self.g-self.r
            
        for p in fight.platforms:
            if self.y+self.r <= p.y and p.x <= self.x <= p.x+p.w:
                self.g = p.y
                break
            else:
                self.g = fight.g
            
    def update(self):
        self.gravity()
        
        self.x+=self.vx
        self.y+=self.vy
        
    def display(self):
        self.update()
        stroke(255)
        fill(0)
        ellipse(self.x,self.y,2*self.r,2*self.r)

#######################################################################################################################
#######################################################################################################################

class Mario(Creature):
    def __init__ (self,x,y,r,g):
        Creature.__init__(self,x,y,r,g)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False, DOWN: False}
        self.img = loadImage('attack_on_titan_rpg_sprite__eren__by_allthelittlewonders-d8oynfh.png')
        self.frames=3
        self.f=1
        self.ff=1
        self.dir = 1
        #self.life = 5
        self.t = 0
        self.deadtime = 0
        self.hitTimer=0   

    def display(self):
        self.update()
        
        if game.state == "prison":
            if self.vx != 0 or self.vy != 0:
                self.f=(self.f+0.1)%self.frames
            # BOUNDARIES AS YOU ASKED!!
            if self.x <= game.r.l+self.r:
                self.x = game.r.l+self.r
            elif self.x >= game.w-game.r.l-self.r:
                self.x = game.w-game.r.l-self.r
            if self.y <= game.r.l+self.r:
                self.y = game.r.l+self.r
            elif self.y >= game.h-game.r.l-self.r:
                self.y = game.h-game.r.l-self.r
                
            if self.vx > 0 or self.dir == 1:
                image(self.img, self.x-self.r, self.y-self.r, 2*self.r, 2*self.r, 0+int(self.f)*32, 64, 32+int(self.f)*32, 96)
            elif self.vx < 0 or self.dir == 2:
                image(self.img, self.x-self.r, self.y-self.r, 2*self.r, 2*self.r, 64-int(self.f)*32, 32, 96-int(self.f)*32, 64)
            elif self.vy > 0 or self.dir == 3:
                image(self.img, self.x-self.r, self.y-self.r, 2*self.r, 2*self.r, 0+int(self.f)*32, 0, 32+int(self.f)*32, 32)
            elif self.vy < 0 or self.dir == 4:
                image(self.img, self.x-self.r, self.y-self.r, 2*self.r, 2*self.r, 64-int(self.f)*32, 96, 96-int(self.f)*32, 128)
                self.dir = 4

        elif game.state == "fight":
            if self.vx != 0:
                    self.f=(self.f+0.1)%self.frames
                    
            if self.hitTimer % 2 == 0:
                if self.vx > 0 or self.dir > 0:
                    image(self.img, self.x-self.r-fight.x, self.y-self.r, 2*self.r, 2*self.r, 0+int(self.f)*32, 64, 32+int(self.f)*32, 96)
                elif self.vx < 0 or self.dir < 0:
                    image(self.img, self.x-self.r-fight.x, self.y-self.r, 2*self.r, 2*self.r, 64-int(self.f)*32, 32, 96-int(self.f)*32, 64)
            
    def distance(self,target):
        return ((self.x-target.x)**2+(self.y-target.y)**2)**0.5

    def update(self):
        #print(self.keyHandler)
        if game.state == "prison":
            if self.keyHandler[LEFT]:
                self.vx = -2
                self.dir = 2
            elif self.keyHandler[RIGHT]:
                self.vx = 2
                self.dir = 1
            elif self.keyHandler[UP]:
                self.vy = -2
                self.dir = 4
            elif self.keyHandler[DOWN]:
                self.vy = 2
                self.dir = 3
            else:
                self.vx = 0
                self.vy = 0
            
            if self.distance(game.d) <= self.r+game.d.r+20:
                game.state = "beforeFight"
                game.marioX = game.mario.x
                game.marioY = game.mario.y+50
                game.mario.x = 0
                setup()
            elif self.distance(game.d2) <= self.r+game.d.r+20:
                if game.state == "prison" and game.complete == "fight":
                    game.state = "level3"
                    setup()
            elif self.distance(game.d3) <= self.r+game.d.r+20:
                game.state = "maze"
                setup()
            elif self.distance(game.d4) <= self.r+game.d.r+20:
                game.state = "escape"
                setup()




############################ for three other doors, it says game.state = "something else"
            
                
            self.x+=self.vx
            self.y+=self.vy 
        
            
            if self.x-self.r < 0:
                self.x = self.r
            elif self.x+self.r > game.w:
                self.x = game.w-self.r
                
        elif game.state == "fight":
            self.gravity()
            
            if self.hitTimer > 0:
                self.hitTimer -= 1
            
            if self.keyHandler[LEFT]:
                self.vx = -2
                self.dir = -1
            elif self.keyHandler[RIGHT]:
                self.vx = 2
                self.dir = 1
            else:
                self.vx = 0
                
            if self.keyHandler[UP] and (self.jumps < 2 and self.vy >= 0):
                self.jumps+=1
                self.vy = -5
    
                
            self.x+=self.vx
            self.y+=self.vy 
        
            
            if self.x-self.r < 0:
                self.x = self.r
            elif self.x+self.r > fight.w:
                self.x = fight.w-self.r
            
            
            if (self.distance(fight.enemy) <= self.r+fight.enemy.r \
                    or self.distance(fight.ball) <= self.r+fight.ball.r \
                or (self.distance(fight.fire) <= self.r+fight.fire.r and int(fight.enemy.f) == 2) \
                or (self.distance(fight.fire2) <= self.r+fight.fire2.r and int(fight.enemy.f) == 2) \
                or (self.distance(fight.fire3) <= self.r+fight.fire3.r and int(fight.enemy.f) == 2)) \
                    and self.hitTimer==0:
                if self.vy > 0 and self.distance(fight.enemy) <= self.r+fight.enemy.r:
                    fight.enemy.life -= 1
                    self.attacked = True
                    self.vy = -5
                    if fight.enemy.life == 0:
                        game.state = "prison"
                        game.complete = "fight"
                        game.mario.x = game.marioX
                        game.mario.y = game.marioY
                        setup()

                else:
                    self.t=(self.t+1)%60
                    if self.t==0:
                        self.deadtime+=1
                    fight.life -= 1
                    self.vx = -10
                    self.x+=self.vx
                    self.hitTimer=120
                    # if self.deadtime < 3:
                    #     self.r = 0
                    if fight.life == 0:
                         game.state="gameOver"
                         setup()
            

            
#######################################################################################################################
#######################################################################################################################

class Enemy(Creature):
    def __init__ (self,x,y,r,g,x1,x2):
        Creature.__init__ (self,x,y,r,g)
        self.img = loadImage("Sprites-AlexanderBelmont.gif")
        self.vx = 0
        self.frames = 3
        self.f = 0
        self.x1 = x1
        self.x2 = x2
        self.life = 5
        self.attacked = False
        
    def display(self):
        # if self.x < self.x1:
        #     self.vx = 2
        # elif self.x > self.x2:
        #     self.vx = -2
        
        self.update()
        
        # if self.vx != 0:
        
        if fight.timer < 2:
                image(self.img,self.x-self.r-fight.x,self.y-self.r,2*self.r,2*self.r,0,316,56, 368)

        else: 
            self.f=(self.f+0.03)%self.frames
            if int(self.f) == 0:
                image(self.img,self.x-self.r,self.y-self.r,2*self.r,2*self.r,0, 316, 56, 368)
            elif int(self.f) == 1:
                image(self.img,self.x-self.r,self.y-self.r,2*self.r,2*self.r, 0+56+66, 316, 56+56+66, 368)
            elif int(self.f) == 2:
                image(self.img,self.x-self.r,self.y-self.r,2*self.r,2*self.r, 0+64, 316, 56+72, 368)
                # image(self.img,self.x-200-self.r, self.y-self.r,2*self.r,2*self.r, 316+150, 21, 316+200, 21+50)
                # image(self.img,self.x-300-self.r, self.y-self.r,2*self.r,2*self.r, 316+150, 21, 316+200, 21+50)
                # image(self.img,self.x-400-self.r, self.y-self.r,2*self.r,2*self.r, 316+150, 21, 316+200, 21+50)


        

#######################################################################################################################
#######################################################################################################################
class Sphere (Creature):
    def __init__ (self, x, y, r, g):
        Creature.__init__(self,x,y,r,g)
        self.img = loadImage("Sprites-AlexanderBelmont.gif")
        self.vx = -3
        self.vy = 3
    
    def display(self):
        image(self.img,self.x-self.r, self.y-self.r,2*self.r,2*self.r+30, 316+115, 21+40, 316+145, 21+40+35)
        self.update()
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.bounds()
        
    def bounds(self):
        if self.x < 0 or self.x > fight.w:
            self.vx = self.vx*(-1)
        if self.y < 0 or self.y > fight.h:
            self.vy = self.vy*(-1)

#######################################################################################################################
#######################################################################################################################
class Fire (Creature):
    def __init__ (self,x,y,r,g):
        Creature.__init__ (self,x,y,r,g)
        self.img = loadImage("Sprites-AlexanderBelmont.gif")
        self.vx = 0
        self.frames = 3
        self.f = 0
        
    def display(self):
        
        self.update()
        
        if fight.timer > 2:
            self.f=(self.f+0.03)%self.frames
        if int(fight.enemy.f) == 2:
            image(self.img,self.x-self.r, self.y-self.r,2*self.r,2*self.r, 466, 21, 516, 71)
            image(self.img,self.x-self.r, self.y-self.r,2*self.r,2*self.r, 466, 21, 516, 71)
            image(self.img,self.x-self.r, self.y-self.r,2*self.r,2*self.r, 466, 21, 516, 71)

#######################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################
#######################################################################################################################    
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
  
class Level3():
    def __init__(self):
        self.guess = []
        self.guessList = []
        self.guessString = ""
        self.guessCounter = 0
        self.newGuessCounter = 0
        self.guessLimit = 3
        self.guessLength = 6
        self.recInitial = 180
        self.boxWidth = 70
        self.margin = 10
        self.anotherBox = (game.w - self.recInitial*2)/self.guessLength
        self.memoX = 430
        self.memoY = 330
        self.newInput = False
        self.enterX = 410
        self.enterY = 530
        self.enterWidth = 180
        self.enterHeight = 80
        self.answer = "NEW"
        self.answerMessageX = 350
        self.answerMessageY = 500
        self.answerMessageW = 300
        self.answerMessageH = 70
        self.hintx = 425
        self.hinty = 25
        self.hintw = 50
        self.hinth = 5

    def newGame(self):
        self.code = Coded()
    
    def update(self):
        if self.newGuessCounter > self.guessCounter:
            self.guessString = ""
            self.guessString = ''.join(self.guess)
            self.guessAnswer = str(self.code.printAnswer())
            if self.guessString == self.guessAnswer:
               self.answer = "YES"
            else:
                self.answer = "NO"
            self.guessCounter = self.newGuessCounter

    def display(self):
        #image(img,0,0,game.w,game.h)
        background(0)
        fill(255)
        rect(self.memoX-80, self.memoY-70, 300, 100)
        if self.answer == "YES" or self.answer == "NO":
            self.answer = "NEW"
            time.sleep(1)
            stroke(50)
        self.update()
        fill (220,255,70)
        textSize(18)
        text ("You have now reached the last stage of your escape! \nTo go through the final password-protected door, you need to decode the coded password you find in \nthe warden's drawer. The door is protected by a 6-digit numeric password that you need to find out. \nYou have " + str(level3.guessLimit) + " chances to enter the correct password, after which the alarm will ring and the game will end. \nHint: A = 0, U = 0, T = 9, J = 9", 50, 70)
        fill(0)
        textSize(50)
        text(str(self.code.printCode()), self.memoX, self.memoY)
        stroke(0)
        fill(255)
        for i in range(self.guessLength):
            rect(self.recInitial+self.anotherBox*i + 30, 420, self.boxWidth, self.boxWidth)
        fill(0)
        for g in range(len(self.guess)):
            text(self.guess[g], self.recInitial+self.anotherBox*g+self.margin + 40, 410 +self.boxWidth-self.margin)
        fill(80,255,120)
        rect(self.enterX, self.enterY, self.enterWidth, self.enterHeight)
        fill(0)
        textSize(40)
        text('ENTER',self.enterX+30,self.enterY+55)
        if self.answer == "YES":
            stroke(0)
            fill(0,255,0)
            rect(self.answerMessageX, self.answerMessageY, self.answerMessageW, self.answerMessageH)
            textSize(30)
            fill(0)
            stroke(0)
            text("ACCESS GRANTED", self.answerMessageX+35, self.answerMessageY+40) 
            self.guess = []
        elif self.answer == "NO":
            stroke(0)
            fill(255,0,0)
            rect(self.answerMessageX, self.answerMessageY, self.answerMessageW, self.answerMessageH)
            textSize(30)
            fill(0)
            stroke(0)
            text("ACCESS DENIED", self.answerMessageX+35, self.answerMessageY+40)
            self.guess = []
        
            
            
class Coded(Level3):
    def __init__ (self):
        self.stored = open('dict.txt', 'r')
        self.__output = []
        self.__solutions = []
        self.__give = 0
        self.__ans = 0
        self.__r = 0
        self.i = []
        
    def createCoded(self):
        self.i = self.stored.readlines()
        for a in self.i:
            self.__list = a.split()
            self.__output.append(self.__list[0])
            self.__solutions.append(self.__list[1])
        self.__r = random.randint(0, len(self.__output)-1)
        self.__give = self.__output[self.__r]
        self.__ans = self.__solutions[self.__r]

    def printCode(self):
        return self.__give
    
    def printAnswer(self):
        return self.__ans



#######################################################################################################################
#######################################################################################################################

class Welcome():
    def __init__(self):
        self.w = game.w
        self.h = game.h
    
    
    def display(self):
        image(img,0,0,self.w,self.h)
        fill(210,200,0)
        textSize(50)
        text("PRISON BREAK!", game.w/2 - 180, game.header +100)
        stroke(0)
        fill(0)
        rect(100,game.header + 130,game.w - 200,400)
        stroke(255)
        fill (255)
        textSize(18)
        text ('Welcome to Prison Break! You are a convict and you have been planning an escape \nfor months. And tonight is the night when you break out of the prison! \n \nInstructions: \nYou have to find your way through a maze of confusing walls, police dogs, prison \nguards and electric fences and out of the main building, after which you have to \nfight the head guard to obtain the key to the wardens office. In the wardens office, \nyou must decode the password in order to unlock the main gate and escape. \n \nYou will have exactly 15 minutes to complete the above. After 10 minutes, \nyou will be discovered missing from your cell and the alarm will be sounded. \nIf you cannot escape by the end of 15 minutes, you will be caught by the prison \nguards and the game will end.', 130, game.header+160)
class Timer():
    def __init__(self):
        self.timeLimitInMin = 15
        self.timeSixtiethSec = 0
        self.timeSec = 0
        self.timeMin = 0
        self.timeMinRemain = 0
        self.timeSecRemain = 0
        
    def update(self):
        self.timeSixtiethSec += 1
        self.timeSec = int(self.timeSixtiethSec/60)
        self.timeMinRemain = int(self.timeLimitInMin - float(self.timeSec)/60)
        self.timeSecRemain = (self.timeLimitInMin*60 - self.timeSec)%60
        
    def display(self):
        self.update()
        if self.timeSecRemain < 10:
            text("Time: "+str(self.timeMinRemain)+":0"+str(self.timeSecRemain),game.w/2-50,30)
        else:
            text("Time: "+str(self.timeMinRemain)+":"+str(self.timeSecRemain),game.w/2-50,30)
        
class Header():
    def __init__(self):
        self.header = game.header
    
    def display(self):
        stroke(50)
        fill(50)
        rect(0,0,game.w,self.header)
        fill(255)
        stroke(255)
        textSize(20)
        if game.state == "welcome":
            text('Play', 25,30)
        elif game.state == "prison":
            timer.display()
        elif game.state == "fight":
            text("Your Life:"+"*"*fight.life,10,30)
            text("Enemy's Life:"+"*"*fight.enemy.life,fight.w - 250,30)
            timer.display()
        elif game.state == "level3":
            timer.display()
        elif game.state == "gameOver":
            text('Play Again', 25,30)
      
      
###########################
       
class Maze:
    def __init__(self):
        self.w = 800
        self.h = 600
        self.enemies = []
        self.x = 0
        self.state = 'Menu'
        self.name = ""
        self.timer = 0
        self.t = 0
        self.walls = []
        self.name = ""
        self.score = 0
        self.timer = 0

        
    def create(self):
        self.prisoner = Prisoner(45,10,10)
        
        for row in range(len(maze1)):
            for col in range(len(maze1[0])):
                if maze1[row][col] == "#":
                    self.walls.append(Wall(col*29+5,row*29+10, 15, 15))
        self.entrance = Door3(27, 5, 0, 0, 78, 62)
        self.escape = Door3(41*29-2, 20*29-6, 0, 0, 78, 62)
    
    def display(self):
        background(255)
        for w in self.walls:
            w.display()
        
        self.entrance.display()
        self.escape.display()
        
        # self.t = (self.t+1)%32
        
        # if self.t==0: 
        #     self.timer+=1
        
        self.prisoner.display()
        fill(255)

class Door3:
    def __init__ (self,x,y, x1, y1, x2, y2):
        self.x = x
        self.y = y
        self.r = 5
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.img = loadImage('171-Door02.png')
    
    def display (self):
        image(self.img, self.x-maze.x-self.r, self.y-self.r, 36, 36, self.x1, self.y1, self.x2, self.y2)


class Wall:
    def __init__ (self, x, y, r1, r2):
        self.x = x
        self.y = y
        self.r = 29
        self.r1 = r1
        self.r2 = r2
        
    def display (self):
        stroke(0)
        fill(190)
        rect(self.x-5-maze.x, self.y-5, 29, 29)


maze1 = [
        ['#','S','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
        ['#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#'],
        ['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#'],
        ['#',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#'],
        ['#',' ','#','#','#',' ','#','#','#','#','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#'],
        ['#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#'],
        ['#',' ','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#'],
        ['#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#'],
        ['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#',' ','#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#'],
        ['#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#',' ','#'],
        ['#',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#'],
        ['#',' ','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#',' ','#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#'],
        ['#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#'],
        ['#',' ','#','#','#','#','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#'],
        ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],
        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','E','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
        ]

# class Creature:
#     def __init__ (self,x,y,r):
#         self.x = x
#         self.y = y
#         self.vx = 0
#         self.vy = 0
#         self.r = r
    
#     def update(self):
#         self.x += self.vx
#         self.y += self.vy
    
#     def display(self):
#         self.update()
#         stroke(255)
#         fill(0)
    
class Prisoner(Creature):
    def __init__ (self,x,y,r):
        Creature.__init__(self,x,y,r, g)
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False, DOWN:False}
        # print(loadImage('attack_on_titan_rpg_sprite__eren__by_allthelittlewonders-d8oynfh.png'))
        self.img = loadImage('attack_on_titan_rpg_sprite__eren__by_allthelittlewonders-d8oynfh.png')
        self.frames = 3
        self.f = 1
        self.dir = 1
        
    def display(self):
        self.update()
        
        if self.vx != 0 or self.vy != 0:
            self.f = (self.f+0.1)%self.frames
        
        if self.vx > 0 or self.dir ==1:
            image(self.img, self.x-self.r-maze.x, self.y-self.r, 2*self.r, 2*self.r, int(self.f)*32, 64, int(self.f)*32+32, 96)
        elif self.vx < 0  or self.dir ==2:
            image(self.img, self.x-self.r-maze.x, self.y-self.r, 2*self.r, 2*self.r, 64-int(self.f)*32, 32, 96-int(self.f)*32, 64)
        elif self.vy > 0 or self.dir ==3:
            image(self.img, self.x-self.r-maze.x, self.y-self.r, 2*self.r, 2*self.r,int(self.f)*32, 0, int(self.f)*32+32, 32)
        elif self.vy < 0 or self.dir ==4:
            image(self.img, self.x-self.r-maze.x, self.y-self.r, 2*self.r, 2*self.r, 64-int(self.f)*32, 96, 96-int(self.f)*32, 128)
               

    def distance(self,target):
        return ((self.x-target.x)**2+(self.y-target.y)**2)**0.5
    
    def update(self):
        
        if self.keyHandler[RIGHT]:
            self.vx = 2
            self.vy = 0
            self.dir = 1
        elif self.keyHandler[LEFT]:
            self.vx = -2
            self.vy = 0
            self.dir = 2
        elif self.keyHandler[UP]:
            self.vy = -2
            self.vx = 0
            self.dir = 4
        elif self.keyHandler[DOWN]:
            self.vy = 2
            self.vx = 0
            self.dir = 3
        else:
            self.vx = 0
            self.vy = 0
        
        self.x += self.vx
        self.y += self.vy
        
        
            
        if self.x - self.r < 0:
            self.x = self.r
                    
        for w in maze.walls:
            if self.distance(w) <= w.r1:
                if self.vx > 0:
                    self.x = w.x-w.r1
                    self.vx = 0
                elif self.vy > 0:
                    self.y = w.y-w.r1
                    self.vy = 0
                elif self.vx < 0:
                    self.x = w.x+w.r1
                    self.vx = 0
                elif self.vy < 0:
                    self.y = w.y+w.r1
                    self.vy = 0

                # self.x = w.x-self.r
                # self.y = w.y-self.r
    # for e in maze.enemies
    #     if self.distance(e) <= self.r+e.r:
    #         if self.vy < 0:
                # maze.music.stop()
                # self.mazeOver.play()
                # maze.state="inputNae"\
            
        if self.distance(maze.escape) <= self.r+maze.escape.r:
            game.state = "prison"
            print ("yay")
            setup()
                
        if self.x >= maze.w//2:
            maze.x += self.vx           
          
#########################                    
game = Game()
fight = Fight()
welcome = Welcome()
header = Header()
maze = Maze()

def setup():
    size(game.w, game.h)
    path = os.getcwd()
    global img
    global welcome

    background(120)
    if game.state == "welcome":
        img = loadImage('prison_cell-block.jpg')
        nightMusic = SoundFile(this, 'night.wav')
        nightMusic.amp(4)
        nightMusic.loop()
        global nightMusic
        timer = Timer()
        global timer
    elif game.state == "prison":
        #nightMusic.stop()
        game.create()
    elif game.state == "beforeFight":
        img = loadImage('DoorDungeon2.gif')
    elif game.state == "fight":
        fight.create()
        textSize(24)
    elif game.state == "level3":
        img = loadImage('bg.jpg')
        level3 = Level3()
        level3.newGame()
        level3.code.createCoded()
        global level3
    elif game.state == "gameOver":
        background(0)
        dogs = SoundFile(this, 'Dogs Barking-SoundBible.com-625577590.wav')
        dogs.amp(5)
        dogs.play()
        global dogs
        sirens = SoundFile(this, 'Siren_Noise-KevanGC-1337458893.wav')
        sirens.amp(0.1)
        sirens.play()
        global siren
    elif game.state == "maze":
        background(0)
        maze.create()
        global maze

def draw():
    if game.state == "welcome":
        welcome.display()
    elif game.state == "prison":
        background(0)
        game.display()
    elif game.state == "beforeFight":
        stroke(0)
        fill(0,50,80)
        rect(0,0,1000,250)
        image(img,400,0,150,250)
        stroke(0)
        line(0,250,1000,250)
        stroke(0)
        fill(255)
        textSize(20)
        text("You are now in the Admin building. The warden's office is locked and \nthe head-guard holds the key. Fight and defeat the head-guard to unlock \nthe warden's office.",150,300)
        if 420 <= mouseX <= 520 and 570 <= mouseY <= 620:
            fill(0)
        text("FIGHT", 450,600)
    elif game.state == "fight":
        background(0)
        fight.display()
    elif game.state == "level3":
        level3.display() 
    elif game.state == "gameOver":
        textSize(50)
        fill(255,0,0)
        text("YOU HAVE BEEN CAUGHT",200,380)
        text("GAME OVER",350,450)
    elif game.state == "maze":
        maze.display()
    
    header.display()

def keyPressed():
    if game.state == "prison":
        game.mario.keyHandler[keyCode] = True
        #print('pressed', game.mario.keyHandler)
    elif game.state == "fight":
        game.mario.keyHandler[keyCode]=True
    elif game.state == "level3":
        if key == BACKSPACE:
            if len(level3.guess) > 0:
                level3.guess.pop()
        elif key == "1" or key == "2" or key == "3" or key == "4" or key == "5" or key == "6" or key == "7" or key == "8" or key == "9" or key == "0":
            if len(level3.guess) < level3.guessLength:
                level3.guess.append(key)
        elif key == ENTER:
            if len(level3.guess) == level3.guessLength:
                level3.newGuessCounter += 1
    elif game.state == "maze":
        maze.prisoner.keyHandler[keyCode]=True
        
def keyReleased():
    if game.state == "prison":
        game.mario.keyHandler[keyCode] = False
        #print('released', game.mario.keyHandler)
    elif game.state == "fight":
        game.mario.keyHandler[keyCode]=False
    elif game.state == "maze":
        maze.prisoner.keyHandler[keyCode] = False

def mouseClicked():
    if game.state == "welcome":
        if 0 <= mouseX <= 150 and 0 <= mouseY <= game.header:
            game.state = "prison"
            setup()
    elif game.state == "beforeFight":
        if 420 <= mouseX <= 520 and 570 <= mouseY <= 620:
            game.state = "fight"
            setup()        
    elif game.state == "gameOver":
        if 0 <= mouseX <= 200 and 0 <= mouseY <= game.header:
            game.state = "welcome"
            setup()

    elif game.state == "level3":
        if level3.enterX <= mouseX <= level3.enterX + level3.enterWidth and level3.enterY <= mouseY <= level3.enterY+level3.enterHeight:
            if len(level3.guess) == level3.guessLength:
                level3.newGuessCounter += 1
#######################################################################################################################
 