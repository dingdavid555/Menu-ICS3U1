# David Ding
# ICS3U1
# May 3rd 2017
# This program displays information about viruses and computer crimes

# Imports
import pygame
import random

# ========================================= VARIABLE DECLARATIONS AND INITIAL SETUP
# Defining Constants
# MAXX is the maximum horizontal size of the window in pixels
# MAXY is the maximum vertical size of the window in pixels
MAXX = 800
MAXY = 600

# Pygame Initialization
pygame.init()       # Initialization
screen = pygame.display.set_mode((MAXX, MAXY))      # Setting maximum screen size
pygame.mouse.set_visible(0)     # Sets the mouse to be invisible, we will be using a custom cursor

# Defining Variables
# running is a boolean variable that handles if the game is running or not
# cats is an array of NyanCat Objects
# clicks is an array of clicker effect objects
# scene_selection is a variable to told which scene should be played
# myClock is the clock variable to enforce frame rate
# increment is an integer used to determine opacity of the text
# bg is used to handle the background on the computer
running = True
cats = []
clicks = []
bg = 0

# Pygame Initialization
scene_selection = 0
myClock = pygame.time.Clock()

# Image Loading
# NYAN_CAT is the picture of the cats that wil cross the screen
# CURSOR is the picture of the cursor that is pointing (non-clicked)
# CURSOR_CLICKED is the picture of the cursor that is pointing (after the user clicks something)
# BSOD is the blue screen of death that might appear on the computer in the menu
# CHROME is the chrome new tab page that might appear on the computer in the menu
# WALL_ONE is a wallpaper that might appear on the computer in the menu
# LOL is the league of legends launcher that might appear on the computer in the menu
NYAN_CAT = pygame.image.load("nyan_cat.png")
CURSOR = pygame.image.load("cursor.png")
CURSOR_CLICKED = pygame.image.load("cursor_clicked.png")
BSOD = pygame.image.load("BSOD.png")
SCREEN = pygame.image.load("win10.png")
CHROME = pygame.image.load("chrome.png")
WALL_ONE = pygame.image.load("wall1.png")
LOL = pygame.image.load("four.png")

# Defining constant colors and shapes
# UPPER_RECT is the upper selection rectangle in the screen selection
# LOWER_RECT is the lower selection rectangle in the screen selection
# QUIT is the rectangle for the quit box
# BACK_RECT is the rectangle to go back to the main screen
# TITLE_FONT is the font used for the title
# SMALL_FONT is the font used for the menus and the main bodies
RED = (117, 0, 0)               # Fairly Self Explanatory... Background for code red
BRIGHT_RED = (255, 0, 0)        # ...   Used for the power button on the computer
GREEN = (0, 117, 0)             # ...   Background for cryptolocker
WHITE = (255, 255, 255)         # ...   Used for text on screens
BLACK = (0, 0, 0)               # ...   Used to draw the computer
DARK_BLUE = (30, 72, 140)       # ...   Used as the background color on the main menu
LIGHT_BLUE = (66, 179, 255)     # ...   Used as the highlighted color on the menu
UPPER_RECT = pygame.Rect(MAXX // 2, 3 * MAXY // 8, MAXX // 3, MAXY // 8)
LOWER_RECT = pygame.Rect(MAXX // 2, 5 * MAXY // 8, MAXX // 3, MAXY // 8)
QUIT = pygame.Rect(MAXX // 2, 5 * MAXX // 8, MAXX // 3, MAXY // 15)
BACK_RECT = pygame.Rect(MAXX // 8, 7 * MAXY // 8, MAXX // 6, MAXY // 12)
LAPTOP_SCREEN_RECT = pygame.Rect(95, 295, 220, 120)
MONITOR_INSIDE = pygame.Rect(100, 300, 210, 110)
TITLE_FONT = pygame.font.SysFont("courier", 40)
SMALL_FONT = pygame.font.SysFont("courier", 20)


# ========================================= OBJECT CLASSES
# This class is for each cat, each time a click is made on any screen, a cat will appear and run through the screen
class NyanCat(object):
    def __init__(self, status, position, ycoor):
        self.status = status        # This is the status of the cat, whether or not it exists
        self.position = position    # This is the x-position of the cat, where along the x-values it is at
        self.ycoor = ycoor          # This is the y-position of the cat, it is randomly generated


# This class is for each click circle, each time a click happens, a circle will appear
class ClickCircle(object):
    def __init__(self, status, position, progress):
        self.status = status        # This sees if the click exists or not
        self.position = position    # This checks the position, duple variable type storing the x and y coordinates of
                                    # the click
        self.progress = progress    # This checks how much of the drawing it has completed


# ========================================= DEFINITIONS (METHODS)
# This function draws the boxes in the title menu. This method gets passed which number is selected
def draw_boxes(selected):
    # title_one is a local variable that stores the name of the first button
    # title_two is a local variable that stores the name of the second button
    # title_three is a local variable that stores the name of the third button
    # title_two_selected is a local variable that stores the name of the first button when there is a mouse-over
    # title_two_selected is a local variable that stores the name of the second button when there is a mouse-over
    # title_two_selected is a local variable that stores the name of the third button when there is a mouse-over
    title_one = SMALL_FONT.render("CryptoLocker", 1, WHITE)
    title_two = SMALL_FONT.render("Code Red", 1, WHITE)
    title_three = SMALL_FONT.render("Quit", 1, WHITE)
    title_one_selected = SMALL_FONT.render("CryptoLocker", 1, BLACK)
    title_two_selected = SMALL_FONT.render("Code Red", 1, BLACK)
    title_three_selected = SMALL_FONT.render("Quit", 1, BLACK)

    if selected == 1:       # If the first box is highlighted
        pygame.draw.rect(screen, LIGHT_BLUE, UPPER_RECT, 0)
        screen.blit(title_one_selected, [450, 250])
        pygame.draw.rect(screen, WHITE, LOWER_RECT, 1)
        screen.blit(title_two, [450, 400])
        pygame.draw.rect(screen, WHITE, QUIT, 1)
        screen.blit(title_three, [450, 510])
    elif selected == 2:     # If the second box is highlighted
        pygame.draw.rect(screen, WHITE, UPPER_RECT, 1)
        screen.blit(title_one, [450, 250])
        pygame.draw.rect(screen, LIGHT_BLUE, LOWER_RECT, 0)
        screen.blit(title_two_selected, [450, 400])
        pygame.draw.rect(screen, WHITE, QUIT, 1)
        screen.blit(title_three, [450, 510])
    elif selected == 3:     # If the third box is highlighted
        pygame.draw.rect(screen, WHITE, UPPER_RECT, 1)
        screen.blit(title_one, [450, 250])
        pygame.draw.rect(screen, WHITE, LOWER_RECT, 1)
        screen.blit(title_two, [450, 400])
        pygame.draw.rect(screen, LIGHT_BLUE, QUIT, 0)
        screen.blit(title_three_selected, [450, 510])
    elif selected == 0:     # If nothing is highlighted
        pygame.draw.rect(screen, WHITE, UPPER_RECT, 1)
        screen.blit(title_one, [450, 250])
        pygame.draw.rect(screen, WHITE, LOWER_RECT, 1)
        screen.blit(title_two, [450, 400])
        pygame.draw.rect(screen, WHITE, QUIT, 1)
        screen.blit(title_three, [450, 510])


# This method handles drawing the main scene, finds if the mouse collides with any of the boxes
def draw_scene(screen, mx, my, mb):
    # text is the title to be rendered out onto the screen
    text = TITLE_FONT.render("Computer Science Information", 1, WHITE)
    screen.blit(text, pygame.Rect(MAXX // 12, MAXY // 8, MAXX // 3, MAXY // 8))
    if mb == 0:     # This if statement checks if the mouse is not clicked, only highlighted over a box
        if UPPER_RECT.collidepoint(mx, my):     # If the mouse collides with the first box
            draw_boxes(1)
            mouse_handler(mx, my, mb)
            return 0
        elif LOWER_RECT.collidepoint(mx, my):   # If the mouse collides with the second box
            draw_boxes(2)
            mouse_handler(mx, my, mb)
            return 0
        elif QUIT.collidepoint(mx, my):         # If the mouse collides with the quit box
            draw_boxes(3)
            mouse_handler(mx, my, mb)
            return 0
        else:                                   # If the mouse does not collide with anything
            draw_boxes(0)
            mouse_handler(mx, my, mb)
            return 0
    else:           # If the mouse is clicked
        if UPPER_RECT.collidepoint(mx, my):     # If the mouse is clicked on the first box
            draw_boxes(1)
            mouse_handler(mx, my, mb)
            return 1
        elif LOWER_RECT.collidepoint(mx, my):   # If the mouse is on the second box
            draw_boxes(2)
            mouse_handler(mx, my, mb)
            return 2
        elif QUIT.collidepoint(mx, my):         # If the mouse is on the quit box
            mouse_handler(mx, my, mb)
            return 3
        else:                                   # If the mouse is just clicked but not on any given box
            draw_boxes(0)
            mouse_handler(mx, my, mb)
            return 0


# This method is what handles the body text. It gives a new line to when the boundaries have been exceeded
def blit_body(surface, pos, text, font):
    words = [word.split(' ') for word in text.splitlines()]     # words is a list that separates every word in a string
                                                                # that is separated by a space
    space_width = font.size(' ')[0]     # This is used to check if the word will go outside of the boundaries, it is
                                        # just enough space for a blank space character to be rendered out
    x, y = pos      # the position of the word starting is set to x and y to begin with
    for word in words:      # loops through the number of lines in words
        for i in word:      # loops through the number of words in each line
            # wrectangle creates a rectangle that fits the word using the font render
            # wwidth stores the width of the rectangle word
            # wheight stores the height of the rectangle word
            wrectangle = font.render(str(i), 0, (increment, increment, increment))
            wwidth, wheight = wrectangle.get_size()
            if x + wwidth >= MAXY + 100:    # Sees if the position would be passed by the maximum boundary
                x = pos[0]      # if it does, the restart the x-value to start again from the beginning
                y += wheight    # increases the y coordinates by the space of the text, the same as new line
            surface.blit(wrectangle, (x, y))    # displays the text
            x += wwidth + space_width   # Creates a space
    x = pos[0]  # Resets the dimensions for multiple lines in words
    y += wheight    # Generates a new blank line


# This method is used to handle the crypto_locker screen, it takes the mouse properties in order to check
# if the go back button has been triggered
def crypto_locker(mx, my, mb):
    screen.fill(GREEN)
    # title is the title of the screen
    # text is what will show up in the body of the screen, it is blit out and handled by the method above, blit_body
    title = TITLE_FONT.render("Cryptolocker", 1, WHITE)
    screen.blit(title, pygame.Rect(MAXX // 3, MAXY // 8, MAXX // 3, MAXY // 3))
    text = "Cryptolocker was an incredibly notorious Trojan Horse style program."\
           "Its notoriety came from the fact that it encrypted files on the hard drive, then proceeded to ask the "\
           "ask the owner of the machine to pay a random for their files to be decrypted. The general amount was to "\
           "be $400 in prepaid cash or in BitCoin, a virtual currency. The man who developed it, Evgeniy Bogachev was "\
           "charged. The encryption keys were released to the affected computers. He would have made a whopping "\
           "$3 Million dollars from this operation. "
    blit_body(screen, (MAXX // 6, MAXX // 5), text, SMALL_FONT)

    # Checks if buttons have been clicked, same methods as draw_boxes and draw_scene but on a smaller, one button scale
    if mb != 1:
        if BACK_RECT.collidepoint(mx, my):
            pygame.draw.rect(screen, WHITE, BACK_RECT, 0)
            back = SMALL_FONT.render("Go Back", 1, BLACK)
            screen.blit(back, BACK_RECT)
            mouse_handler(mx, my, mb)
            return 1
        else:
            back = SMALL_FONT.render("Go Back", 1, WHITE)
            screen.blit(back, BACK_RECT)
            pygame.draw.rect(screen, WHITE, BACK_RECT, 1)
            mouse_handler(mx, my, mb)
            return 1
    else:
        if BACK_RECT.collidepoint(mx, my):
            back = SMALL_FONT.render("Go Back", 1, BLACK)
            screen.blit(back, BACK_RECT)
            pygame.draw.rect(screen, WHITE, BACK_RECT, 0)
            mouse_handler(mx, my, mb)
            return 0
        else:
            back = SMALL_FONT.render("Go Back", 1, WHITE)
            screen.blit(back, BACK_RECT)
            pygame.draw.rect(screen, WHITE, BACK_RECT, 1)
            mouse_handler(mx, my, mb)
            return 1


# Handles the screen for Code Red, same as the Cryptolocker above
def code_red(mx, my, mb):
    screen.fill(RED)
    # title shows Code Red at the top of the screen
    # text is the text that will be displayed in the body of the text
    title = TITLE_FONT.render("Code Red", 1, WHITE)
    screen.blit(title, pygame.Rect(MAXX // 3, MAXY // 8, MAXX // 3, MAXY // 3))
    text = "Code Red was first seen in 2001 and was quite comically named so because they were drinking Mountain " \
           "Dew Code Red at the time of discovery. This worm linked computers to a botnet system. " \
           "A Botnet is a number of Internet-connected devices that then perform various tasks. " \
           "In this case, the Botnet was used to perform a series of DDOS (Direct Denial of Service Attacks), " \
           "on several websites. Additionally, it leaves behind a message \" Hacked by Chinese!\" on every affected " \
           "website. "
    blit_body(screen, (MAXX // 6, MAXX // 5), text, SMALL_FONT)

    # Checks if buttons have been clicked, same methods as draw_boxes and draw_scene but on a smaller, one button scale
    if mb != 1:
        if BACK_RECT.collidepoint(mx, my):
            pygame.draw.rect(screen, WHITE, BACK_RECT, 0)
            back = SMALL_FONT.render("Go Back", 1, BLACK)
            screen.blit(back, BACK_RECT)
            mouse_handler(mx, my, mb)
            return 2
        else:
            back = SMALL_FONT.render("Go Back", 1, WHITE)
            screen.blit(back, BACK_RECT)
            pygame.draw.rect(screen, WHITE, BACK_RECT, 1)
            mouse_handler(mx, my, mb)
            return 2
    else:
        if BACK_RECT.collidepoint(mx, my):
            back = SMALL_FONT.render("Go Back", 1, BLACK)
            screen.blit(back, BACK_RECT)
            pygame.draw.rect(screen, WHITE, BACK_RECT, 0)
            mouse_handler(mx, my, mb)
            return 0
        else:
            back = SMALL_FONT.render("Go Back", 1, WHITE)
            screen.blit(back, BACK_RECT)
            pygame.draw.rect(screen, WHITE, BACK_RECT, 1)
            mouse_handler(mx, my, mb)
            return 2


# This function makes the custom cursor that is used in the program
def mouse_handler(mx, my, mb):
    if mb == 0:     # Checks if the mouse has been clicked
        screen.blit(CURSOR, pygame.Rect(mx, my, 100, 100))      # Image of the cursor, non-clicked
    elif mb == 1:
        screen.blit(CURSOR_CLICKED, pygame.Rect(mx, my, 100, 100))      # Image of the cursor that was clicked


# This function gets the position of the mouse
def get_mouse():
    mx, my = pygame.mouse.get_pos()     # mx, my are variables to store the x and y coordinates of the mouse
    mb = pygame.mouse.get_pressed()[0]  # mb stores if the first mouse button has been clicked or not
    return mx, my, mb


# Toggle Switch for the BSOD screen, just a simple toggle method
def toggle(var):
    if var:     # If initially true, return false
        return False
    else:       # If initially false, return true
        return True


# Draws a computer in the main menu screen
def draw_computer(mx, my, mb, selection):
    # Draws monitor
    pygame.draw.rect(screen, BLACK, LAPTOP_SCREEN_RECT)
    pygame.draw.line(screen, BLACK, (200, 355), (200, 420), 5)
    pygame.draw.line(screen, BLACK, (200, 420), (160, 425), 5)
    pygame.draw.line(screen, BLACK, (200, 420), (240, 425), 5)

    # Draws desktop part of computer
    pygame.draw.rect(screen, BLACK, pygame.Rect(40, 350, 40, 80))
    pygame.draw.circle(screen, BRIGHT_RED, (70, 360), 5, 1)
    pygame.draw.line(screen, BRIGHT_RED, (70, 360), (70, 355), 1)

    if mb == 0:     # If the mouse was not being pressed
        if LAPTOP_SCREEN_RECT.collidepoint(mx, my):     # If the mouse is on the computer screen
            screen.blit(SCREEN, LAPTOP_SCREEN_RECT)     # If the mouse is hovered, and there is nothing "running"
            return selection                            # then display the windows logo
        else:
            return selection
    if mb == 1:
        if LAPTOP_SCREEN_RECT.collidepoint(mx, my):     # If the mouse is clicked on the computer screen
            screen.blit(SCREEN, LAPTOP_SCREEN_RECT)
            return random.randint(1, 4)                 # Return a random number between 1 and 4 for the 4 possible
        else:                                           # screens
            return selection


# ========================================= MAIN GAME LOOP
# This is the main game loop
while running:
    screen.fill(DARK_BLUE)      # Refreshes the screen every frame

    # Quit handling by pygame exit button
    for evnt in pygame.event.get():     # Every time an event is triggered, check if it is a quit event
        if evnt.type == pygame.QUIT:    # if the user wants to quit, then quit the game
            running = False

    # Keyboard Controls
    keys = pygame.key.get_pressed()     # Gets the keys that are currently pressed
    if keys[pygame.K_ESCAPE]:   # If the user presses ESC, then return to the title screen
        scene_selection = 0

    # Mouse Controls
    mx, my, mb = get_mouse()
    # Not sure if I'm going to keep the cats in or not yet, it's kind of obnoxious
    if keys[pygame.K_n] == 1:
        cats.append(NyanCat(True, -400, random.randint(0, 550)))

    for i in cats:      # For every cat in the list cats
        screen.blit(NYAN_CAT, (i.position, i.ycoor, 100, 100))  # Draws the cats
        i.position += 15    # Changes the cat's position by 15 pixels every time (may be changed to a random speed)
        if i.position > 1200:   # If the cat is outside of the screen, no use it in staying there
            cats.remove(i)      # REMOVE CAT BECAUSE ITS USELESS NOW"""

    # Scene selection starting, which screen to display to user
    if scene_selection == 0:    # 0 refers to the title screen
        increment = 0   # Progress for fading in the text is reset when the user returns to the menu

        # user inputs on the screen
        if mb == 1:     # If there is a click on the main screen, display a circle that moves outwards
            clicks.append(ClickCircle(True, (mx, my), 5))   # Creates a new click object

        # Drawing circles every click
        for click in clicks:    # Cycles through clicks
            pygame.draw.circle(screen, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)),
                               click.position, click.progress, 1)   # Draws clicks
            click.progress += 2     # Timer for clicks
            if click.progress > 100:     # if the circle gets too big, remove the circle
                clicks.remove(click)

        # Drawing onto the screen
        scene_selection = draw_scene(screen, mx, my, mb)    # Draws the screen, and return value if anything is clicked
        bg = draw_computer(mx, my, mb, bg)                  # Draws the computer, handles changes on the screen

        if bg == 1:
            screen.blit(BSOD, MONITOR_INSIDE)
        elif bg == 2:
            screen.blit(CHROME, MONITOR_INSIDE)
        elif bg == 3:
            screen.blit(WALL_ONE, MONITOR_INSIDE)
        elif bg == 4:
            screen.blit(LOL, MONITOR_INSIDE)

    elif scene_selection == 1:  # Cryptolocker scene
        increment += 2          # Handler to fade in the text
        if increment > 255:     # Can't have the text be over full brightness!
            increment -= 2
        scene_selection = crypto_locker(mx, my, mb)     # Sees if the user wants to go to another scene
                                                        # and displays crypto_locker
    elif scene_selection == 2:  # Code Red
        scene_selection = code_red(mx, my, mb)      # Sees if the user wants to go to another screen and
                                                    # displays code_red
        increment += 2  # increments the brightness for the text fade in effect
        if increment > 255:     # Can't have the text be over full brightness!
            increment -= 2
    elif scene_selection == 3:  # If the user presses the quit button, then set running to False
        running = False
    mouse_handler(mx, my, mb)
    myClock.tick(60)    # myClock modifies frame rate (30 fps)
    pygame.display.flip()   # Updates all drawing
