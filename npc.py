import pygame
from entity import Entity
from player import Player

class NPC(Entity):
    def __init__(self, name, pos, groups, obstacle_sprites, interact_with_npc=None):
        super().__init__(groups)
        self.name = name
        self.image = pygame.image.load(f'../graphics/objects/{name}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-6, -6)
        self.obstacle_sprites = obstacle_sprites
        self.interact_with_npc = interact_with_npc

    def interact(self):
        if self.interact_with_npc is not None:
            self.interact_with_npc(self)
        # Call cloud function or Vertex AI to get response
            response = get_response_from_cloud_function_or_vertex_ai()

        # Display response in text box
            display_response_in_text_box(response)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check if the player is colliding with an NPC
                    npc_group = pygame.sprite.Group()
                    player_collisions = pygame.sprite.spritecollide(Player, npc_group, False)
                    if player_collisions:
                        # Interact with the first NPC in the collisions list
                        npc = player_collisions[0]
                        npc.interact() 