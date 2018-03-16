import pygame
platform=pygame.image.load("platform.png")
camera=pygame.image.load("securitycamera.png")
minigun=pygame.image.load("minigun.png")
character=pygame.image.load("character.jpg.png")
background=pygame.image.load("background.jpg")
minigun=pygame.transform.rotate(minigun,90)
# cannon=pygame.transform.scale(cannon,(78,65))
scale=5
character=pygame.transform.scale(character,(int(331/scale),int(256/scale)))
bottom=pygame.transform.scale(platform,(1400,1))
bullet=pygame.image.load("bullet.png")