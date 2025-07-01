import pygame.mixer
import time



class NotaMusica:
    
    def __init__(self, nota, instrumento=0, volume=0.5, oitava=0, bpm = 80):
        self.nota = nota
        self.instrumento = instrumento
        self.volume = volume
        self.oitava = oitava
        self.bpm = bpm
        pygame.mixer.init()  # Inicializa o mixer do pygame

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



