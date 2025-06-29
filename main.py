from documento import Documento
from musica import Musica
from interface import Interface
from nota_musica import NotaMusica
import tkinter as tk
from conversor import Conversor


def alterar_configuracoes():
    # Cria uma nota padrão para configuração inicial
    nota = NotaMusica("C")

    while True:
        print("\nConfigurações da Nota:")
        print("1. Alterar Instrumento")
        print("2. Alterar Volume")
        print("3. Alterar Oitava")
        print("4. Tocar Nota")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            novo_instrumento = input("Digite o novo instrumento: ")
            nota.trocarInstrumento(novo_instrumento)
        elif escolha == "2":
            try:
                novo_volume = float(input("Digite o novo volume (0.0 a 1.0): "))
                if 0.0 <= novo_volume <= 1.0:
                    nota.alterarVolume(novo_volume)
                else:
                    print("Volume fora do intervalo permitido.")
            except ValueError:
                print("Entrada inválida. Digite um número entre 0.0 e 1.0.")
        elif escolha == "3":
            try:
                nova_oitava = int(input("Digite a nova oitava (1 a 8): "))
                if 1 <= nova_oitava <= 8:
                    nota.alterarOitava(nova_oitava)
                else:
                    print("Oitava fora do intervalo permitido.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro entre 1 e 8.")
        elif escolha == "4":
            nota.tocar()
        elif escolha == "5":
            print("Saindo das configurações.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
