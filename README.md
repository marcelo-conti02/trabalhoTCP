# Gerador de Música a partir de Texto

## Descrição
Este projeto é uma aplicação que converte texto em música. Ele utiliza uma interface gráfica para permitir que o usuário insira texto ou carregue um arquivo de texto, que é então processado para gerar notas musicais. As notas são reproduzidas usando a biblioteca `pygame.midi`.

O objetivo principal é transformar texto em uma experiência musical interativa, onde cada caractere do texto é mapeado para uma nota ou ação musical específica.

---

## Estrutura do Projeto

### Arquivos
- **`main.py`**: Arquivo principal que inicializa a interface gráfica e gerencia a execução do programa.
- **`interface.py`**: Contém a classe `Interface`, que gerencia a interação com o usuário por meio de uma GUI (Interface Gráfica do Usuário) construída com `tkinter`.
- **`documento.py`**: Contém a classe `Documento`, responsável por carregar, validar e processar o texto para gerar notas musicais.
- **`musica.py`**: Contém a classe `Musica`, que gerencia a reprodução das notas musicais usando `pygame.midi`.
- **`nota_musica.py`**: Contém a classe `NotaMusica`, que representa uma nota musical individual e gerencia sua reprodução.
- **`musica.txt`**: Arquivo de exemplo contendo texto que pode ser processado para gerar música.
- **`musica/musica.mid`**: Arquivo MIDI gerado ou utilizado pelo projeto.
- **`icons/`**: Pasta contendo ícones para os instrumentos disponíveis na interface gráfica.
- **`__pycache__/`**: Diretório gerado automaticamente pelo Python para armazenar arquivos compilados.

---

## Dependências
- **Python 3.9 ou superior**
- **Bibliotecas Python**:
  - `pygame`
  - `tkinter` (incluso no Python)

---

## Como Executar

1. **Instale o Python**:
   - Certifique-se de que o Python está instalado no sistema. Você pode verificar executando:
     ```bash
     python --version
     ```

2. **Instale as dependências**:
   - Instale a biblioteca `pygame`:
     ```bash
     pip install pygame
     ```

3. **Execute o projeto**:
   - Navegue até o diretório do projeto:
     ```bash
     cd c:\Users\User\Desktop\trabalho\trabalho
     ```
   - Execute o arquivo principal:
     ```bash
     python main.py
     ```

4. **Interaja com a interface gráfica**:
   - Use a interface para carregar texto ou arquivos e reproduzir música.
   - Selecione o instrumento desejado no menu suspenso e clique em "Atualizar Instrumento" para alterar o som.

---

## Funcionalidades

### Carregar Texto
- O usuário pode carregar texto de um arquivo ou digitá-lo diretamente na interface.
- O texto é validado para garantir que contém apenas caracteres permitidos.

### Gerar Música
- O texto validado é processado para gerar uma lista de notas musicais.
- Cada nota é representada por um objeto `NotaMusica`.

### Reproduzir Música
- As notas geradas são reproduzidas sequencialmente utilizando sons MIDI.
- A reprodução é gerenciada por uma thread separada para evitar travamentos na interface.

### Pausar e Reiniciar
- O usuário pode pausar a reprodução e retomá-la posteriormente.
- A música pode ser reiniciada desde o início a qualquer momento.

### Alterar Instrumento
- O usuário pode selecionar entre os seguintes instrumentos na interface gráfica:
  - Guitarra
  - Violino
  - Violão
  - Piano
  - Bateria
  - Flauta
- Após selecionar, clique em "Atualizar Instrumento" para aplicar a alteração.

---

## Detalhamento das Classes

### `Documento` (documento.py)
A classe `Documento` é responsável por gerenciar o texto que será convertido em música. Ela lida com a abertura, validação e processamento do texto para gerar notas musicais.

#### Atributos:
- `caminho_arquivo`: Caminho do arquivo de texto a ser carregado.
- `texto`: Conteúdo do texto carregado.
- `notas`: Lista de notas musicais geradas a partir do texto.

#### Métodos:
- `abrir()`: Abre o arquivo de texto e carrega seu conteúdo no atributo `texto`.
- `validarDoc()`: Valida o texto carregado, verificando se contém apenas caracteres permitidos.
- `gerarMusica()`: Processa o texto para gerar uma lista de objetos `NotaMusica` representando as notas musicais.

---

### `Interface` (interface.py)
A classe `Interface` gerencia a interação com o usuário por meio de uma interface gráfica construída com `tkinter`. Ela permite carregar texto, gerar música e controlar a reprodução.

#### Atributos:
- `root`: Janela principal da interface gráfica.
- `main_frame`: Frame principal para organizar os elementos da interface.
- `texto_entry`: Campo de texto para entrada ou exibição do texto.
- `estado_musica`: Label que exibe o estado atual da música.
- `musica`: Instância da classe `Musica` que gerencia a reprodução.

#### Métodos:
- `carregar_arquivo()`: Permite ao usuário carregar um arquivo de texto.
- `carregar_texto_digitado()`: Processa o texto digitado pelo usuário no campo de texto.
- `reproduzir_musica()`: Inicia a reprodução da música gerada.
- `pausar_musica()`: Pausa a reprodução da música.
- `resetar_musica()`: Reinicia a reprodução da música.
- `atualizar_instrumento()`: Atualiza o instrumento selecionado para as notas musicais.

---

### `Musica` (musica.py)
A classe `Musica` gerencia a reprodução das notas musicais geradas a partir do texto. Ela utiliza a biblioteca `pygame.midi` para tocar as notas.

#### Atributos:
- `notas`: Lista de objetos `NotaMusica` representando as notas a serem reproduzidas.
- `player`: Objeto MIDI responsável por tocar as notas.
- `is_playing`: Indica se a música está sendo reproduzida.
- `is_paused`: Indica se a música está pausada.
- `playback_thread`: Thread responsável pela reprodução das notas.

#### Métodos:
- `reproduzir()`: Inicia a reprodução das notas musicais.
- `_playback()`: Método interno que executa a reprodução em uma thread separada.
- `pausar()`: Pausa ou retoma a reprodução.
- `resetar()`: Reinicia a reprodução desde o início.
- `parar()`: Para a reprodução e finaliza a thread.
- `fechar()`: Finaliza o uso do dispositivo MIDI.

---

### `NotaMusica` (nota_musica.py)
A classe `NotaMusica` representa uma nota musical individual e gerencia sua reprodução.

#### Atributos:
- `nota`: Representação textual da nota (ex.: `A`, `B`, `C`).
- `instrumento`: Instrumento associado à nota.
- `volume`: Volume da nota.
- `oitava`: Oitava da nota.

#### Métodos:
- `tocar()`: Reproduz a nota utilizando arquivos de som.
- `trocarInstrumento()`: Altera o instrumento associado à nota.
- `alterarVolume()`: Ajusta o volume da nota.

---

## Limitações
- Apenas caracteres específicos (`A` a `H`) são processados como notas musicais.
- O projeto depende de dispositivos MIDI disponíveis no sistema.

---

## Como Personalizar
- **Adicionar novos sons**:
  - Adicione arquivos `.wav` na pasta `sons/` e ajuste o código em `NotaMusica` para utilizá-los.
- **Alterar mapeamento de notas**:
  - Modifique o método `_converter_nota_para_midi` na classe `Musica` para alterar o mapeamento de caracteres para valores MIDI.
- **Adicionar novos instrumentos**:
  - Atualize o método `_converter_instrumento_para_midi` na classe `Musica` para incluir novos instrumentos MIDI.

