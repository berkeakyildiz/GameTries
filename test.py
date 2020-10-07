import pygame, random, time
from sirius import *
# Define some color

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 225)
lightblue = (153, 204, 255)
dodgerblue = (30, 144, 255)
deepskyblue = (0, 191, 255)
hotpink = (255, 105, 180)
deeppink = (255, 20, 147)
pink = (255, 192, 203)
yellow = (255, 255, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (899, 1599)  # 700,500
screen = pygame.display.set_mode(size)

pygame.display.set_caption("I love my sirius")
background = pygame.image.load("IMG-20180922-WA0001.jpg")
background2 = pygame.image.load("IMG-20180922-WA0001(1).jpg")

player1 = Player(background)
player2 = Player(background2)
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites2.add(player2)

def randomhearts():
    a1 = (red)
    a2 = (hotpink)
    a3 = (deeppink)
    a4 = (pink)
    rana = (red, hotpink, deeppink, pink)
    heartcol = random.choice(rana)
    time.sleep(.01)
    return (heartcol)


def randomtext():
    b1 = (blue)
    b2 = (lightblue)
    b3 = (dodgerblue)
    b4 = (deepskyblue)
    ranb = (blue, lightblue, deepskyblue, dodgerblue)
    textcol = random.choice(ranb)
    time.sleep(.5)
    return (textcol)


def msg():
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return (c)


done = False

clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)
a = "love"
wait = pygame.time.wait(800)
i = 0
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    i += 1
    if i == 1:
        all_sprites.draw(screen)
    elif i == 2:
        all_sprites2.draw(screen)
    else:
        all_sprites.draw(screen)
        i = 0
    #all_sprites.draw(screen)

    text = font.render(a, True, randomhearts())
    screen.blit(text, [150, 0])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [450, 0])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [110, 40])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [189, 40])
    text = font.render("lo", True, randomhearts())
    screen.blit(text, [270, 40])  ##
    text = font.render("lo", True, randomhearts())
    screen.blit(text, [365, 40])

    text = font.render(a, True, randomhearts())
    screen.blit(text, [400, 40])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [485, 40])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [60, 80])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [140, 80])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [220, 80])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [300, 80])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [380, 80])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [460, 80])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [540, 80])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [20, 120])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [100, 120])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [180, 120])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [260, 120])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [340, 120])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [420, 120])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [500, 120])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [580, 120])
    ##############
    text = font.render(a, True, randomhearts())
    screen.blit(text, [20, 160])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [100, 160])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [180, 160])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [260, 160])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [340, 160])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [420, 160])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [500, 160])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [580, 160])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [50, 200])
    text = font.render("    I love you Sirius", True, randomtext())  # going to make it
    # randomlly go through various shades of blue
    screen.blit(text, [140, 200])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [560, 200])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [90, 230])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [177, 230])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [260, 230])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [340, 230])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [422, 230])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [509, 230])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [140, 260])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [220, 260])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [300, 260])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [380, 260])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [460, 260])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [180, 290])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [260, 290])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [340, 290])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [412, 290])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [220, 320])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [300, 320])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [380, 320])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [260, 350])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [340, 350])
    text = font.render(a, True, randomhearts())
    screen.blit(text, [300, 380])
    text = font.render("lo", True, randomhearts())
    screen.blit(text, [320, 410])

    text = font.render("I love you", True, msg())
    screen.blit(text, [250, 500])

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

