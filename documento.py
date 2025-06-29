from nota_musica import NotaMusica

class Documento:

    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.texto = ""

    def abrir(self):
        print(self.caminho_arquivo)
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                self.texto = arquivo.read()
            return True
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")
            return False

    def validarDoc(self):
        if self.abrir():
            return True
        return False

