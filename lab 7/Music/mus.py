import sys, pygame, os
import time

pygame.init()

# display
screen = pygame.display.set_mode((500, 500))

# MUSIC
mus = os.listdir('C:/Users/Hp/Documents/pp2_dias/PP2/lab 7/Music')
index = 0
path = 'C:/Users/Hp/Documents/pp2_dias/PP2/lab 7/Music/{}'

pygame.mixer.music.load(path.format(mus[index]))
pygame.mixer.music.play()
pygame.mixer.music.pause()

isPlaying = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        if isPlaying:
            pygame.mixer.music.pause()
            isPlaying = False
        else:
            pygame.mixer.music.unpause()
            isPlaying = True

    if key[pygame.K_RIGHT]:
        index += 1
        if index == len(mus):
            index = 0

        pygame.mixer.music.load(path.format(mus[index]))
        pygame.mixer.music.play()

    if key[pygame.K_LEFT]:
        index -= 1
        if index < 0:
            index = len(mus) - 1

        pygame.mixer.music.load(path.format(mus[index]))
        pygame.mixer.music.play()

    if key[pygame.K_END]:
        pygame.mixer.music.stop()

    time.sleep(0.2)