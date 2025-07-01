import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from documento import Documento
from musica import Musica
from conversor import Conversor
import pygame.mixer

DEFAULT_VOLUME = 50  
DEFAULT_OITAVA = 4 
MIN_OITAVA = 0
MAX_OITAVA = 8

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Música a partir de Texto")
        # Configuração da janela principal
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Estilo dos botões
        button_style = {
            "bg": "#4CAF50", 
            "fg": "white", 
            "font": ("Helvetica", 10, "bold"), 
            "relief": "raised", 
            "bd": 2
        }

        # Cabeçalho
        self.titulo_label = tk.Label(
            self.root, 
            text="Gerador de Música a partir de Texto", 
            font=("Helvetica", 16, "bold"), 
            bg="#4CAF50", 
            fg="white", 
            pady=10
        )
        self.titulo_label.pack(fill="x")

        # Área principal
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(pady=20)

        # Campo de texto
        self.texto_label = tk.Label(
            self.main_frame, 
            text="Texto ou Arquivo de Música:", 
            bg="#f0f0f0", 
            font=("Helvetica", 12, "bold")
        )
        self.texto_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.texto_entry = tk.Text(self.main_frame, height=5, width=50)
        self.texto_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        # Botões de ação
        self.carregar_button = tk.Button(
            self.main_frame, 
            text="Carregar Arquivo", 
            command=self.carregar_arquivo, 
            **button_style
        )
        self.carregar_button.grid(row=2, column=0, padx=10, pady=5)

        self.carregar_texto_button = tk.Button(
            self.main_frame, 
            text="Carregar Texto", 
            command=self.carregar_texto_digitado, 
            **button_style
        )
        self.carregar_texto_button.grid(row=2, column=1, padx=10, pady=5)

        # Status da música
        self.estado_musica = tk.Label(
            self.main_frame, 
            text="Estado da Música: Pronta para tocar", 
            font=("Helvetica", 12, "bold"), 
            bg="#f0f0f0"
        )
        self.estado_musica.grid(row=10, column=0, columnspan=3, pady=10)

        # Controles de reprodução
        self.controles_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.controles_frame.pack(pady=20)

        self.reproduzir_button = tk.Button(
            self.controles_frame, 
            text="▶ Reproduzir", 
            command=self.alternar_reproducao, 
            width=10, 
            **button_style
        )
        self.reproduzir_button.grid(row=0, column=0, padx=10)

        #self.pausar_button = tk.Button(
        #    self.controles_frame, 
        #    text="⏸ Pausar", 
        #   command=self.pausar_musica, 
        #    width=10, 
        #    **button_style
        #)
        #self.pausar_button.grid(row=0, column=1, padx=10)

        self.resetar_button = tk.Button(
            self.controles_frame, 
            text="⏹ Reiniciar", 
            command=self.resetar_musica, 
            width=10, 
            **button_style
        )
        self.resetar_button.grid(row=0, column=2, padx=10)

        # Controles avançados
        self.controles_avancados_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.controles_avancados_frame.pack(pady=10)

        # Volume
        self.volume_label = tk.Label(
            self.controles_avancados_frame, 
            text="Volume:", 
            bg="#f0f0f0"
        )
        self.volume_label.grid(row=0, column=0, padx=5)
        
        self.volume_scale = tk.Scale(
            self.controles_avancados_frame, 
            from_=0, 
            to=100, 
            orient="horizontal",
            command=self.alterar_volume
        )
        self.volume_scale.set(DEFAULT_VOLUME)
        self.volume_scale.grid(row=0, column=1, padx=5)



        #Oitava
        #self.oitava_label = tk.Label(
        #    self.controles_avancados_frame, 
        #    text="Oitava:", 
        #    bg="#f0f0f0"
        #)
        #self.oitava_label.grid(row=0, column=2, padx=5)
        
        #self.oitava_scale = tk.Scale(
        #    self.controles_avancados_frame, 
        #    from_=MIN_OITAVA, 
        #    to=MAX_OITAVA, 
        #    orient="horizontal",
        #    command=self.alterar_oitava
        #)
        #self.oitava_scale.set(DEFAULT_OITAVA)
        #self.oitava_scale.grid(row=0, column=3, padx=5)

        # Instrumento
        self.instrumento_label = tk.Label(
            self.controles_avancados_frame, 
            text="Instrumento:", 
            bg="#f0f0f0"
        )
        self.instrumento_label.grid(row=0, column=4, padx=5)
        
        self.instrumento_var = tk.StringVar()
        self.instrumento_combobox = ttk.Combobox(
            self.controles_avancados_frame,
            textvariable=self.instrumento_var,
            values=[
                "Piano (0)", "Guitarra (24)", 
                "Violino (40)", "Bateria (118)",
                "Flauta (73)", "Saxofone (66)"
            ],
            state="readonly"
        )
        self.instrumento_combobox.set("Piano (0)")
        self.instrumento_combobox.bind("<<ComboboxSelected>>", self.alterar_instrumento)
        self.instrumento_combobox.grid(row=0, column=5, padx=5)

        self.musica = None

    def carregar_arquivo(self):
        
        caminho_arquivo = filedialog.askopenfilename(
            title="Escolher Arquivo de Texto",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if caminho_arquivo:
            documento = Documento(caminho_arquivo)
            if documento.validarDoc():
                self.estado_musica.config(text="Estado da Música: Preparando para tocar")
                self.texto_entry.delete(1.0, tk.END)
                self.texto_entry.insert(tk.END, documento.texto)
            else:
                messagebox.showerror("Erro", "Arquivo inválido. Tente novamente.")
        else:
            messagebox.showinfo("Informação", "Nenhum arquivo foi selecionado.")


    def carregar_texto_digitado(self):
        texto_digitado = self.texto_entry.get(1.0, tk.END).strip()
        if texto_digitado:
            if self.musica:
                self.musica.fechar()
                self.musica = None

            documento = Documento("texto_digitado")
            documento.texto = texto_digitado
            conversor = Conversor(documento.texto)
            
            # Aplica as configurações atuais
            conversor.volume = self.volume_scale.get() / 100
            #conversor.oitava = self.oitava_scale.get()
            conversor.instrumento = int(self.instrumento_var.get().split("(")[-1].rstrip(")"))
            
            notas = conversor.converte_texto_em_musica()
            self.musica = Musica(notas)
            self.estado_musica.config(text="Estado da Música: Pronto para tocar")
        else:
            messagebox.showerror("Erro", "O campo de texto está vazio. Digite algo antes de reproduzir.")


    def reproduzir_musica(self):
        if not self.musica:
            self.carregar_texto_digitado()

        if self.musica:
            self.musica.reproduzir()
            self.estado_musica.config(text="Estado da Música: Tocando")
        else:
            messagebox.showerror("Erro", "Nenhuma música carregada. Digite um texto ou carregue um arquivo primeiro.")


    def pausar_musica(self):
        if self.musica:
            self.musica.pausar()
            self.estado_musica.config(text="Estado da Música: Pausada")
        else:
            messagebox.showerror("Erro", "Nenhuma música carregada para pausar.")

    def alternar_reproducao(self):

        if not self.musica.is_playing:
            # Reproduzir
            self.reproduzir_musica()
            self.reproduzir_button.config(text="⏸ Pausar")
            self.estado_musica.config(text="Estado da Música: Tocando")
        else:
            if self.musica.is_paused:
                self.reproduzir_musica()
                self.reproduzir_button.config(text="⏸ Pausar")
                self.estado_musica.config(text="Estado da Música: Tocando")
            else:                
                # Pausar
                self.pausar_musica()
                self.reproduzir_button.config(text="▶ Reproduzir")
                self.estado_musica.config(text="Estado da Música: Pausada")


    def resetar_musica(self):
        if self.musica:
            self.musica.resetar()
            self.estado_musica.config(text="Estado da Música: Reiniciada")
            self.reproduzir_button.config(text="⏸ Pausar")
        else:
            messagebox.showerror("Erro", "Nenhuma música carregada para reiniciar.")
        

    def alterar_volume(self, valor):
        if self.musica:
            volume_normalizado = int(valor) / 100
            self.musica.set_volume(volume_normalizado)
            self.estado_musica.config(text=f"Volume: {valor}%")
        else:
            self.estado_musica.config(text=f"Volume: {valor}% (aguardando música)")


    
    def alterar_oitava(self, valor):
        if hasattr(self, 'musica') and self.musica:
            for nota in self.musica.notas:
                nota.oitava = int(valor)
            self.estado_musica.config(text=f"Oitava: {valor}")
            if self.musica.is_playing:
                self.resetar_musica()


    def alterar_instrumento(self, event=None):
        if hasattr(self, 'musica') and self.musica:
            try:
                instrumento_texto = self.instrumento_var.get()
                novo_instrumento = int(instrumento_texto.split("(")[-1].rstrip(")"))
                for nota in self.musica.notas:
                    nota.instrumento = novo_instrumento
                self.estado_musica.config(text=f"Instrumento: {instrumento_texto}")
                if self.musica.is_playing:
                    self.musica.player.set_instrument(novo_instrumento)
            except Exception as e:
                print(f"Erro ao alterar instrumento: {e}")

       
    def baixar_musica(self):
        pass
