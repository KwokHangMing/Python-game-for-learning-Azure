import pygame
from entity import Entity
from player import Player
import requests
from settings import *
from chatbox import ChatBox

screen = pygame.display.set_mode((WIDTH,HEIGHT))
class NPC(Entity):
    def __init__(self, name, pos, groups, obstacle_sprites, text=None):
        super().__init__(groups)
        self.name = name
        self.image = pygame.image.load(f'../graphics/objects/{name}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-6, -6)
        self.obstacle_sprites = obstacle_sprites
        # self.interact_with_npc = interact_with_npc
        self.text = text
        self.text_box_displayed = False
        self.text_box_timer = 0

    # def interact(self):
        # if self.interact_with_npc is not None:
        #     self.interact_with_npc(self)
        # # Call cloud function or Vertex AI to get response
        #     response = get_response_from_cloud_function_or_vertex_ai()

        # # Display response in text box
        #     display_response_in_text_box(response)
    def interact(self):
        if self.text is not None and not self.text_box_displayed:
            # Send HTTP request to cloud function
            url = 'https://us-central1-final-year-project-400406.cloudfunctions.net/npc-messages'
            data = {'text': self.text}
            response = requests.post(url, json=data)

            if response.status_code == 200:
                self.text_box_displayed = True
                self.text_box_timer = pygame.time.get_ticks()

        elif self.text_box_displayed:
            # Check if timer has expired
            current_time = pygame.time.get_ticks()
            if current_time - self.text_box_timer > 5000:  # Hide text box after 5 seconds
                self.text_box_displayed = False


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            # Check if the player is colliding with an NPC
            npc_group = pygame.sprite.Group()
            player_collisions = pygame.sprite.spritecollide(self, npc_group, False)
            if player_collisions:
                # Interact with the first NPC in the collisions list
                npc = player_collisions[0]
                npc.interact()

        if self.text_box_displayed:
            # Display text box
            font = pygame.font.Font(None, 24)
            text_surface = font.render(self.text_box_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT - 50))
            pygame.draw.rect(screen, (0, 0, 0), (0, HEIGHT - 70, WIDTH, 70))
            screen.blit(text_surface, text_rect)
