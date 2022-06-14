#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3') # substituir musica pelo nome do arquivo
pygame.mixer.musica.play()

pygame.event.wait()
