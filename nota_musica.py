import pygame.mixer
import time



class NotaMusica:
    def __init__(self, nota, instrumento=0, volume=0.5, oitava=4, bpm = 80):
        self.nota = nota
        self.instrumento = instrumento
        self.volume = volume
        self.oitava = oitava
        self.bpm = bpm
        pygame.mixer.init()  # Inicializa o mixer do pygame

    def tocar(self):
        if self.nota != ' ':
            arquivo_audio = f"sons/{self.nota}.wav"  # Caminho para o arquivo de som da nota
            try:
                pygame.mixer.music.load(arquivo_audio)  # Carrega o arquivo de som
                pygame.mixer.music.set_volume(self.volume)  # Ajusta o volume
                pygame.mixer.music.play()  # Reproduz o som
                print(f"Tocando {self.nota} com {self.instrumento} na oitava {self.oitava}")

                # Aguarda até a música ser finalizada
                while pygame.mixer.music.get_busy():  # Verifica se a música ainda está tocando
                    time.sleep(0.1)  # Aguarda um pouco antes de verificar novamente
            except Exception as e:
                print(f"Erro ao tentar tocar a nota {self.nota}: {e}")
        else:
            print("Silêncio")

    def __str__(self):
        return f"Nota: {self.nota}, Instrumento: {self.instrumento}, Oitava: {self.oitava}"

    def trocarInstrumento(self, novo_instrumento):
        self.instrumento = novo_instrumento
        print(f"Instrumento trocado para {self.instrumento}")

    def alterarVolume(self, novo_volume):
        self.volume = novo_volume
        print(f"Volume ajustado para {self.volume}")

    def alterarOitava(self, nova_oitava):
        self.oitava = nova_oitava
        print(f"Oitava ajustada para {self.oitava}")



