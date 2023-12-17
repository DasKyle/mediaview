import os
import pygame
from pygame.locals import *

def ajustar_resolucao_imagem(imagem, tela):
   largura_tela, altura_tela = tela.get_size()
   proporcao_largura = largura_tela / float(imagem.get_width())
   proporcao_altura = altura_tela / float(imagem.get_height())
   proporcao = max(proporcao_largura, proporcao_altura)
   nova_largura = int(imagem.get_width() * proporcao)
   nova_altura = int(imagem.get_height() * proporcao)
   return pygame.transform.scale(imagem, (nova_largura, nova_altura))

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

        tela.fill((0, 0, 0))

        if arquivo_atual.endswith(('.jpg', '.png')):
            imagem = pygame.image.load(arquivo_atual)
            imagem_ajustada = ajustar_resolucao_imagem(imagem, tela)
            tela.blit(imagem_ajustada, ((tela.get_width() - imagem_ajustada.get_width()) // 2, (tela.get_height() - imagem_ajustada.get_height()) // 2))
        elif arquivo_atual.endswith('.mp4'):
            os.system(f'mpv --fs {arquivo_atual}')

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    diretorio_da_midia = "D:\Mediatest"
    apresentar_midia(diretorio_da_midia)
