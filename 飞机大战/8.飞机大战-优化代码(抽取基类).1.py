# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
import random

class Base(object):
    
    def __init__(self,screen_temp,x,y,image_name):
        self.image = pygame.image.load(image_name)
        self.x = x
        self.y = y
        self.screen = screen_temp

#飞机基类
class BasePlane(Base):
    def __init__(self,screen_temp, x, y, image_name):
        Base.__init__(self,screen_temp, x, y, image_name)
        self.bullet_list = []#存储发射出去的子弹对象引用

    #显示
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

        for bullet in self.bullet_list:
            #显示子弹
            bullet.display()
            #改变当前子弹坐标
            bullet.move()
            #判断子弹是否越界
            if bullet.judge():
                self.bullet_list.remove(bullet) #删除子弹


#主机
class HeroPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,210,480,"./feiji/hero1.png")

    def move_left(self):
        self.x -= 5
    
    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

#敌机
class EnemyPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,210,10,"./feiji/enemy0.png")
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > (480 - 50):
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1,100)
        if  random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))


#子弹基类
class BaseBullet(Base): 
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")
    
    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0 :
            return True
        else:
            return False

#敌机子弹
class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+25,y+40,"./feiji/bullet1.png")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y >600 :
            return True
        else:
            return False

def key_control(hero_temp):
    #获取事件，比如按键等
    for event in pygame.event.get():
   
        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero_temp.move_left()

            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero_temp.move_right()

            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                #开火
                hero_temp.fire()


def main():
    #1.创建一个窗口，用来显示内容
    screen  = pygame.display.set_mode((480,600),0,32)
    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    #创建一个飞机对象
    hero = HeroPlane(screen)

    #创建一个敌机
    enemy = EnemyPlane(screen)

    #3.把背景图片放到窗口中显示
    while True:
        screen.blit(background, (0,0))
        hero.display()
        enemy.display()
        enemy.move()#调用敌机的移动方法
        enemy.fire()#敌机开火
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()