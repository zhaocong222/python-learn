# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time

class HeroPlane(object):
    def __init__(self,screen_temp):
        #创建一个飞机图片
        self.image = pygame.image.load("./feiji/hero1.png")
        self.x = 210
        self.y = 480
        self.screen = screen_temp
        self.bullet_list = [] #存储发射出去的子弹

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        #显示子弹
        for bullet in self.bullet_list:
            #显示子弹
            bullet.display()
            #改变当前子弹坐标
            bullet.move()

    def move_left(self):
        self.x -= 5
    
    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))


#子弹类
class Bullet(object):
    def __init__(self,screen_temp,x,y):
        #创建一个子弹图片
        self.image = pygame.image.load("./feiji/bullet.png")
        self.screen = screen_temp
        self.x = x + 40
        self.y = y - 20

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= 5

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

    #3.把背景图片放到窗口中显示
    while True:
        #设定需要显示的背景图 ，第2个参数坐标
        screen.blit(background,(0,0))
        hero.display()
        #更新需要显示的内容
        pygame.display.update()
        
        #键盘控制
        key_control(hero)

        #延迟 单位s
        time.sleep(0.01)

if __name__ == "__main__":
    main()