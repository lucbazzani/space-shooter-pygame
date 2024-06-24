import pygame
from pygame import Surface, Rect

SC_WIDTH = 576
SC_HEIGHT = 324

# Inicializar o Módulo PyGame
pygame.init()
running = True

#  Criação de janela do PyGame
print('Setup start')
screen: Surface = pygame.display.set_mode(size=(SC_WIDTH, SC_HEIGHT))

# Carregar imagem e gerar uma superfície
bg_surface: Surface = pygame.image.load('./asset/purple_clouds.png').convert_alpha()
player1_surface: Surface = pygame.image.load('./asset/violet_ship.png').convert_alpha()

# Obter o Retângulo da superfície
bg_rect: Rect = bg_surface.get_rect(left=0, top=0)
player1_rect: Rect = player1_surface.get_rect(left=30, top=145)

# Desenhar na janela (screen)
screen.blit(source=bg_surface, dest=bg_rect)
screen.blit(source=player1_surface, dest=player1_rect)

# Atualizar a janela
pygame.display.flip()


def blit_all_and_flip():
    screen.blit(source=bg_surface, dest=bg_rect)
    screen.blit(source=player1_surface, dest=player1_rect)
    pygame.display.flip()


# Colocar um relógio para sincronizar o pressionar das teclas
clock = pygame.time.Clock()

# Carregar música e mantê-la reproduzindo
music = pygame.mixer_music
music.load('./asset/sounds/electronic-diddie-2.mp3')
music.play(-1)

print('Setup end')
print('Loop start')
while running:
    clock.tick(140)  # argumento significa que o loop acontece X vezes por segundo
    # print(f'{clock.get_fps():.0f}')  # monitorar o fps
    blit_all_and_flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print('Loop end')
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1  # diminuir a posição em Y porque o topo da janela possui o valor Y=0
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1

#
