import pygame
import random
import math

# Inicializando o pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bolas com Status em Círculo")

# Definindo as cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)   # Cor de "pensando"
AMARELO = (255, 255, 0)  # Cor de "fome"
AZUL = (0, 0, 255)    # Cor de "comendo"

# Lista de status possíveis
status_options = ["pensando", "fome", "comendo"]

# Classe para representar as bolas
class Bola:
    def __init__(self, angulo, raio_circulo, centro_x, centro_y):
        # Cálculo da posição (x, y) com base no ângulo
        self.x = centro_x + raio_circulo * math.cos(angulo)
        self.y = centro_y + raio_circulo * math.sin(angulo)
        self.radius = 30
        self.status = "pensando"  # Status inicial
        self.cor = VERDE  # Cor inicial, associada ao status "pensando"
    
    def mudar_status(self):
        # Mudar status aleatoriamente
        self.status = random.choice(status_options)
        
        # Mudar a cor de acordo com o status
        if self.status == "pensando":
            self.cor = VERDE
        elif self.status == "fome":
            self.cor = AMARELO
        elif self.status == "comendo":
            self.cor = AZUL

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.radius)

# Definindo o número de bolas
num_bolas = 5
raio_circulo = 150  # Raio do círculo em que as bolas irão se posicionar
centro_x = screen_width // 2  # Centro do círculo (meia largura da tela)
centro_y = screen_height // 2  # Centro do círculo (meia altura da tela)

# Calculando o ângulo para distribuir as bolas no círculo
bolas = []
for i in range(num_bolas):
    angulo = 2 * math.pi * i / num_bolas  # Distribui as bolas igualmente ao longo do círculo
    bola = Bola(angulo, raio_circulo, centro_x, centro_y)
    bolas.append(bola)

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(PRETO)  # Preenchendo o fundo com a cor preta

    for bola in bolas:
        bola.desenhar(screen)  # Desenhando as bolas na tela
        bola.mudar_status()    # Mudando o status de cada bola (seu comportamento)

    pygame.display.flip()  # Atualizando a tela

    # Controle de eventos para fechar o programa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(2)  # Alterando o status das bolas a cada 2 segundos (para exemplo)

pygame.quit()
