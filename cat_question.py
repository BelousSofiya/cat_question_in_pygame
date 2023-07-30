# Rules:
# You have to guess this number
# You have 10 attempts
# The cat will help you (you'll see his clue in the left corner)
# Print your number (you'll see it in the right corner)
# and use space-button to show it the cat
# Use w-button to see cat's rules
# Use backspace-button to correct your number
# Use TAB-button to restart the game.


import pygame
from random import randint, choice
pygame.init()

FPS = 60
clock = pygame.time.Clock()

W = 800
H = 600
speed = 5
cat_x = W//2
cat_y = H//2
alice_x =0
alice_y = H - 50
cat_number = randint(0, 100)
text = "Tell me a secret number, Alice"
rules = [
"Dear Alice,",
"this awful cat likes to play game. Rules are next:",
"The cat has a secret number in range 0-100",
"You have to guess this number",
"You have 10 attempts",
"The cat will help you (you'll see his clue in the left corner)",
"Print your number (you'll see it in the right corner)",
"and use space-button to show it the cat",
"Use w-button to see cat's rules",
"Use backspace-button to correct your number",
"Use TAB-button to restart the game.",
"Be careful, I saw human bones under his tree!"
]

AQUA = (0, 255, 255)
TEAL = (0, 128, 128)
RED = (150, 0, 20)
FONT = pygame.font.SysFont('inkfree', 20)
rules_font = pygame.font.SysFont('segoescript', 19)
counter = 0

sc = pygame.display.set_mode((W, H))

pygame.display.set_caption('Guess the number, Alice')
pygame.display.set_icon(pygame.image.load("images/smiling_cat.png"))

cat_surf = pygame.image.load("images/cat_wonderland.png")
cat_rect = cat_surf.get_rect(center=(cat_x, cat_y))

rules_surf = pygame.image.load("images/perg_peaces.png")
rules_rect = rules_surf.get_rect(center=((cat_x+200), (cat_y+150)))
rules_surf = pygame.transform.scale(rules_surf, (rules_surf.get_width()//1.5, rules_surf.get_height()//1.5))

blood_surf = pygame.image.load("images/red_drop.png")
blood_rect = blood_surf.get_rect(topleft=(400, 0))
blood_surf = pygame.transform.scale(blood_surf, (blood_surf.get_width()//6, blood_surf.get_height()//5.5))

alice_surf = pygame.Surface((550, 50))
alice_surf.set_colorkey(TEAL)

number_surf = pygame.Surface((100, 40))
number_surf.set_colorkey(TEAL)

bg_surf = pygame.image.load("images/mashroom_forrest.jpg")
bg_rect = bg_surf.get_rect(center=(cat_x, cat_y))

pygame.mixer.music.load("sounds/fon1.mp3")
pygame.mixer.music.play(-1)
vol = 0.1
pygame.mixer.music.set_volume(vol)

myau = pygame.mixer.Sound("sounds/mur2.ogg")
ship = pygame.mixer.Sound("sounds/ship1.ogg")
win = pygame.mixer.Sound("sounds/mur4.ogg")
rev = pygame.mixer.Sound("sounds/ryk2.ogg")
mur = pygame.mixer.Sound("sounds/mur1.ogg")

a = pygame.draw
secret_number = ""

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.blit(bg_surf, bg_rect)
    sc.blit(cat_surf, cat_rect)
    number_surf.fill(TEAL)
    sc.blit(number_surf, ((W-50), (H-20)))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        secret_number += "1"
        pygame.time.delay(200)
    elif keys[pygame.K_2]:
        secret_number += "2"
        pygame.time.delay(200)
    elif keys[pygame.K_3]:
        secret_number += "3"
        pygame.time.delay(200)
    elif keys[pygame.K_4]:
        secret_number += "4"
        pygame.time.delay(200)
    elif keys[pygame.K_5]:
        secret_number += "5"
        pygame.time.delay(200)
    elif keys[pygame.K_6]:
        secret_number += "6"
        pygame.time.delay(200)
    elif keys[pygame.K_7]:
        secret_number += "7"
        pygame.time.delay(200)
    elif keys[pygame.K_8]:
        secret_number += "8"
        pygame.time.delay(200)
    elif keys[pygame.K_9]:
        secret_number += "9"
        pygame.time.delay(200)
    elif keys[pygame.K_0]:
        secret_number += "0"
        pygame.time.delay(200)
    elif keys[pygame.K_BACKSPACE]:
        secret_number = secret_number[0:(len(secret_number) - 1)]
        pygame.time.delay(200)
    elif keys[pygame.K_UP]:
        vol += 0.1
        pygame.mixer.music.set_volume(vol)
        pygame.time.delay(200)
    elif keys[pygame.K_DOWN]:
        vol -= 0.1
        pygame.mixer.music.set_volume(vol)
        pygame.time.delay(200)
    elif keys[pygame.K_w]:
        for i, e in enumerate(rules):
            sc.blit(rules_surf, rules_rect)
            rules_surf.blit(blood_surf, blood_rect)
            rules_text = rules_font.render(e, True, RED)
            rules_post = rules_text.get_rect(topleft=(210, 100+(30*i)))
            rules_surf.blit(rules_text, rules_post)
        pygame.display.update()
    elif keys[pygame.K_TAB]:
        counter = 0
        cat_number = randint(0, 100)
        text = "You are so sweet, my heart! Of course, we can play again."
        mur.play()
        cat_surf = pygame.image.load("images/cat_wonderland.png")
        cat_rect = cat_surf.get_rect(center=(cat_x, cat_y))
        sc.blit(cat_surf, cat_rect)
        pygame.display.update()
    elif keys[pygame.K_SPACE]:
        pygame.time.delay(200)
        counter += 1
        try:
            if counter >= 10:
                text = "You lost the time. Run!"
                cat_surf = pygame.image.load("images/cats2.com (7).png")
                cat_rect = cat_surf.get_rect(center=(cat_x, (cat_y+70)))
                sc.blit(cat_surf, cat_rect)
                rev.play()
            else:
                if int(secret_number) > cat_number:
                    text = "Your number is too big, honey...Try again."
                    myau.play()
                elif int(secret_number) < cat_number:
                    text = "Your number is too small, honey...Try again."
                    myau.play()
                elif int(secret_number) == cat_number:
                    text = "You are right! You are win!"
                    win.play()
                    cat_surf = pygame.image.load("images/black_cat_in_hat.png")
                    cat_rect = cat_surf.get_rect(center=(cat_x, cat_y))
                    sc.blit(cat_surf, cat_rect)
        except:
            text = "Silly joke, young lady! You've lost this attempt."
            ship.play()
        secret_number = ""

    secret_text = FONT.render(secret_number, True, AQUA)
    post_secret = secret_text.get_rect(topleft=(5, 1))
    number_surf.blit(secret_text, post_secret)

    sc.blit(number_surf, ((W - 100), (H - 40)))
    alice_surf.fill(TEAL)
    alice_text = FONT.render(text, True, AQUA)
    post = alice_text.get_rect(topleft=(10, 1))
    alice_surf.blit(alice_text, post)
    sc.blit(alice_surf, (alice_x, alice_y))

    pygame.display.update()
    clock.tick(FPS)