from turtle import left
import pygame
from pygame import mixer
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

class Game():
    def __init__(self):
        pygame.display.set_caption("game")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()
        self.sprite_nums = [7,2]
        self.sounds = [mixer.Sound("sounds/sound_1_2.wav")]
        mixer.music.load("sounds/sound_1_1.wav")
        mixer.music.play(-1)
        self.path = ""
        self.sprites = []
        for n in range(0, len(self.sprite_nums)):
            self.sprites.append([])
            for j in range(0, self.sprite_nums[n]):
                self.path = f"sprites/sprite_{n+1}_{j+1}.png"
                if n == 0:
                    self.sprites[n].append(pygame.transform.scale(pygame.image.load(self.path).convert_alpha(), (self.width, self.height)))
                else:
                    self.sprites[n].append(pygame.transform.scale(pygame.image.load(self.path).convert_alpha(), ((self.width / 1100) * 165, (self.height / 600) * 90)))
        self.run = True
        self.background_num_1 = 0
        self.background_num_2 = 0

    def update(self):
        if self.background_num_1 <= 45: self.background_num_1 += 1
        else:
            self.background_num_1 = 0
            if self.background_num_2 <= len(self.sprites[0])-2: self.background_num_2 += 1
            else: self.background_num_2 = 0
        self.keys = pygame.key.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        if self.keys[pygame.K_ESCAPE]:
            self.run = False
    
    def drawWin(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.sprites[0][self.background_num_2], (0, 0))
        for button in buttons:
            self.screen.blit(button.images[button.hovered], button.rect)
        pygame.display.update()

class Button():
    def __init__(self, x, y, image):
        self.images = image
        self.x = x
        self.y = y
        self.rect = self.images[0].get_rect(center = (self.x, self.y))
        self.clicked = False
        self.hovered = 0

    def update(self):
        if self.rect.collidepoint(game.mouse_pos) and self.hovered == 0:
            self.hovered = 1
            mixer.Sound.play(game.sounds[0])
        elif self.rect.collidepoint(game.mouse_pos) and self.hovered == 1:
            self.hovered = 1
        else:
            self.hovered = 0

game = Game()
buttons = []
buttons.append(Button((game.width / 1100) * 100 + (game.width / 1100) * (165 / 2), (game.height / 600) * 488 + (game.height / 600) * (90 / 2), game.sprites[1]))

while game.run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False

    game.update()
    for button in buttons:
        button.update()
    game.drawWin()
    
pygame.quit()