import pygame, sys

#initialization
pygame.init()

# caption and icon
pygame.display.set_caption('TicTacToe')
ICON = pygame.image.load('XO.png'); ICON = pygame.transform.scale(ICON, (50,32))
pygame.display.set_icon(ICON)

# SCREEN
SCREEN = pygame.display.set_mode((450,600))
SCREEN.fill((143,219,222))
# XO
X = pygame.image.load('X.png'); X = pygame.transform.scale(X, (60,110))
O = pygame.image.load('O.png'); O = pygame.transform.scale(O, (60,110))
#BOARD
BOARD = [
    True, True, True,
    True, True, True,
    True, True, True
]
#current player
player = X
def switch():
    global player, X, O
    if player == X:
        player = O
    else:
        player = X
            
# exit
def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# check for win
def check_for_win():
    global BOARD, X, O
    # horizontal win
    for i in range(0, 7, 3):
        if BOARD[i] == BOARD[i+1] == BOARD[i+2] != True:
            return f'PLAYER {BOARD[i]} WON'
    # vertical win
    for i in range(3):
        if BOARD[i] == BOARD[i+3] == BOARD[i+6] != True:
            return f'PLAYER {BOARD[i]} WON'
    # diagonal win
    if BOARD[0] == BOARD[4] == BOARD[8] != True:
        return f'PLAYER {BOARD[0]} WON'
    if BOARD[2] == BOARD[4] == BOARD[6] != True:
        return  f'PLAYER {BOARD[2]} WON'

def change_board(x):
    global BOARD
    if player == X:
        BOARD[x] = 'X'
    else:
        BOARD[x] = 'O'

# font
font = pygame.font.SysFont('Comics Sans MS', 70)
font2 = pygame.font.SysFont('Comics Sans MS', 40)
home = font2.render('PRESS SPACE BAR TO START', True, (255,255,255))
run = True

# __home__
while run:
    SCREEN.blit(home, (20, 450))
    exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        run = False
    pygame.display.flip()
# __main__
# empty screen
SCREEN.fill((153,225,212))
# draw lines
LINES = [(150,50),(150,550), (300,50),(300,550), (50,200),(400,200), (50,400),(400,400)]
COLOR = (89,89,94)
for i in range(0, 8, 2):
    pygame.draw.line(SCREEN, COLOR, LINES[i], LINES[i+1], 5)

while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # row 1
            if pos[1] in range(0, 200):
                # col 1
                if pos[0] in range(0,150) and BOARD[0] == True:
                    SCREEN.blit(player, (50,70))
                    change_board(0)
                    switch()
                # col 2
                if pos[0] in range(150,300) and BOARD[1] == True:
                    SCREEN.blit(player, (200,70))
                    change_board(1)
                    switch()
                # col 3
                if pos[0] in range(300,450) and BOARD[2] == True:
                    SCREEN.blit(player, (325,70))
                    change_board(2)
                    switch()
            # row 2
            if pos[1] in range(200, 400):
                # col 1
                if pos[0] in range(0,150) and BOARD[3] == True:
                    SCREEN.blit(player, (50,250))
                    change_board(3)
                    switch()
                # col 2
                if pos[0] in range(150,300) and BOARD[4] == True:
                    SCREEN.blit(player, (200,250))
                    change_board(4)
                    switch()
                # col 3
                if pos[0] in range(300,450) and BOARD[5] == True:
                    SCREEN.blit(player, (325,250))
                    change_board(5)
                    switch()
            # row 1
            if pos[1] in range(400, 600):
                # col 1
                if pos[0] in range(0,150) and BOARD[6] == True:
                    SCREEN.blit(player, (50,425))
                    change_board(6)
                    switch()
                # col 2
                if pos[0] in range(150,300) and BOARD[7] == True:
                    SCREEN.blit(player, (200,425))
                    change_board(7)
                    switch()
                # col 3
                if pos[0] in range(300,450) and BOARD[8] == True:
                    SCREEN.blit(player, (325,425))
                    change_board(8)
                    switch()

    # check for win
    win = font.render(check_for_win(), True, (255, 255, 255))
    SCREEN.blit(win, (40, 270))

    pygame.display.flip()
