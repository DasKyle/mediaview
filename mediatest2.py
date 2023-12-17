import os
import pygame
from pygame.locals import *

def ajustar_resolucao_imagem(imagem, tela):
    largura_imagem, altura_imagem = imagem.get_size()
    largura_tela, altura_tela = tela.get_size()

    if largura_imagem > largura_tela or altura_imagem > altura_tela:
        proporcao_largura = largura_tela / largura_imagem
        proporcao_altura = altura_tela / altura_imagem
        proporcao = min(proporcao_largura, proporcao_altura)

        nova_largura = int(largura_imagem * proporcao)
        nov_altura = int(altura_imagem * proporcao)

        return pygame.transform.scale(imagem, (nova_largura, nov_altura))
    else:
        return imagem

def apresentar_midia(diretorio):
    pygame.init()
    tela = pygame.display.set_mode((1920, 1080), FULLSCREEN)
    pygame.display.set_caption('MeliHacks')
    clock = pygame.time.Clock()

    arquivos = [f for f in os.listdir(diretorio) if f.endswith(('.jpg', '.png', '.mp4'))]
    indice = 0
    intervalo_tempo = 15 #intervalo de tempo em segundos
    tempo_passado = 0

    executando = True
    while executando:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_SPACE):
                executando = False

        tempo_passado += clock.tick(30) / 1000.0 #converte para segundos
        if tempo_passado >= intervalo_tempo:
            indice = (indice + 1) % len(arquivos)
            tempo_passado = 0 #reinicia o temporizador

        arquivo_atual = os.path.join(diretorio, arquivos[indice])

        if arquivo_atual.endswith(('.jpg', 'png')):
            imagem = pygame.image.load(arquivo_atual)
            tela.blit(imagem, (0, 0))
        elif arquivo_atual.endswith('.mp4'):
            os.system(f'mpv --fs {arquivo_atual}')

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    diretorio_da_midia = "D:\Mediatest"
    apresentar_midia(diretorio_da_midia)
