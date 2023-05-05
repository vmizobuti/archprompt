import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    )
from util import messageBox, typingBox, prompter

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (148, 214, 10)

# Cria a instância do PyGame
pygame.init()
size = width, height = 1200, 600
screen = pygame.display.set_mode(size)

# Fontes
GROT_LIGHT = "_assets/FoundersGrotesk-Light.otf"
GROT_MEDIUM = "_assets/FoundersGrotesk-Medium.otf"
textFont = pygame.font.Font(GROT_LIGHT, 16)
headerFont = pygame.font.Font(GROT_MEDIUM, 16)
smallFont = pygame.font.Font(GROT_LIGHT, 24)
mediumFont = pygame.font.Font(GROT_LIGHT, 32)
largeFont = pygame.font.Font(GROT_MEDIUM, 40)

# Inicializa o PyGame até o encerramento da instância
running = True

while running:
    # Encerra a instância se o usuário fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com um fundo preto
    screen.fill((0, 0, 0))

    # Cria o título da aplicação
    title = largeFont.render("Arch.Prompt", True, WHITE)
    titleRect = title.get_rect()
    titleRect.left = 40
    titleRect.top = 40
    screen.blit(title, titleRect)

    # Cria o subtítulo da aplicação
    subtitle = smallFont.render("by Superlimão _ v.1.0", True, GREEN)
    subtitleRect = title.get_rect()
    subtitleRect.left = 40
    subtitleRect.top = 80
    screen.blit(subtitle, subtitleRect)

    # Adiciona a tabela para geração dos prompts
    headers = [
        "Composição", "Câmera", "Estilo da Imagem", "Conteúdo", "Ponto Focal", 
        "Texturas", "Paleta", "Iluminação", "Localização", "Período",
        "Sensação", "Estilo Arquitetônico", "Tipologia" 
        ]

    # Adiciona a tabela
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()