# IMPORTS
import pygame as pg
import sys
import time
from pygame.locals import *
import os
from pyvidplayer2 import Video

count = 0
width = 1280
height = 720
white = (255, 255, 255)
game_blue = (0, 150, 255)
winner = None
win_direction = None
continue_game = None
display = True

pg.init()

pg.font.init()
pg.mixer.init()
pg.display.set_caption("Connect 4")

# CONSTANTS
FPS = 60
table1 = ["","","","",""]
table2 = ["","","","",""]
table3 = ["","","","",""]
table4 = ["","","","",""]
grand_table = [table1,table2,table3,table4]
current = 'X'
count_row = 0
X_SCORE = 0
O_SCORE = 0
STREAK_COUNT = ['',0]
username1 = None
username2 = None
first_name = False
message = None

# IMPORTS
input_rect = pg.Rect(((width/2)-100), 300, 200, 30)
submit_rect = pg.Rect(((width/2)-50), 350, 100, 30)
quit_rect = pg.Rect(((width/2)-97), 305, 195, 54)
back_rect = pg.Rect(18, 12, 100, 28)

left_bar = pg.Rect(0,0, 200,50)
left_bar_on = pg.Rect(10,10, 180,30)
right_bar = pg.Rect(width - 200,0, 200,50)
right_bar_on = pg.Rect(width - 190,10, 180,30)
connect_rect = pg.Rect(200, 200, 800, 400)

board = pg.image.load("Assets/connect board.png")
red_score_board = pg.image.load("Assets/score board.png")
yellow_score_board = pg.image.load("Assets/score board2.png")
red_piece = pg.image.load("Assets/piece.png")
yellow_piece = pg.image.load("Assets/piece2.png")
streak = pg.image.load("Assets/Streak symbol.png")
submit_button = pg.image.load("Assets/submit button.png")
quit_button = pg.image.load("Assets/quit button.png")
back_button = pg.image.load("Assets/back button.png")
yellow_vertical = pg.image.load("Assets/yellow vertical.png")
red_vertical = pg.image.load("Assets/red vertical.png")
yellow_horizontal = pg.image.load("Assets/yellow horizontal.png")
red_horizontal = pg.image.load("Assets/red horizontal.png")
yellow_diagonal = pg.image.load("Assets/yellow diagonal.png")
red_diagonal = pg.image.load("Assets/red diagonal.png")

bg = pg.image.load("Assets/background.png")
draw_bg = pg.image.load('Assets/draw.png')
win_bg = pg.image.load('Assets/win.png')
general_bg = pg.image.load('Assets/general_bg.png')

# transformations

# board details
board = pg.transform.scale(board, (880, 680))
red_score_board = pg.transform.scale(red_score_board, (120, 220))
yellow_score_board = pg.transform.scale(yellow_score_board, (120, 220))
red_piece = pg.transform.scale(red_piece, (120, 120))
yellow_piece = pg.transform.scale(yellow_piece, (120, 120))
streak = pg.transform.scale(streak, (20,20))
icon = pg.transform.scale(board, (32, 32))
submit_button = pg.transform.scale(submit_button, (120, 30))
quit_button = pg.transform.scale(quit_button, (220, 62))
back_button = pg.transform.scale(back_button, (120, 30))

# line details
yellow_vertical = pg.transform.scale(yellow_vertical, (15, 620))
red_vertical = pg.transform.scale(red_vertical, (15, 620))
yellow_horizontal = pg.transform.scale(yellow_horizontal, (620, 15))
red_horizontal = pg.transform.scale(red_horizontal, (620, 15))
yellow_diagonal = pg.transform.scale(yellow_diagonal, (600, 600))
red_diagonal = pg.transform.scale(red_diagonal, (600, 600))
yellow_diagonal_flip = pg.transform.flip(yellow_diagonal, True, False)
red_diagonal_flip = pg.transform.flip(red_diagonal, True, False)

# background details
bg = pg.transform.scale(bg, (width, height))
draw_bg = pg.transform.scale(draw_bg, (width, height))
win_bg = pg.transform.scale(win_bg, (width, height))
general_bg = pg.transform.scale(general_bg, (width, height))

KEY_SOUND = pg.mixer.Sound(os.path.join("Audio", "keyboard.mp3"))
IN_GAME_SOUND = pg.mixer.Sound(os.path.join("Audio", "ingame.mp3"))
EXIT_SOUND = pg.mixer.Sound(os.path.join("Audio", "exit.mp3"))
CLICK_SOUND = pg.mixer.Sound(os.path.join("Audio", "buttonclick.mp3"))
BACK_SOUND = pg.mixer.Sound(os.path.join("Audio", "back.mp3"))
WIN_SOUND = pg.mixer.Sound(os.path.join("Audio", "win.mp3"))

# adjusting volumes
IN_GAME_SOUND.set_volume(0.2)
BACK_SOUND.set_volume(0.2)
EXIT_SOUND.set_volume(0.1)

FONT1 = pg.font.Font("Font/Poppins/Poppins-Regular.ttf", 18)
HEADER = pg.font.Font("Font/Poppins/Poppins-Bold.ttf", 30)
INTRO_FONT = pg.font.Font("Font/Mileast/Mileast.otf", 30)
SCORE_FONT = pg.font.Font('Font/Trilfullnt/Trifullnt.otf', 60)
STREAK_FONT = pg.font.Font('Font/Trilfullnt/Trifullnt.otf', 30)
QUIT_FONT = pg.font.Font('Font/Trilfullnt/Trifullnt.otf', 30)
MESSAGE_FONT = pg.font.Font("Font/Poppins/Poppins-Regular.ttf", 15)

pg.display.set_icon(icon)
screen = pg.display.set_mode((width, height), 0, 32)


color_active = pg.Color('thistle1') 
color_passive = pg.Color(125, 249, 255)
color = color_passive
font = pg.font.Font(None, 30)
font2 = pg.font.Font(None, 20)


# START FUNCTION
def cover():
    try:
        video = Video('Assets/Video.mp4')
        while video.active:
            key = None
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    key = pg.key.name(event.key)

            if key == "m":
                video.toggle_mute()
            if key == 'space':
                video.close()
                break
            if video.draw(screen, (0, 0), force_draw=False):
                pg.display.update()
    
            pg.time.wait(16)

    except:
        proceed = False
        while proceed == False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    key = pg.key.name(event.key)
                    proceed = True
                    break
                    
            screen.blit(bg, (0,0))
            key = INTRO_FONT.render("Press any key to proceed", 1, (0, 0, 0))
            screen.blit(key, ((width/2)-(key.get_width()/2), 700)) 
            pg.display.flip()
            clock = pg.time.Clock()
            clock.tick(60)
            pg.time.delay(200)
cover()  

def start():
    global username1, username2, first_name, message
    user_text = '' 
    active = False
    name = False

    while not name:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit() 
            if event.type == pg.MOUSEBUTTONDOWN:
                if submit_rect.collidepoint(event.pos):
                    CLICK_SOUND.play()
                    if user_text != "":
                        KEY_SOUND.fadeout(1000)
                        if username1:
                            first_name = True
                            user_text = ''
                        if username2:
                            name = True
                            if len(username1.strip()) > 9:
                                username1 = username1[:8]+'-'
                            if len(username2.strip()) > 9:
                                username2 = username2[:8]+'-'
                            return 'DONE'
                elif input_rect.collidepoint(event.pos): 
                    active = True
                else: 
                    active = False
            if event.type == pg.KEYDOWN:
                KEY_SOUND.stop()
                KEY_SOUND.play()
                # Check for backspace 
                if event.key == pg.K_BACKSPACE: 
    
                    # get text input from 0 to -1 i.e. end. 
                    user_text = user_text[:-1] 
    
                # Unicode standard is used for string 
                # formation 
                else: 
                    user_text += event.unicode

        screen.blit(general_bg, (0,0))
    
        if active: 
            color = color_active 
        else: 
            color = color_passive 
            
        # draw rectangle and argument passed which should 
        # be on screen 
        pg.draw.rect(screen, color, input_rect) 
        pg.draw.rect(screen, game_blue, submit_rect) 
        text_surface = font2.render(user_text, True, (0,0,0))
        if first_name:
            text_surface2 = INTRO_FONT.render("Player 2, what is your name please?", 1, game_blue)
        else:
            text_surface2 = INTRO_FONT.render("Player 1, what is your name please?", 1, game_blue) 

        # render at position stated in arguments 
        screen.blit(text_surface, (input_rect.x + 5, input_rect.centery-(text_surface.get_height()/2)))
        # render at position stated in arguments  
        screen.blit(text_surface2, ((width/2)-(text_surface2.get_width()/2), 250))
        screen.blit(submit_button, ((width/2)-(submit_button.get_width()/2), 350))
        if first_name:
            username2 = user_text
        else:
            username1 = user_text
            message = f'{username1}, select a column to place your piece'
        pg.display.flip()
        clock = pg.time.Clock()
        clock.tick(60)
        pg.time.delay(200)
IN_GAME_SOUND.play(loops=-1,fade_ms=2000)
start()


def game_window():
    global X_SCORE, O_SCORE, username1, username2, message, STREAK_COUNT, winner, win_direction, table1, table2, table3, table4, grand_table
    if winner:
        # To display the discs/pieces
        drawing_height = 545
        drawing_width = 260
        for x in grand_table:
            for i in x:
                if i == 'X':
                    screen.blit(red_piece, (drawing_width, drawing_height))
                elif i == 'O':
                    screen.blit(yellow_piece, (drawing_width, drawing_height))
                drawing_width += 160
            drawing_width = 260
            drawing_height -= 160
        
        WIN_SOUND.play()
        if winner == 'X':
            # to print the win line
            if win_direction[0] == 0:
                # if the win is horizontal/across the row 
                screen.blit(red_horizontal, (win_direction[1], win_direction[2]))

            if win_direction[0] == 1:
                # if the win is vertical/down the row 
                screen.blit(red_vertical, (win_direction[1], win_direction[2]))

            if win_direction[0] == 2:
                # if the win is diagonal from bottom left to top right
                screen.blit(red_diagonal, (win_direction[1], win_direction[2]))
            
            if win_direction[0] == 3:
                # if the win is diagonal from bottom left to top right
                screen.blit(red_diagonal_flip, (win_direction[1], win_direction[2]))

            win_text = SCORE_FONT.render(f'{username1} won this round', 1, 'red')
        elif winner == 'O':
            # to print the win line
            if win_direction[0] == 0:
                # if the win is horizontal/ across the row 
                screen.blit(yellow_horizontal, (win_direction[1], win_direction[2]))

            if win_direction[0] == 1:
                # if the win is vertical/down the row 
                screen.blit(yellow_vertical, (win_direction[1], win_direction[2]))

            if win_direction[0] == 2:
                # if the win is diagonal from bottom left to top right
                screen.blit(yellow_diagonal, (win_direction[1], win_direction[2]))

            if win_direction[0] == 3:
                # if the win is diagonal from bottom left to top right
                screen.blit(yellow_diagonal_flip, (win_direction[1], win_direction[2]))

            win_text = SCORE_FONT.render(f'{username2} won this round', 1, 'yellow')
        screen.blit(win_text, ((width/2)-(win_text.get_width()/2),(height/2)-(win_text.get_height()/2)))
        winner = None
        win_direction = None
        pg.display.update()
        time.sleep(1.5)
        table1 = ["","","","",""]
        table2 = ["","","","",""]
        table3 = ["","","","",""]
        table4 = ["","","","",""]
        grand_table = [table1,table2,table3,table4]

    screen.blit(general_bg, (0,0))

    username1_display = FONT1.render(username1, 1, 'white')
    username2_display = FONT1.render(username2, 1, 'white')

    score1 = SCORE_FONT.render(f'{X_SCORE}', 1, 'white')
    score2 = SCORE_FONT.render(f'{O_SCORE}', 1, 'white') 

    screen.blit(board, (200,20))
    screen.blit(red_score_board, (5,(height/2)-(red_score_board.get_height()/2)))
    screen.blit(yellow_score_board, (1150,(height/2)-(red_score_board.get_height()/2)))
    screen.blit(username1_display, (20, (height/2)-(red_score_board.get_height()/2)+5))
    screen.blit(username2_display, (1160,(height/2)-(yellow_score_board.get_height()/2)+5))
    screen.blit(score1, (45, (height/2)-(red_score_board.get_height()/2)+105))
    screen.blit(score2, (1190,(height/2)-(yellow_score_board.get_height()/2)+105))

    # For the streak control
    if STREAK_COUNT[1] > 1:
        streak_score = STREAK_FONT.render(f'{STREAK_COUNT[1]}', 1, 'white')
        if STREAK_COUNT[0] == 'X':
            screen.blit(streak, (40, (height/2)-(red_score_board.get_height()/2)+185))
            screen.blit(streak_score, (65, (height/2)-(red_score_board.get_height()/2)+180))
        if STREAK_COUNT[0] == 'O':
            screen.blit(streak, (1190, (height/2)-(yellow_score_board.get_height()/2)+185))
            screen.blit(streak_score, (1215, (height/2)-(yellow_score_board.get_height()/2)+180))

    # To display messages on-screen
    if message:
        message_text = MESSAGE_FONT.render(f'{message}', 1, 'white')
        screen.blit(message_text, ((width/2)-(message_text.get_width()/2), height-50))
    
    # To display the discs/pieces
    drawing_height = 545
    drawing_width = 260

    for x in grand_table:
        for i in x:
            if i == 'X':
                screen.blit(red_piece, (drawing_width, drawing_height))
            elif i == 'O':
                screen.blit(yellow_piece, (drawing_width, drawing_height))
            drawing_width += 160
        drawing_width = 260
        drawing_height -= 160


    pg.display.update()

game_window() 

def main_logic():
    global current, grand_table, table1, table2, table3, table4, message, STREAK_COUNT,X_SCORE,O_SCORE, winner, win_direction
    switch = True
    count = 0
    count_row = 0
    count_col = 0
    count_diag_left_right = 0
    count_diag_left_right2 = 0
    count_diag_right_left = 0
    count_diag_right_left2 = 0
    choice = None

    if current == 'X':
        x, y = pg.mouse.get_pos()
        # assign the choices based on mouse position
        if y > 20:
            if 240 < x < 390:
                choice = 1
            elif 410 < x < 550:
                choice = 2
            elif 570 < x < 720:
                choice = 3
            elif 740 < x < 880:
                choice = 4
            elif 900 < x < 1040:
                choice = 5
            if choice: 
                for index, list in enumerate(grand_table):
                    # CHECK VACANCY
                    if list[choice-1]:
                        count += 1  
                        if count >= 4:
                            switch = False
                            continue
                    else:
                        list[choice-1] = 'X'
                        CLICK_SOUND.play()
                        for x in range(0,5):
                            if list[x] == 'X':
                                count_row += 1
                            elif list[x] != 'X' and count_row < 4:
                                count_row = 0

                        # ROW
                        if count_row == 4:
                            # to figure out where to draw the win line
                            if list[0] == 'X':
                                width = 250
                            else:
                                width = 410
                            height = 600
                            for num in range(index):
                                height -= 160 
                            # win direction in the format (orientation:horizontal, starting point, level/row)
                            win_direction = [0, width, height]
                            X_SCORE += 1
                            winner = 'X'
                            if STREAK_COUNT[0] == 'X':
                                STREAK_COUNT[1] += 1
                            else:
                                STREAK_COUNT[0] = 'X'
                                STREAK_COUNT[1] = 1
                            break
                        else:
                            count_row = 0
                        break
                for x in range(0,5):
                    for index,i in enumerate(grand_table):
                        # FOR DIAGONAL LEFT TO RIGHT
                        # for the first level of diagonal wins from the bottom left
                        if i[index] == 'X':
                            count_diag_left_right += 1
                        elif i[index] != 'X' and count_diag_left_right < 4:
                            count_diag_left_right = 0
                        
                        # for the second level of diagonal wins from the bottom left
                        if i[index+1] == 'X':
                            count_diag_left_right2 += 1
                        elif i[index+1] != 'X' and count_diag_left_right2 < 4:
                            count_diag_left_right2 = 0

                    # check columns
                    for x in range(0,5):
                        for index,i in enumerate(grand_table):
                            if i[x] == 'X':
                                count_col += 1
                                col_win_index = x
                        if count_col < 4:
                            count_col = 0
                        else:
                            break
                    
                    for index,i in enumerate(reversed(grand_table)):
                        # FOR DIAGONAL RIGHT TO LEFT
                        # for the first level of diagonal wins from the bottom right
                        if i[index] == 'X':
                            count_diag_right_left += 1
                        elif i[index] != 'X' and count_diag_right_left < 4:
                            count_diag_right_left = 0
                        
                        # for the second level of diagonal wins from the bottom right
                        if i[index+1] == 'X':
                            count_diag_right_left2 += 1
                        elif i[index+1] != 'X' and count_diag_right_left2 < 4:
                            count_diag_right_left2 = 0

                    # LEFT TO RIGHT
                    if count_diag_left_right == 4 or count_diag_left_right2 == 4:
                        
                        if count_diag_left_right == 4:
                            width = 265
                            height = 50
                        
                        if count_diag_left_right2 == 4:
                            width = 420
                            height = 50

                        # win direction in the format (orientation:horizontal, starting point, level/row)
                        win_direction = [2, width, height]

                        X_SCORE += 1
                        current = 'O'
                        winner = 'X'
                        message = f"{username2}'s turn"

                        if STREAK_COUNT[0] == 'X':
                            STREAK_COUNT[1] += 1
                        else:
                            STREAK_COUNT[0] = 'X'
                            STREAK_COUNT[1] = 1
                        break
                    else:
                        count_diag_left_right = 0

                    # RIGHT TO LEFT
                    if count_diag_right_left == 4 or count_diag_right_left2 == 4:
                        
                        if count_diag_right_left == 4:
                            width = 265
                            height = 50
                        
                        if count_diag_right_left2 == 4:
                            width = 420
                            height = 50

                        # win direction in the format (orientation:horizontal, starting point, level/row)
                        win_direction = [3, width, height]

                        X_SCORE += 1
                        current = 'O'
                        winner = 'X'
                        message = f"{username2}'s turn"

                        if STREAK_COUNT[0] == 'X':
                            STREAK_COUNT[1] += 1
                        else:
                            STREAK_COUNT[0] = 'X'
                            STREAK_COUNT[1] = 1
                        break
                    else:
                        count_diag_right_left = 0

                    # COLUMN
                    if count_col == 4:
                        # to figure out where to draw the win line
                        width = 310
                        height = 50
                        for index in range(col_win_index):
                            width += 160
                        # win direction in the format (orientation:horizontal, starting point, level/row)
                        win_direction = [1, width, height]
                        X_SCORE += 1
                        current = 'O'
                        winner = 'X'
                        message = f"{username2}'s turn"

                        if STREAK_COUNT[0] == 'X':
                            STREAK_COUNT[1] += 1
                        else:
                            STREAK_COUNT[0] = 'X'
                            STREAK_COUNT[1] = 1
                        break
                    else:
                        count_col = 0
                    if switch:
                        current = 'O'
                        message = f"{username2}'s turn"
                    break
            else:
                message = f'Invalid column selection from {username1}. Try again'
    elif current == 'O':
        x, y = pg.mouse.get_pos()
        # assign the choices based on mouse position
        if y > 20:
            if 240 < x < 390:
                choice = 1
            elif 410 < x < 550:
                choice = 2
            elif 570 < x < 720:
                choice = 3
            elif 740 < x < 880:
                choice = 4
            elif 900 < x < 1040:
                choice = 5
            if choice:
                for index,list in enumerate(grand_table):
                    if list[choice-1]:
                        count += 1  
                        if count >= 4:
                            continue
                    else:
                        list[choice-1] = 'O'
                        CLICK_SOUND.play()
                        for x in range(0,5):
                            if list[x] == 'O':
                                count_row += 1
                            elif list[x] != 'O' and count_row < 4:
                                count_row = 0
                                
                        if count_row == 4:
                            # to figure out where to draw the win line
                            if list[0] == 'O':
                                width = 250
                            else:
                                width = 410
                            height = 600
                            for num in range(index):
                                height -= 160 
                            # win direction in the format (orientation:horizontal, starting point, level/row)
                            win_direction = [0, width, height]
                            O_SCORE += 1
                            
                            current = 'X'
                            winner = 'O'
                            message = f"{username1}'s turn"

                            if STREAK_COUNT[0] == 'O':
                                STREAK_COUNT[1] += 1
                            else:
                                STREAK_COUNT[0] = 'O'
                                STREAK_COUNT[1] = 1
                            break
                        else:
                            count_row = 0
                        break
                for x in range(0,5):
                    for index,i in enumerate(grand_table):
                        # FOR DIAGONAL LEFT TO RIGHT
                        # for the first level of diagonal wins from the bottom left
                        if i[index] == 'O':
                            count_diag_left_right += 1
                        elif i[index] != 'O' and count_diag_left_right < 4:
                            count_diag_left_right = 0
                        
                        # for the second level of diagonal wins from the bottom left
                        if i[index+1] == 'O':
                            count_diag_left_right2 += 1
                        elif i[index+1] != 'O' and count_diag_left_right2 < 4:
                            count_diag_left_right2 = 0

                    # check columns
                    for x in range(0,5):
                        for index,i in enumerate(grand_table):
                            if i[x] == 'O':
                                count_col += 1
                                col_win_index = x
                        if count_col < 4:
                            count_col = 0
                        else:
                            break

                    for index,i in enumerate(reversed(grand_table)):
                        # FOR DIAGONAL RIGHT TO LEFT
                        # for the first level of diagonal wins from the bottom right
                        if i[index] == 'O':
                            count_diag_right_left += 1
                        elif i[index] != 'O' and count_diag_right_left < 4:
                            count_diag_right_left = 0
                        
                        # for the second level of diagonal wins from the bottom right
                        if i[index+1] == 'O':
                            count_diag_right_left2 += 1
                        elif i[index+1] != 'O' and count_diag_right_left2 < 4:
                            count_diag_right_left2 = 0

                    # LEFT TO RIGHT
                    if count_diag_left_right == 4 or count_diag_left_right2 == 4:
                        
                        if count_diag_left_right == 4:
                            width = 265
                            height = 50
                        
                        if count_diag_left_right2 == 4:
                            width = 420
                            height = 50

                        # win direction in the format (orientation:horizontal, starting point, level/row)
                        win_direction = [2, width, height]

                        O_SCORE += 1
                        current = 'X'
                        winner = 'O'
                        message = f"{username1}'s turn"

                        if STREAK_COUNT[0] == 'O':
                            STREAK_COUNT[1] += 1
                        else:
                            STREAK_COUNT[0] = 'O'
                            STREAK_COUNT[1] = 1
                        break
                    else:
                        count_diag_left_right = 0
                        count_diag_left_right2 = 0

                    # RIGHT TO LEFT
                    if count_diag_right_left == 4 or count_diag_right_left2 == 4:

                        if count_diag_right_left == 4:
                            width = 265
                            height = 50
                        
                        if count_diag_right_left2 == 4:
                            width = 420
                            height = 50

                        # win direction in the format (orientation:horizontal, starting point, level/row)
                        win_direction = [3, width, height]

                        O_SCORE += 1
                        current = 'X'
                        winner = 'O'
                        message = f"{username1}'s turn"

                        if STREAK_COUNT[0] == 'O':
                            STREAK_COUNT[1] += 1
                        else:
                            STREAK_COUNT[0] = 'O'
                            STREAK_COUNT[1] = 1
                        break
                    else:
                        count_diag_right_left = 0
                        count_diag_right_left2 = 0

                    if count_col == 4:
                        # to figure out where to draw the win line
                        width = 310
                        height = 50
                        for index in range(col_win_index):
                            width += 160
                        # win direction in the format (orientation:horizontal, starting point, level/row)
                        win_direction = [1, width, height]

                        O_SCORE += 1
                        current = 'X'
                        winner = 'O'
                        message = f"{username1}'s turn"

                        if STREAK_COUNT[0] == 'O':
                            STREAK_COUNT[1] += 1
                        else:
                            STREAK_COUNT[0] = 'O'
                            STREAK_COUNT[1] = 1
                        break
                    else:
                        count_col = 0
                    if switch:
                        current = 'X'
                        message = f"{username1}'s turn"
                    break
            else:
                message = f'Invalid column selection from {username1}. Try again'

    # check if the spaces are filled
    for list in grand_table:
        for x in list:
            if x != '':
                available = False
            else:
                available = True
                break
    if available == False and winner == None:
        table1 = ["","","","",""]
        table2 = ["","","","",""]
        table3 = ["","","","",""]
        table4 = ["","","","",""]
        grand_table = [table1,table2,table3,table4]

# MAIN FUNCTION
def main():
    global username1,username2,X_SCORE,O_SCORE, current, STREAK_COUNT, winner, display
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            continue_game = None
            if event.type == pg.QUIT:
                # Display final scores before exiting
                display = False
                margin = X_SCORE - O_SCORE
                if margin > 0:
                    final_text = QUIT_FONT.render(f"{username1} is leading {username2} by {margin}", 1, 'red')
                    final_bg = win_bg
                elif margin < 0:
                    final_text = QUIT_FONT.render(f"{username2} is leading {username1} by {margin*-1}", 1, 'yellow')
                    final_bg = win_bg
                elif margin == 0:
                    final_text = QUIT_FONT.render("The game will end in a tie", 1, (0, 0, 0))
                    final_bg = draw_bg
                    
                screen.blit(final_bg,(0,0))
                screen.blit(final_text, ((width/2)-(final_text.get_width()/2), (height/2)-150))

                pg.draw.rect(screen, game_blue, quit_rect) 
                pg.draw.rect(screen, game_blue, back_rect) 
                screen.blit(quit_button, ((width/2)-(quit_button.get_width()/2), 300))
                screen.blit(back_button, (10, 10))

                pg.display.update()
                

            if event.type == pg.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos):
                    IN_GAME_SOUND.stop()
                    EXIT_SOUND.play()
                    pg.time.delay(2000)
                    run = False
                    pg.quit()
                    sys.exit()
                if back_rect.collidepoint(event.pos):
                   BACK_SOUND.play()
                   continue_game = True
                   display = True
                if display == True:
                    if not continue_game:
                        main_logic()
                    game_window()
                continue_game =  None
        pg.display.update()

        
if __name__ == "__main__":
    main()
