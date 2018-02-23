import pygame
platform=pygame.image.load("platform.png")
camera=pygame.image.load("securitycamera.png")
cannon=pygame.image.load("cannon.png")
character=pygame.image.load("character.png")
background=pygame.image.load("background.jpg")
cannon=pygame.transform.rotate(cannon,90)
character=pygame.transform.scale(character,(78,65))