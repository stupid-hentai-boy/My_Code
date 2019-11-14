import pygame, sys, time, random, time 
from pygame.locals import *
from tkinter import _flatten

FPS = 60
fpsClock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Finger Board")
WINDOW_WIDTH = 740
WINDOW_HEIGHT = 500
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32) 
FINGER_BOARD = pygame.image.load("picture/Finger_Board.bmp").convert()
FINGER_BOARD2 = pygame.image.load("picture/guitar_board2.bmp").convert()
GUITAR_HEAD = pygame.image.load("picture/guitar_head.png").convert()
GUITAR_HEAD1 = pygame.image.load("picture/guitar_head1.png").convert_alpha()
GUITAR_HEAD2 = pygame.image.load("picture/guitar_head2.png").convert_alpha()
CONTINUE = pygame.image.load("picture/continue.bmp").convert()
PAUSE = pygame.image.load("picture/pause.bmp").convert()
FINGER_BOARD_BACKGROUND = pygame.image.load("picture/Finger_Board_background.bmp").convert()
FINGER_BOARD_BACKGROUND2 = pygame.image.load("picture/Finger_Board_background2.bmp").convert()
ARROWHEAD = pygame.image.load("picture/arrowhead.png").convert_alpha()
FONTOBJ = pygame.font.Font("freesansbold.ttf", 40)
FONTOBJ2 = pygame.font.Font("freesansbold.ttf", 80)
#START_INTERFACE =  pygame.image.load("").convert()
BOARD_RECT = FINGER_BOARD.get_rect()
BOARD_RECT.center = (WINDOW_WIDTH/2, (WINDOW_HEIGHT/2 + 25))
ARROWHEAD_RECT = ARROWHEAD.get_rect()
#颜色
BLUE = [70, 86, 114]
BLUE_GREEN = (8, 255, 202)
ORANGE = (255, 143, 9)
GREEN = (9, 255, 29)
YELLOW = (239, 226, 2)
RIGHT_COLOR = (228, 255, 68)
WRONG_COLOR = (250, 10, 10)
# 常变量
EIGHTDEGREE = 0
DEVILMODE = 1

YES = 0
NO = 1

# 音源
'''
sd_C = pygame.mixer.Sound("")
sd_hC = pygame.mixer.Sound("")
sd_hhC = pygame.mixer.Sound("")

sd_D = pygame.mixer.Sound("")
sd_hD = pygame.mixer.Sound("")
sd_hhD = pygame.mixer.Sound("")

sd_lE = pygame.mixer.Sound("") 
sd_E = pygame.mixer.Sound("")
sd_hE = pygame.mixer.Sound("")

sd_lF = pygame.mixer.Sound("")
sd_F = pygame.mixer.Sound("")
sd_hF = pygame.mixer.Sound("")

sd_lG = pygame.mixer.Sound("")
sd_G = pygame.mixer.Sound("")
sd_hG = pygame.mixer.Sound("")

sd_lA = pygame.mixer.Sound("")
sd_A = pygame.mixer.Sound("")
sd_hG = pygame.mixer.Sound("")

sd_lB = pygame.mixer.Sound("")
sd_B = pygame.mixer.Sound("")
sd_hB = pygame.mixer.Sound("")
'''

def main():

    CHOICE = EIGHTDEGREE
    while True: # the main loop

        CHOICE = MENU_INTERFACE() # menu
        GAME_START(CHOICE) # 游戏开始
        
        
def MENU_INTERFACE():

    while True:

        return EIGHTDEGREE   

def GAME_START(choice):

    global GAME_LIST, STRCOLOR
    GAME_LIST = NUMBER_FACTORY(EIGHTDEGREE)
    SCORE = 0
    KEY_1 = 0
    KEY_2 = 0
    KEY_3 = 0
    TIMES = 0
    TEMPLE_TIMES = 1
    LIMIT_TIME = 5 * FPS
    TIME_COLOR = [70, 86, 114]
    TIME_COLOR2 = [186, 172, 151]
    L_KEYNUM = KEYNUM = 0
    TM1 = TM2 = TM3 = TM4 = TM5 = TM6 = 0
    STRCOLOR = [0 for i in range(7)]
    for i in range(7):
        STRCOLOR[i] = BLUE

    while True:
        if(TEMPLE_TIMES != TIMES):
            TEMPLE_TIMES = TIMES
            THE_TONE, THE_NUMBER = TONE_SYMBOL(TIMES)
        DISPLAYSURF.blit(FINGER_BOARD_BACKGROUND, (0, 50))
        DISPLAYSURF.blit(FINGER_BOARD_BACKGROUND2, (0, 0))
        DISPLAYSURF.blit(CONTINUE, (685, 9))
        DISPLAYSURF.blit(FINGER_BOARD, BOARD_RECT)
        DISPLAYSURF.blit(GUITAR_HEAD, (0, 200))
        DISPLAYSURF.blit(GUITAR_HEAD1, (0, 150))
        DISPLAYSURF.blit(GUITAR_HEAD2, (0, 350))
        DISPLAYSURF.blit(FINGER_BOARD2, (730, 200))

        DRAW_CIRCLE()
        FRETWIRE()
        STRINGS()
        BOARD_Y, BOARD_X = ARROWHEADPOS()
        SCORETEXT = FONTOBJ.render(" %d / 21" %SCORE, True, BLUE)
        TONETEXT = FONTOBJ2.render("%s%d" %(THE_TONE, THE_NUMBER), True, BLUE)
        DISPLAYSURF.blit(SCORETEXT, (10,10))    
        DISPLAYSURF.blit(TONETEXT, (320, 63))
        #TIME_LINE
        pygame.draw.line(DISPLAYSURF, TIME_COLOR2, (220, 425), (520, 425), 20)
        pygame.draw.line(DISPLAYSURF, TIME_COLOR, (220, 425), (220 + LIMIT_TIME, 425), 20)
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):

                #DECISIION = EXIT_INTERFACE()# 结束UI
                #if DECISION == YES:
                    pygame.quit()
                    sys.exit()
               # else:
                    #break
            elif event.type == KEYUP and event.key == K_SPACE:
                Break = False
                while True:

                    DISPLAYSURF.blit(FINGER_BOARD_BACKGROUND, (0, 50))
                    DISPLAYSURF.blit(FINGER_BOARD_BACKGROUND2, (0, 0))
                    DISPLAYSURF.blit(PAUSE, (685, 9))
                    DISPLAYSURF.blit(FINGER_BOARD, BOARD_RECT)
                    DISPLAYSURF.blit(GUITAR_HEAD, (0, 200))
                    DISPLAYSURF.blit(GUITAR_HEAD1, (0, 150))
                    DISPLAYSURF.blit(GUITAR_HEAD2, (0, 350))
                    DISPLAYSURF.blit(FINGER_BOARD2, (730, 200))

                    DRAW_CIRCLE()
                    FRETWIRE()
                    STRINGS()
                    BOARD_Y, BOARD_X = ARROWHEADPOS()
                    SCORETEXT = FONTOBJ.render(" %d / 21" %SCORE, True, BLUE)
                    TONETEXT = FONTOBJ2.render("%s%d" %(THE_TONE, THE_NUMBER), True, BLUE)
                    DISPLAYSURF.blit(SCORETEXT, (10,10))    
                    DISPLAYSURF.blit(TONETEXT, (320, 63))
                    #TIME_LINE
                    pygame.draw.line(DISPLAYSURF, TIME_COLOR2, (220, 425), (520, 425), 20)
                    pygame.draw.line(DISPLAYSURF, TIME_COLOR, (220, 425), (220 + LIMIT_TIME, 425), 20)
                    pygame.display.update()
                    fpsClock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == KEYUP and event.key == K_SPACE:
                            Break = True
                    if Break == True:
                        break

            elif event.type == MOUSEBUTTONUP and (BOARD_Y != 6, BOARD_X != 12):
                
                TONE = GAME_LIST[TIMES]

                if TONE == 1: # C

                    if (BOARD_Y, BOARD_X) == (4, 3):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (5, 8):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 2: # hC

                    if (BOARD_Y, BOARD_X) == (1, 1):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (2, 5):
                        KEY_2 = 1
                    elif (BOARD_Y, BOARD_X) == (3, 10):
                        KEY_3 = 1
                elif TONE == 3: # hhC     
                    
                    if (BOARD_Y, BOARD_X) == (0, 8):
                        KEY_1 = 1
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 4: # D

                    if (BOARD_Y, BOARD_X) == (3, 0):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (4, 5):
                        KEY_2 = 1
                    elif (BOARD_Y, BOARD_X) == (5, 10):
                        KEY_3 = 1
                elif TONE == 5: # hD

                    if (BOARD_Y, BOARD_X) == (1, 3):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (2, 7):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 6: # hhD

                    if (BOARD_Y, BOARD_X) == (0, 10):
                        KEY_1 = 1
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 7: # lE
                    if (BOARD_Y, BOARD_X) == (5, 0):
                        KEY_1 = 1
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 8: # E

                    if (BOARD_Y, BOARD_X) == (3, 2):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (4, 7):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 9: # hE

                    if (BOARD_Y, BOARD_X) == (0, 0):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (1, 5):
                        KEY_2 = 1
                    elif (BOARD_Y, BOARD_X) == (2, 9):
                        KEY_3 = 1
                elif TONE == 10: # lF

                    if (BOARD_Y, BOARD_X) == (5, 1):
                        KEY_1 = 1
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 11: # F

                    if (BOARD_Y, BOARD_X) == (3, 3):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (4, 8):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 12: # hF

                    if (BOARD_Y, BOARD_X) == (0, 1):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (1, 6):
                        KEY_2 = 1
                    elif (BOARD_Y, BOARD_X) == (2, 10):
                        KEY_3 = 1
                elif TONE == 13: # lG

                    if (BOARD_Y, BOARD_X) == (5, 3):
                        KEY_1 = 1
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 14: # G

                    if (BOARD_Y, BOARD_X) == (2, 0):
                        KEY_1 = 1
                    if (BOARD_Y, BOARD_X) == (3, 5):
                        KEY_2 = 1
                    if (BOARD_Y, BOARD_X) == (4, 10):
                        KEY_3 = 1
                elif TONE == 15: # hG

                    if (BOARD_Y, BOARD_X) == (0, 3):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (1, 8):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 16: # lA

                    if (BOARD_Y, BOARD_X) == (4, 0):
                        KEY_1 = 1 
                    elif (BOARD_Y, BOARD_X) == (5, 5):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 17: # A
               
                    if BOARD_X == 7:
                        KEY_1 = 1
                 
                    elif (BOARD_Y, BOARD_X) == (2, 2):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 18: # hA

                    if (BOARD_Y, BOARD_X) == (1, 10):
                         KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (0, 5):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 19: # lB

                    if (BOARD_Y, BOARD_X) == (4, 2):
                        KEY_1 = 1 
                    elif (BOARD_Y, BOARD_X) == (5, 7):
                        KEY_2 = 1
                        KEY_3 = 1
                elif TONE == 20: # B

                    if (BOARD_Y, BOARD_X) == (1, 0):
                        KEY_1 = 1
                    elif (BOARD_Y, BOARD_X) == (2, 4):
                        KEY_2 = 1
                    elif (BOARD_Y, BOARD_X) == (3, 9):
                        KEY_3 = 1
                elif TONE == 21: # hB

                    if (BOARD_Y, BOARD_X) == (0, 7):
                        KEY_1 = 1
                        KEY_2 = 1
                        KEY_3 = 1

                KEYNUM = KEY_1 + KEY_2 + KEY_3
                if KEYNUM > L_KEYNUM:
                    STRCOLOR[BOARD_Y] = RIGHT_COLOR
                    L_KEYNUM = KEYNUM
                elif KEYNUM == L_KEYNUM:
                    if STRCOLOR[BOARD_Y] != RIGHT_COLOR:
                        STRCOLOR[BOARD_Y] = WRONG_COLOR

                if KEY_1 * KEY_2 * KEY_3 == 1 and LIMIT_TIME > 0:
                    SCORE += 1
                    TIMES += 1
                    STRINGS() # 让黄色再保持0.5秒
                    ARROWHEADPOS()
                    pygame.display.update()
                    time.sleep(0.5)
                    KEY_1 = KEY_2 = KEY_3 = 0
                    LIMIT_TIME = 5 * FPS
                    TIME_COLOR = [70, 86, 114]
                    L_KEYNUM = KEYNUM = 0
                    for i in range(7):
                        STRCOLOR[i] = BLUE
        
        if LIMIT_TIME <= 0:
            TIMES += 1
            KEY_1 = KEY_2 = KEY_3 = 0
            LIMIT_TIME = 5 * FPS
            TIME_COLOR = [70, 86, 114]
            L_KEYNUM = KEYNUM = 0
            for i in range(7):
                STRCOLOR[i] = BLUE

        LIMIT_TIME -= 1
        TIME_COLOR[0] += 0.6
        TIME_COLOR[1] -= 0.1
        TIME_COLOR[2] -= 0.1
        #计时器

        if(STRCOLOR[0] == WRONG_COLOR):

            TM1 += 1
            if TM1 == 20:
                STRCOLOR[0] = BLUE
                TM1 = 0
        if(STRCOLOR[1] == WRONG_COLOR):

            TM2 += 1
            if TM2 == 20:
                STRCOLOR[1] = BLUE
                TM2 = 0
        if(STRCOLOR[2] == WRONG_COLOR):

            TM3 += 1
            if TM3 == 20:
                STRCOLOR[2] = BLUE
                TM3 = 0
        if(STRCOLOR[3] == WRONG_COLOR):

            TM4 += 1
            if TM4 == 20:
                STRCOLOR[3] = BLUE
                TM4 = 0
        if(STRCOLOR[4] == WRONG_COLOR):

            TM5 += 1
            if TM5 == 20:
                STRCOLOR[4] = BLUE
                TM5 = 0
        if(STRCOLOR[5] == WRONG_COLOR):

            TM6 += 1
            if TM6 == 20:
                STRCOLOR[5] = BLUE
                TM6 = 0
        if TIMES == 20:
            break
        pygame.display.update()
        fpsClock.tick(FPS)

#def EXIT_INTERFACE():

def NUMBER_FACTORY(choice):

    D_BOARD = [0 for col in range(21)]
    G_BOARD = [[0 for col in range(3)]for row in range(7)]
    num = 1
    if choice == EIGHTDEGREE:
        
        for row in range(7):
            for col in range(3):
                G_BOARD[row][col] = num
                num += 1
            random.shuffle(G_BOARD[row])
        random.shuffle(G_BOARD)
        G_BOARD = list(_flatten(G_BOARD))
    return (G_BOARD)

    if choice == DEVILMODE:
        for i in range(21):
            D_BOARD[i] = num
            num += 1
        rangdom.shuffle(D_BOARD)
    return (D_BOARD)

def ARROWHEADPOS():
 
    mouse_x, mouse_y = pygame.mouse.get_pos()
    X = mouse_x - 10 # (740 - 720) / 2
    Y = mouse_y - 200 # 200 = 图1 + 图2
    row = 6
    col = 12
    if X > 0 and X < 720:
        if Y > 0 and Y < 180:
            row = Y / 30 #游戏板上的位置
            col = X / 60
            ARROWHEAD_RECT.center = ((30 + 60 * int(col) + 10), (-30 + 30 * int(row) + 200))
            DISPLAYSURF.blit(ARROWHEAD, ARROWHEAD_RECT)
 
    return(int(row), int(col))

def STRINGS():
    # 弦
    WSTRING = 8
    pygame.draw.line(DISPLAYSURF, STRCOLOR[0], (0, 200), (740, 200), WSTRING)
    pygame.draw.line(DISPLAYSURF, STRCOLOR[1], (0, 230), (740, 230), WSTRING)
    pygame.draw.line(DISPLAYSURF, STRCOLOR[2], (0, 260), (740, 260), WSTRING)
    pygame.draw.line(DISPLAYSURF, STRCOLOR[3], (0, 290), (740, 290), WSTRING)
    pygame.draw.line(DISPLAYSURF, STRCOLOR[4], (0, 320), (740, 320), WSTRING)
    pygame.draw.line(DISPLAYSURF, STRCOLOR[5], (0, 350), (740, 350), WSTRING)
def FRETWIRE():
    # 品柱
    WFRET = 4
    pygame.draw.line(DISPLAYSURF, (58, 74, 102), (70, 200), (70, 350), 15)
    pygame.draw.line(DISPLAYSURF, BLUE, (130, 200), (130, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (190, 200), (190, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (250, 200), (250, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (310, 200), (310, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (370, 200), (370, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (430, 200), (430, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (490, 200), (490, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (550, 200), (550, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (610, 200), (610, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (670, 200), (670, 350), WFRET)
    pygame.draw.line(DISPLAYSURF, BLUE, (730, 200), (730, 350), WFRET)

def TONE_SYMBOL(times):
    
    tone = GAME_LIST[times]
    the_tone = 'C'
    the_number = 4
    if tone >= 1 and tone <= 3:
        the_tone = 'C'
        the_number = tone + 3
    elif tone >= 4 and tone <= 6:
        the_tone = 'D'
        the_number = tone  
    elif tone >= 7 and tone <= 9:
        the_tone = 'E'
        the_number = tone - 4
    elif tone >= 10 and tone <= 12:
        the_tone = 'F'
        the_number = tone - 7
    elif tone >= 13 and tone <= 15:
        the_tone = 'G'
        the_number = tone - 10
    elif tone >= 16 and tone <= 18:
        the_tone = 'A'
        the_number = tone - 13
    elif tone >= 19 and tone <= 21:
        the_tone = 'B'
        the_number = tone - 16
    return (the_tone, the_number)
def DRAW_CIRCLE():

    pygame.draw.circle(DISPLAYSURF, YELLOW, (220, 275), 9, 0)
    pygame.draw.circle(DISPLAYSURF, GREEN, (340, 275), 9, 0)
    pygame.draw.circle(DISPLAYSURF, ORANGE, (460, 275), 9, 0)
    pygame.draw.circle(DISPLAYSURF, BLUE_GREEN, (580, 275), 9, 0)
if __name__ == "__main__":

    main()
