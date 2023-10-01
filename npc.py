import pygame
import requests

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # 设置NPC的图像（可以是一个矩形表现）
        self.image.fill((255, 0, 0))  # 设置NPC的颜色（这里设置为红色）
        self.rect = self.image.get_rect()
        self.rect.x = x  # 设置NPC的初始位置
        self.rect.y = y

    def update(self):
        # NPC的更新逻辑（例如移动、碰撞检测等）
        pass