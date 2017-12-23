# -*- coding:utf-8 -*-
import pygame
import time

def main():
    #1.创建一个窗口，用来显示内容
    screen  = pygame.display.set_mode((480,600),0,32)
    #2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png")

    #创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")

    x = 210
    y = 480


    #3.把背景图片放到窗口中显示
    while True:
        #设定需要显示的背景图 ，第2个参数坐标
        screen.blit(background,(0,0))
        screen.blit(hero,(x,y))        
        

        #更新需要显示的内容
        pygame.display.update()

        x += 1
        y -= 1

        #延迟 单位s
        time.sleep(0.05)

if __name__ == "__main__":
    main()