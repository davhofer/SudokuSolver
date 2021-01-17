import pygame
import Solver

# initialise the pygame font
pygame.font.init()

# Total window
SCREEN_SIZE = 500
screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))

# Title and Icon
pygame.display.set_caption("Sudoku Solver")
# img = pygame.image.load('icon.png')
# pygame.display.set_icon(img)

Ggrid = Solver.g
grid = Ggrid.grid

x = 0
y = 0
dif = SCREEN_SIZE / 9
val = 0

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans",40)
font2 = pygame.font.SysFont("comicsans",20)


def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255,0,0), (x*dif-3, (y+i)*dif), (x * dif + dif + 3, (y+i)*dif),7)
        pygame.draw.line(screen, (255,0,0),((x+i)*dif, y*dif),((x+i)*dif,y*dif+dif),7)

# Function to draw required lines for making Sudoku grid
def draw():
    # Draw the lines
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                if (i,j) in Solver.g.defaults:
                        color = (170, 160, 190)
                else:
                    color = (120, 130, 200)
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, color, (i * dif, j * dif, dif + 1, dif + 1))

                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    # Draw lines horizontally and verticallyto form grid
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

# Fill value entered in cell
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))

# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))
def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))

# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop that keeps the window running
while run:

    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
        # Get the mouse postion to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                val = -1
            if event.key == pygame.K_SPACE:
                print("hello")
            #     flag2 = 1
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                Ggrid.restoreDefault()
                grid = Ggrid.grid

    if flag2 == 1:
        if solve(grid, 0, 0)== False:
            error = 1
        else:
            rs = 1
        flag2 = 0

    if (int(x),int(y)) not in Solver.g.defaults:
        if val == -1:
            draw_val(0)
            Ggrid.put(0,int(x),int(y))
        elif val != 0:

            # print(x)
            # print(y)
            if Ggrid.check(val, int(x), int(y)):
                draw_val(val)
                Ggrid.put(val,int(x),int(y))
                flag1 = 0
            else:
                Ggrid.put(0,int(x),int(y))
                raise_error2()
    val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()
    instruction()

    # Update window
    pygame.display.update()

# Quit pygame window
pygame.quit()
