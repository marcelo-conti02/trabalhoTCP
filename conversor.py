from nota_musica import NotaMusica
import random

DEFAULT_OITAVA = 0 
DEFAULT_VOLUME = 0.5
DEFAULT_BPM = 80
MIN_BPM = 60
MAX_BPM = 600
MIN_OITAVA = 0
MAX_OITAVA = 9
MIN_VOLUME = 0.0
MAX_VOLUME = 1

class Conversor:
    def __init__(self, texto):
        self.texto = texto
        self.oitava = DEFAULT_OITAVA
        self.volume = DEFAULT_VOLUME
        self.bpm = DEFAULT_BPM
        self.instrumento = 0

    def is_rmais(self, i):
        return self.texto[i:i+2] == "R+"

    def is_rmenos(self, i):
        return self.texto[i:i+2] == "R-"

    def is_bpm_mais(self, i):
        return self.texto[i:i+4] == "BPM+"

    def is_novalinha(self, i):
        return self.texto[i] == "\n"


    def converte_texto_em_musica(self):
        char_notas = 'AaBbCcDdEeFfGg'
        nota_silencio = NotaMusica(' ')
        notas = []
        i = 0

        while i < len(self.texto):
            char = self.texto[i]


            if char == '+': 
                self.volume = min(self.volume * 2, MAX_VOLUME)
                i +=1
                continue

            elif char == '-':
                self.volume = DEFAULT_VOLUME
                i +=1
                continue

            elif char in 'OoIiUu':
                try:
                    if self.texto[i-1] in char_notas:
                        notas.append(NotaMusica(self.texto[i-1], self.instrumento, self.volume, self.oitava,self.bpm))
                    else:
                        notas.append(NotaMusica('A', 125, self.volume, self.oitava,self.bpm))
                except:
                    notas.append(NotaMusica('A', 125, self.volume, self.oitava,self.bpm))
                i +=1
                continue


            elif self.is_rmais(i):
                self.oitava = min(self.oitava + 1, MAX_OITAVA)
                i += 2
                continue

            elif self.is_rmenos(i):
                self.oitava = max(self.oitava - 1, MIN_OITAVA)
                i += 2
                continue

            elif char == '?':
                notas.append(NotaMusica(random.choice(char_notas), self.instrumento, self.volume, self.oitava,self.bpm))
                i +=1
                continue

            elif self.is_novalinha(i):
                self.instrumento = 44
                i += 1
                continue

            elif self.is_bpm_mais(i):
                self.bpm += 80
                self.bpm = min(self.bpm, MAX_BPM)
                i += 4
                continue

            elif char == ';':
                self.bpm = random.randint(MIN_BPM, MAX_BPM)
                i +=1
                continue
            
            if char in char_notas:
                notas.append(NotaMusica(char, self.instrumento, self.volume, self.oitava,self.bpm))
                i +=1
                continue

                    
            elif char == ' ':
                notas.append(nota_silencio)
                i +=1
                continue                
            
            else:
                if not notas:
                    i +=1
                    continue                    
                notas.append(notas[-1])
                i +=1
                continue

        print(f"Musica gerada com {len(notas)} notas.")
        for nota in notas:
            print(nota.nota,nota.volume)

        return notas
