import pygame
import math
import random
from pygame import mixer
pygame.init()


# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space.png')

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerXmove = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXmove = []
enemyYmove = []
enemyNum = 6

for i in range(enemyNum):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyXmove.append(2)
    enemyYmove.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletXmove = 0
bulletYmove = 10
bullet_state = "ready"

# Score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over
overFont = pygame.font.Font('freesansbold.ttf', 64)


def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameOvertext():
    overText = overFont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overText, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # bullet appears at the center top of the bullet
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # Background image
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement mechanics
        # Keyboard input controls: Check left and right movement of player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXmove = -5
            if event.key == pygame.K_RIGHT:
                playerXmove = 5

            # Player shooting
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX   # So that bullet doesn't follow the spaceship
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # releases that press
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXmove = 0

    # Boundaries for player
    playerX += playerXmove
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(enemyNum):
        # Game over: Enemies closes in on player
        if enemyY[i] > 440:
            for j in range(enemyNum):
                enemyY[j] = 2000
            gameOvertext()
            break

        # Boundaries for enemy
        # Enemy goes to line below
        enemyX[i] += enemyXmove[i]
        if enemyX[i] <= 0:
            enemyXmove[i] = 2
            enemyY[i] += enemyYmove[i]

        elif enemyX[i] >= 736:
            enemyXmove[i] = -2
            enemyY[i] += enemyYmove[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            scoreValue += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYmove

    player(playerX, playerY)
    showScore(textX, textY)

    pygame.display.update()


# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space.png')

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerXmove = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXmove = []
enemyYmove = []
enemyNum = 6

for i in range(enemyNum):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyXmove.append(2)
    enemyYmove.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletXmove = 0
bulletYmove = 10
bullet_state = "ready"

# Score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over
overFont = pygame.font.Font('freesansbold.ttf', 64)


def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameOvertext():
    overText = overFont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overText, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # bullet appears at the center top of the bullet
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # Background image
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement mechanics
        # Keyboard input controls: Check left and right movement of player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXmove = -5
            if event.key == pygame.K_RIGHT:
                playerXmove = 5

            # Player shooting
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX   # So that bullet doesn't follow the spaceship
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # releases that press
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXmove = 0

    # Boundaries for player
    playerX += playerXmove
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(enemyNum):
        # Game over: Enemies closes in on player
        if enemyY[i] > 440:
            for j in range(enemyNum):
                enemyY[j] = 2000
            gameOvertext()
            break

        # Boundaries for enemy
        # Enemy goes to line below
        enemyX[i] += enemyXmove[i]
        if enemyX[i] <= 0:
            enemyXmove[i] = 2
            enemyY[i] += enemyYmove[i]

        elif enemyX[i] >= 736:
            enemyXmove[i] = -2
            enemyY[i] += enemyYmove[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            scoreValue += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYmove

    player(playerX, playerY)
    showScore(textX, textY)

    pygame.display.update()


# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space.png')

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerXmove = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXmove = []
enemyYmove = []
enemyNum = 6

for i in range(enemyNum):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyXmove.append(2)
    enemyYmove.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletXmove = 0
bulletYmove = 10
bullet_state = "ready"

# Score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over
overFont = pygame.font.Font('freesansbold.ttf', 64)


def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameOvertext():
    overText = overFont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overText, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # bullet appears at the center top of the bullet
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # Background image
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement mechanics
        # Keyboard input controls: Check left and right movement of player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXmove = -5
            if event.key == pygame.K_RIGHT:
                playerXmove = 5

            # Player shooting
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX   # So that bullet doesn't follow the spaceship
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # releases that press
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXmove = 0

    # Boundaries for player
    playerX += playerXmove
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(enemyNum):
        # Game over: Enemies closes in on player
        if enemyY[i] > 440:
            for j in range(enemyNum):
                enemyY[j] = 2000
            gameOvertext()
            break

        # Boundaries for enemy
        # Enemy goes to line below
        enemyX[i] += enemyXmove[i]
        if enemyX[i] <= 0:
            enemyXmove[i] = 2
            enemyY[i] += enemyYmove[i]

        elif enemyX[i] >= 736:
            enemyXmove[i] = -2
            enemyY[i] += enemyYmove[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            scoreValue += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYmove

    player(playerX, playerY)
    showScore(textX, textY)

    pygame.display.update()


# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space.png')

# Background music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title & Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerXmove = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXmove = []
enemyYmove = []
enemyNum = 6

for i in range(enemyNum):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyXmove.append(2)
    enemyYmove.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletXmove = 0
bulletYmove = 10
bullet_state = "ready"

# Score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over
overFont = pygame.font.Font('freesansbold.ttf', 64)


def showScore(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameOvertext():
    overText = overFont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overText, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fireBullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # bullet appears at the center top of the bullet
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    # Background image
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Quit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement mechanics
        # Keyboard input controls: Check left and right movement of player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXmove = -5
            if event.key == pygame.K_RIGHT:
                playerXmove = 5

            # Player shooting
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX   # So that bullet doesn't follow the spaceship
                    fireBullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # releases that press
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXmove = 0

    # Boundaries for player
    playerX += playerXmove
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(enemyNum):
        # Game over: Enemies closes in on player
        if enemyY[i] > 440:
            for j in range(enemyNum):
                enemyY[j] = 2000
            gameOvertext()
            break

        # Boundaries for enemy
        # Enemy goes to line below
        enemyX[i] += enemyXmove[i]
        if enemyX[i] <= 0:
            enemyXmove[i] = 2
            enemyY[i] += enemyYmove[i]

        elif enemyX[i] >= 736:
            enemyXmove[i] = -2
            enemyY[i] += enemyYmove[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            scoreValue += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletYmove

    player(playerX, playerY)
    showScore(textX, textY)

    pygame.display.update()
