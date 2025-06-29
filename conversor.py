from nota_musica import NotaMusica

DEFAULT_OITAVA = 0 
DEFAULT_VOLUME = 25
MIN_OITAVA = 0
MAX_OITAVA = 9
MAX_VOLUME = 0
MIN_VOLUME = 100

class Conversor:
    def __init__(self, texto):
        self.texto = texto
        self.oitava = DEFAULT_OITAVA
        self.volume = DEFAULT_VOLUME
        self.instrumento = 0

    def is_rmais(self, i):
        if i+1 <= len(self.texto):
            return self.texto[i:i+1] == "R+"
        return False

    def is_rmenos(self, i):
        if i+1 <= len(self.texto):
            return self.texto[i:i+1] == "R-"
        return False

    def is_novalinha(self, i):
        if i+1 <= len(self.texto):
            return self.texto[i:i+1] == "\n"    
        return False

    def is_bpm_mais(self, i):
        if i+3 <= len(self.texto):
            return self.texto[i:i+3] == "BPM+"
        return False

    def converte_texto_em_musica(self):
        char_notas = 'AaBbCcDdEeFfGg'
        nota_silencio = NotaMusica(' ')
        notas = []
        ultima_nota = None
        i = 0

        while i < len(self.texto):
            char = self.texto[i]

            if self.is_rmais(i):
                self.oitava = min(self.oitava + 1, MAX_OITAVA)
                i += 2
                continue
            elif self.is_rmenos(i):
                self.oitava = max(self.oitava - 1, MIN_OITAVA)
                i += 2
                continue
            elif self.is_bpm_mais(i):
                self.volume = min(self.volume + 10, MIN_VOLUME)
                i += 4
                continue
            elif self.is_novalinha(i):
                self.instrumento = 44
                i += 1
                continue

            if char in char_notas:
                notas.append(NotaMusica(char, self.instrumento, self.volume, self.oitava))
                ultima_nota = char
            elif char == ' ':
                notas.append(nota_silencio)

            elif char == '!':
                self.instrumento = 24

            elif char in 'OoIiUu':
                if ultima_nota in char_notas:
                    notas.append(NotaMusica(ultima_nota, self.instrumento, self.volume, self.oitava))
                else:
                    notas.append(NotaMusica('A', 125, self.volume, self.oitava))
                 
            elif char in 'hjklmnpqrstvwxyz':
                if ultima_nota in char_notas:
                    notas.append(NotaMusica(ultima_nota, self.instrumento, self.volume, self.oitava))
                else:
                    notas.append(nota_silencio)
            elif char.isdigit():
                if int(char) % 2 == 0:
                    self.instrumento += int(char)
                else:
                    self.instrumento = 15

            elif char == '?':
                continue

            elif char == ';':
                continue
                
            elif char == '+':
                print(self.volume)
                self.volume = max(self.volume * 2, MAX_VOLUME)
                print(self.volume)
            elif char == '-':
                self.volume = DEFAULT_VOLUME

            else:
                notas.append(NotaMusica(ultima_nota, self.instrumento, self.volume, self.oitava))

            i += 1

        print(f"Música gerada com {len(notas)} notas.")
        return notas
