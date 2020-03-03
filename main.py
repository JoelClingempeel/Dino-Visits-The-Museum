from sidescroller_engine import *

pygame.init()
win = pygame.display.set_mode((800, 500))
clockSpeed = 27
pygame.display.set_caption("Dino Visits the Museum")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 24)

# Load images, and make white backgrounds transparent.
BadGuyLeft = [pygame.image.load('GameImages/BadGuyL1.bmp'), pygame.image.load('GameImages/BadGuyL2.bmp'),
              pygame.image.load('GameImages/BadGuyL3.bmp'), pygame.image.load('GameImages/BadGuyL4.bmp'),
              pygame.image.load('GameImages/BadGuyL5.bmp'), pygame.image.load('GameImages/BadGuyL6.bmp'),
              pygame.image.load('GameImages/BadGuyL7.bmp')]
BadGuyRight = [pygame.image.load('GameImages/BadGuyR1.bmp'), pygame.image.load('GameImages/BadGuyR2.bmp'),
               pygame.image.load('GameImages/BadGuyR3.bmp'), pygame.image.load('GameImages/BadGuyR4.bmp'),
               pygame.image.load('GameImages/BadGuyR5.bmp'), pygame.image.load('GameImages/BadGuyR6.bmp'),
               pygame.image.load('GameImages/BadGuyR7.bmp')]
AltBadGuyLeft = [pygame.image.load('GameImages/AltBadGuyL1.bmp'), pygame.image.load('GameImages/AltBadGuyL2.bmp'),
                 pygame.image.load('GameImages/AltBadGuyL3.bmp'), pygame.image.load('GameImages/AltBadGuyL4.bmp'),
                 pygame.image.load('GameImages/AltBadGuyL5.bmp'), pygame.image.load('GameImages/AltBadGuyL6.bmp'),
                 pygame.image.load('GameImages/AltBadGuyL7.bmp')]
AltBadGuyRight = [pygame.image.load('GameImages/AltBadGuyR1.bmp'), pygame.image.load('GameImages/AltBadGuyR2.bmp'),
                  pygame.image.load('GameImages/AltBadGuyR3.bmp'), pygame.image.load('GameImages/AltBadGuyR4.bmp'),
                  pygame.image.load('GameImages/AltBadGuyR5.bmp'), pygame.image.load('GameImages/AltBadGuyR6.bmp'),
                  pygame.image.load('GameImages/AltBadGuyR7.bmp')]
DinoLeft = [pygame.image.load('GameImages/DinoL1.png'), pygame.image.load('GameImages/DinoL2.png'),
            pygame.image.load('GameImages/DinoL3.png'), pygame.image.load('GameImages/DinoL4.png'),
            pygame.image.load('GameImages/DinoL5.png'), pygame.image.load('GameImages/DinoL6.png'),
            pygame.image.load('GameImages/DinoL7.png')]
DinoRight = [pygame.image.load('GameImages/DinoR1.png'), pygame.image.load('GameImages/DinoR2.png'),
             pygame.image.load('GameImages/DinoR3.png'), pygame.image.load('GameImages/DinoR4.png'),
             pygame.image.load('GameImages/DinoR5.png'), pygame.image.load('GameImages/DinoR6.png'),
             pygame.image.load('GameImages/DinoR7.png')]
for i in range(7):
    DinoLeft[i].set_colorkey(WHITE)
    DinoRight[i].set_colorkey(WHITE)
    BadGuyLeft[i].set_colorkey(WHITE)
    BadGuyRight[i].set_colorkey(WHITE)
    AltBadGuyLeft[i].set_colorkey(WHITE)
    AltBadGuyRight[i].set_colorkey(WHITE)
crouchingDinoL = pygame.image.load('GameImages/CrouchingDinoL.bmp')
crouchingDinoL.set_colorkey(WHITE)
crouchingDinoR = pygame.image.load('GameImages/CrouchingDinoR.bmp')
crouchingDinoR.set_colorkey(WHITE)
crouchingDino = [crouchingDinoL, crouchingDinoR]
jellyfish = [pygame.image.load('GameImages/Jellyfish1.bmp'), pygame.image.load('GameImages/Jellyfish2.bmp'),
             pygame.image.load('GameImages/Jellyfish3.bmp'), pygame.image.load('GameImages/Jellyfish4.bmp'),
             pygame.image.load('GameImages/Jellyfish5.bmp')]
for j in range(5):
    jellyfish[j].set_colorkey(WHITE)
dino = Hero(win, DinoLeft, DinoRight, 8, crouchingDino, 3)
splashScreen = pygame.image.load('GameImages/DinoSplashScreen.png')
steelBar = pygame.image.load('GameImages/SteelBar.png')
brickWall = pygame.image.load('GameImages/BrickWall.bmp')
woodPlank = pygame.image.load('GameImages/woodPlank.png')
crackedStone = pygame.image.load('GameImages/crackedStone.png')
background1 = pygame.image.load('GameImages/DinoGameLevel1.png')
background2 = pygame.image.load('GameImages/DinoGameLevel2.png')
background3 = pygame.image.load('GameImages/DinoGameLevel3.png')
dinoFriend = pygame.image.load('GameImages/DinoFriend.bmp')
dinoFriend.set_colorkey(WHITE)
dinoEnding = pygame.image.load('GameImages/DinoEnding.png')

# Level 1 Data
platform1 = Platform(steelBar, 80, 460)
platform2 = Platform(steelBar, 130, 400)
platform3 = Platform(steelBar, 300, 350)
platform4 = Platform(steelBar, 850, 400)
platform5 = Platform(steelBar, 1500, 460)
platform6 = Platform(steelBar, 1750, 360)
platform7 = Platform(steelBar, 2000, 260)
platform8 = Platform(steelBar, 2250, 160)
platform9 = Platform(brickWall, 2500, 100)
platform10 = Platform(steelBar, 3300, 400)
platform11 = Platform(steelBar, 3600, 270)
platform12 = Platform(steelBar, 3900, 140)
platform13 = Platform(brickWall, 4200, 100)
platform14 = Platform(background2, 4900, 0)
platformList1 = [platform1, platform2, platform3, platform4, platform5, platform6, platform7, platform8, platform9,
                 platform10, platform11, platform12, platform13, platform14]

enemy1 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 320, 255, 4)
enemy2 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 870, 305, 4)
enemy3 = Enemy(win, BadGuyLeft,BadGuyRight, 40, 1300, 400, 4)
enemy4 = Enemy(win, BadGuyLeft,BadGuyRight, 40, 1800, 260, 4)
enemy5 = Enemy(win, BadGuyLeft,BadGuyRight, 40, 2300, 60, 4)
enemy6 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 2800, 400, 4)
enemy7 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 3100, 400, 4)
enemy8 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 3600, 175, 4)
enemy9 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 4200, 5, 4)
enemyList1 = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9]

level1 = Level(win, background1, dino, 4700, platformList1, enemyList1)

# Level 2 Data
altPlatform1 = Platform(steelBar, 200, 400)
altPlatform2 = Platform(steelBar, 400, 250)
altPlatform3 = Platform(brickWall, 650, 100)
altPlatform4 = Platform(steelBar, 1400, 440)
altPlatform5 = Platform(brickWall, 1600, 300)
altPlatform6 = Platform(steelBar, 1300, 180)
altPlatform7 = Platform(steelBar, 1620, 145)
altPlatform8 = Platform(brickWall, 1880, 90)
altPlatform9 = Platform(brickWall, 3100, 400)
altPlatform10 = Platform(brickWall, 3380, 260)
altPlatform11 = Platform(brickWall, 3660, 120)
altPlatform12 = Platform(brickWall, 3840, 120)
altPlatform13 = Platform(background3, 4120, 0)
platformList2 = [altPlatform1, altPlatform2, altPlatform3, altPlatform4, altPlatform5, altPlatform6, altPlatform7,
                 altPlatform8, altPlatform9, altPlatform10, altPlatform11, altPlatform12, altPlatform13]

altEnemy1 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 400, 153, 7)
altEnemy2 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 480, 400, 7)
altEnemy3 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 950, 400, 4)
altEnemy4 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 1400, 350, 4)
altEnemy5 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 1600, 205, 4)
altEnemy6 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 1335, 85, 4)
altEnemy7 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 1880, -7, 4)
altEnemy8 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 2300, 400, 4)
altEnemy9 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 2600, 400, 4)
altEnemy10 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 2900, 400, 4)
altEnemy11 = Enemy(win, jellyfish, jellyfish, 40, 3700, 20, 15)
enemyList2 = [altEnemy1, altEnemy2, altEnemy3, altEnemy4, altEnemy5, altEnemy6, altEnemy7, altEnemy8, altEnemy9,
              altEnemy10, altEnemy11]

level2 = Level(win, background2, dino, 4000, platformList2, enemyList2)

# Level 3 Data
museumPlatform1 = Platform(crackedStone, 100, 400)
museumPlatform2 = Platform(crackedStone, 600, 400)
museumPlatform3 = Platform(steelBar, 850, 250)
museumPlatform4 = Platform(brickWall, 1100, 100)
museumPlatform5 = Platform(woodPlank, 1380, 150)
museumPlatform6 = Platform(woodPlank, 1880, 250)
museumPlatform7 = Platform(woodPlank, 2380, 300)
museumPlatform8 = Platform(woodPlank, 2880, 350)
friend = Platform(dinoFriend, 3700, 320)
platformList3 = [museumPlatform1, museumPlatform2, museumPlatform3, museumPlatform4, museumPlatform5, museumPlatform6,
                 museumPlatform7, museumPlatform8, friend]

jelly1 = Enemy(win, jellyfish, jellyfish, 40, 200, 300, 15)
jelly2 = Enemy(win, jellyfish, jellyfish, 40, 500, 300, 15)
museumVillain1 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 850, 155, 7)
jelly3 = Enemy(win, jellyfish, jellyfish, 40, 1100, 0, 15)
museumVillain2 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 1550, 55, 4)
museumVillain3 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 1900, 155, 7)
museumVillain4 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 2125, 155, 7)
jelly4 = Enemy(win, jellyfish, jellyfish, 40, 2510, 205, 15)
museumVillain5 = Enemy(win, BadGuyLeft, BadGuyRight, 40, 2420, 205, 4)
jelly5 = Enemy(win, jellyfish, jellyfish, 40, 3060, 245, 15)
museumVillain6 = Enemy(win, AltBadGuyLeft, AltBadGuyRight, 40, 2970, 255, 7)
enemyList3 = [jelly1, jelly2, museumVillain1, jelly3, museumVillain2, museumVillain3, museumVillain4, jelly4,
              museumVillain5, jelly5, museumVillain6]

level3 = Level(win, background3, dino, 3500, platformList3, enemyList3)


def splash():
    global run
    while run:
        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                run = False
        win.blit(splashScreen, (0, 0))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            return 0
        pygame.display.flip()


def game_end():
    global run
    while run:
        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                run = False
        win.blit(dinoEnding, (0, 0))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            return 0
        pygame.display.flip()


game_levels = [level1, level2, level3]
level = 0
run = True
splash()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    current_level = game_levels[level]
    current_level.iterate()
    if current_level.status() == -1:
        current_level.restart()
    if current_level.status() == 1:
        current_level.restart()
        if level < len(game_levels) - 1:
            level += 1
        else:
            game_end()
            pygame.time.delay(1000)
            splash()
            level = 0
    clock.tick(clockSpeed)

pygame.quit()
