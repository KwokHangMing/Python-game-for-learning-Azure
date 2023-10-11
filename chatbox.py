import pygame
import requests
from settings import *
screen = pygame.display.set_mode((WIDTH,HEIGHT))

class ChatBox:
    def __init__(self, text, pos):
        self.text = text
        self.font = pygame.font.Font(None, 24)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(WIDTH / 2, HEIGHT - 50))
        self.timer = pygame.time.get_ticks()
        self.input_box = pygame.Rect(0, HEIGHT - 30, WIDTH, 30)
        self.input_text = ''
        self.input_active = False
        self.pos = pos

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.timer > 5000:  # Hide text box after 5 seconds
            self.text = None
        else:
            # Calculate position of text box
            text_rect = self.text_surface.get_rect(center=(self.pos[0], self.pos[1] - 50))

            pygame.draw.rect(screen, (0, 0, 0), (0, HEIGHT - 70, WIDTH, 70))
            screen.blit(self.text_surface, text_rect)

            # Display input box
            pygame.draw.rect(screen, (255, 255, 255), self.input_box, 2)
            font = pygame.font.Font(None, 24)
            input_text_surface = font.render(self.input_text, True, (255, 255, 255))
            input_text_rect = input_text_surface.get_rect(left=self.input_box.left + 5, centery=self.input_box.centery)
            screen.blit(input_text_surface, input_text_rect)

            # Check for input events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Send HTTP request to cloud function
                        url = 'https://us-central1-final-year-project-400406.cloudfunctions.net/npc-messages'
                        data = {'text': self.input_text}
                        response = requests.post(url, json=data)

                        if response.status_code == 200:
                            self.text = response.json()['text']
                            self.text_surface = self.font.render(self.text, True, (255, 255, 255))
                            self.timer = pygame.time.get_ticks()
                            self.input_text = ''
                            self.input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode

            # Activate input box
            if not self.input_active and pygame.mouse.get_pressed()[0]:
                self.input_active = True
            elif self.input_active and not self.input_box.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                self.input_active = False

            # Blink cursor
            if self.input_active:
                pygame.draw.line(screen, (255, 255, 255), (input_text_rect.right + 5, input_text_rect.centery), (input_text_rect.right + 5, input_text_rect.centery + 10), 2)