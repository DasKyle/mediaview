import os
import subprocess
import time

def apresentar_midia(diretorio):
    arquivos = [f for f in os.listdir(diretorio) if f.endswith(('.jpg', '.png', '.mp4'))]
    indice = 0
    intervalo_tempo = 5  # intervalo de tempo em segundos

    executando = True
    while executando:
        arquivo_atual = os.path.join(diretorio, arquivos[indice])

        if arquivo_atual.endswith(('.jpg', '.png')):
            # Exibir imagem usando fbi
            subprocess.run(["fbi", "-T", "1", "-noverbose", "-a", arquivo_atual])

        elif arquivo_atual.endswith('.mp4'):
            # Reproduzir vídeo usando mpv
            subprocess.run(["mpv", "--fs", "--loop=inf", "--no-osd", arquivo_atual])

        # Aguardar o intervalo de tempo
        time.sleep(intervalo_tempo)

        indice = (indice + 1) % len(arquivos)

if __name__ == "__main__":
    diretorio_da_midia = "/mnt/dietpi_userdata/Pictures"  # Substitua pelo caminho real do seu diretório
    apresentar_midia(diretorio_da_midia)
