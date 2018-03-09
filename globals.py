import pygame
platform=pygame.image.load("platform.png")
camera=pygame.image.load("securitycamera.png")
cannon=pygame.image.load("cannon.png")
character=pygame.image.load("character.jpg.png")
background=pygame.image.load("background.jpg")
cannon=pygame.transform.rotate(cannon,90)
# cannon=pygame.transform.scale(cannon,(78,65))
scale=5
character=pygame.transform.scale(character,(int(331/scale),int(256/scale)))
