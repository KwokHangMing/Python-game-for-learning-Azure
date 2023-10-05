import pygame

class Book(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-6, -6)
        self.is_interactive = True

    def interact(self):
        # Call cloud function or Vertex AI to get response
        response = get_response_from_cloud_function_or_vertex_ai()

        # Display response in text box
        display_response_in_text_box(response)

    def update(self):
        pass