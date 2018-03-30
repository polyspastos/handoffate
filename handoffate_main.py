import pygame as pg
import ctypes
import time
import random
import sys


user32 = ctypes.windll.user32
# print(user32.GetSystemMetrics(0))
# print(user32.GetSystemMetrics(1))

pg.init()
pg.mixer.init()
pg.font.init()


calibri300 = pg.font.SysFont('Calibri', 300)
calibri25 = pg.font.SysFont('Calibri', 25, bold=True)

fps = 30

display_width = user32.GetSystemMetrics(0)
display_height = user32.GetSystemMetrics(1)

gd = pg.display.set_mode((display_width, display_height), pg.FULLSCREEN)
pg.display.set_caption('Hands of Fate')

black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 140, 0)
orange_bright = (255, 190, 0)
forestgreen = (24, 139, 34)
forestgreen_bright = (24, 189, 34)
red = (255, 0, 0)

background_color1 = (255, 195, 160)
background_color2 = (134, 102, 75)
background_main_menu = (130, 150, 196)

clock = pg.time.Clock()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    # print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(gd, ac, (x, y, w, h))

        if click[0] == 1 and action is not None:
            action()
    else:
        pg.draw.rect(gd, ic, (x, y, w, h))

    smallText = pg.font.SysFont("Calibri", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gd.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def intro_card(x, y):
    pg.draw.rect(gd, white, (x, y, display_width / 10, display_height / 4))


def intro():
    gd.fill(background_color2)
    pg.display.update()
    for k in range(3):
        # time.sleep(0.1)
        pg.display.flip()
        for i in range(8):
            intro_card(display_width / 10 + i * 200, 100 + k * 300)
            # time.sleep(0.2)
            pg.display.flip()
            rand1_to_3 = random.randint(1, 3)
            pg.mixer.music.load('sounds/CardPutDown{}.wav'.format(rand1_to_3))
            pg.mixer.music.play(0)
            time.sleep(random.uniform(0.1, 0.4))
    handoffate_str = 'Hand of Fate'
    handoffate_str_nospace = handoffate_str.replace(' ', '')

    for x in range(0, len(handoffate_str_nospace)):
        handoffate_char = handoffate_str_nospace[x]
        intro_title = calibri300.render(handoffate_char, False, orange)
        time.sleep(0.2)
        pg.display.flip()
        pg.mixer.music.load('sounds/anvil1.mp3')
        pg.mixer.music.play(0)
        if x < 4:
            a = 120
            b = 208
            
            gd.blit(
                intro_title,
                (a +
                 display_width /
                 4 +
                 x *
                 b,
                 display_height /
                 10))
        if x >= 4 and x < 6:
            a = 330
            b = 216
            
            gd.blit(intro_title, (a + display_width / 4 +
                               (x - 4) * b, display_height / 2.67))
        if x >= 6:
            a = 150
            b = 200
            gd.blit(intro_title, (a + display_width / 4 +
                               (x - 6) * b, display_height / 1.55))

    press_enter_to_continue1 = calibri25.render(
        'Press Enter', False, forestgreen)
    gd.blit(
        press_enter_to_continue1,
        (display_width - 300,
         display_height - 250))
    press_enter_to_continue2 = calibri25.render(
        'to continue!', False, forestgreen)
    gd.blit(
        press_enter_to_continue2,
        (display_width - 300,
         display_height - 200))
    pg.display.update()

    continue_1 = False

    while not continue_1:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    continue_1 = True


def message_to_screen(msg, color, pos):
    screen_text = calibri25.render(msg, True, color)
    gd.blit(screen_text, pos)


class Card(object):  # nincs kész
    def __init__(self):
        self.image = pg.Surface((200, 500))
        self.update()

    def update(self):
        # hogyan adom be ennek az adatokat?
        self.name = 'Village Commoner'
        self.mana_cost = 1
        # self.influence=[1e]
        self.image.clear()
        self.image.blit(calibri25.render(self.name), (0, 0))
        self.image.blit(calibri25.render(self.mana_cost), (160, 0))
        self.image.blit(calibri25.render(self.atk), (460, 0))
        self.image.blit(calibri25.render(self.hp), (460, 160))
        # self.image.blit(calibri25.render(self.influence), (?, ?))

    def draw(self, surface, pos):
        surface.blit(self.image, pos)


def quitgame():
    pg.quit()
    sys.exit()


def gameLoop():
    gd.fill(background_color1)
    message_to_screen("Test mode. Press T to set gameOver=True.", forestgreen, [
                      display_width / 2 - 200, display_height / 2])  # new line?
    message_to_screen("Press Esc to activate the Main Menu.", forestgreen, [
                      display_width / 2 - 200, display_height / 2 + 50])


# card1=Card()
# card1.update() #?

    pg.display.update()

    gameOver = False
    gameExit = False

    while gameOver == False:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_t:
                    gameOver = True
                if event.key == pg.K_ESCAPE:
                    while True:
                        for event in pg.event.get():
                            gd.fill(background_main_menu)
                            mouse = pg.mouse.get_pos()
                            button(
                                "New Game",
                                display_width/2-display_width/32,
                                display_height/2-display_height/16,
                                display_width/16,
                                display_height/16,
                                forestgreen,
                                forestgreen_bright,
                                gameLoop)
                            button(
                                "Quit",
                                display_width/2-display_width/32,
                                display_height/2,
                                display_width/16,
                                display_height/16,
                                forestgreen,
                                forestgreen_bright,
                                quitgame)
                            pg.display.update()
##                        for event in pg.event.get(
##                        ):  # működik, de biztos, hogy így kell csinálni?
##                            mouse = pg.mouse.get_pos()
##                            if display_width / 2 + \
##                                    100 > mouse[0] > display_width / 2 and 450 + 50 > mouse[1] > 450:
##                                pg.draw.rect(
##                                    gd, forestgreen_bright, (display_width / 2, 450, 100, 50))
##                            else:
##                                pg.draw.rect(
##                                    gd, forestgreen, (display_width / 2, 450, 100, 50))
##                            if display_width / 2 + \
##                                    100 > mouse[0] > display_width / 2 and 550 + 50 > mouse[1] > 550:
##                                pg.draw.rect(
##                                    gd, forestgreen_bright, (display_width / 2, 550, 100, 50))
##                            else:
##                                pg.draw.rect(
##                                    gd, forestgreen, (display_width / 2, 550, 100, 50))
##                            pg.display.update()

    while not gameExit:
        while gameOver:
            gd.fill(orange)
            message_to_screen(
                "Game over. Press C to play again or Q to quit", forestgreen, [
                    display_width / 2 - 200, display_height / 2])
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pg.K_c:
                        gameOver = False
                        gameLoop()
                    if event.key == pg.K_t:
                        gameOver = True

    pg.quit()
    sys.exit()



#intro()
clock.tick(fps)
gameLoop()


# while True:
# for event in pg.event.get():
# print(event)
# if event.type == pg.KEYDOWN:
# if event.key == pg.K_ESCAPE:
# ide kell majd a main menu
# pg.quit()
# if event.key == pg.K_RETURN:
# gd.fill(background_main_menu)
