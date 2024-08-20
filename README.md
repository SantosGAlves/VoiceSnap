# VoiceSnap

![logo](https://github.com/SantosGAlves/VoiceSnap/blob/main/Images/HEAD.png)

## Descrição

O **VoiceSnap** é um aplicativo simples e intuitivo que permite transcrever arquivos de áudio usando o modelo Whisper. Desenvolvido com Python e CustomTkinter, o VoiceSnap é fácil de usar, com uma interface amigável que oferece recursos de seleção de arquivos de áudio, transcrição automática e cópia de texto. Ideal para profissionais e estudantes que precisam converter áudio em texto de forma eficiente.

## Funcionalidades

- **Transcrição de Áudio:** Converte arquivos de áudio em texto utilizando o modelo Whisper.
- **Interface Amigável:** Desenvolvido com CustomTkinter, oferece uma interface moderna e fácil de usar.
- **Cópia para Área de Transferência:** Permite copiar rapidamente o texto transcrito para outros aplicativos.
- **Suporte a Vários Formatos de Áudio:** Suporta formatos como MP3, WAV, M4A, FLAC, MP4, WMV e OPUS.

## Tecnologias Utilizadas

- **Python 3.x**
- **Whisper (OpenAI)**
- **CustomTkinter**
- **Pillow (PIL)**

## Uso

1. Abra o aplicativo **VoiceSnap**.
2. Clique no botão **"Selecione o arquivo"** para escolher o arquivo de áudio que deseja transcrever.
3. O texto transcrito aparecerá na interface assim que a transcrição for concluída.
4. Use o botão **"Copiar"** para copiar o texto transcrito para a área de transferência.

## Estrutura do Projeto
1. main.py: Arquivo principal que contém o código da interface e a lógica de transcrição.
2. images/: Diretório contendo as imagens usadas na interface, como ícones e logos.
3. requirements.txt: Lista de dependências do projeto.

## Funcionalidades
- Suporte a múltiplos formatos de áudio, incluindo MP3, WAV, M4A, FLAC, MP4, WMV e OPUS.
- Interface simples e intuitiva.
- Transcrição rápida e precisa usando o modelo Whisper.
- Opção de copiar o texto transcrito para a área de transferência.

## Capturas de Tela

![logo](https://github.com/SantosGAlves/VoiceSnap/blob/main/Images/Tela_Snap1.jpg)
![logo](https://github.com/SantosGAlves/VoiceSnap/blob/main/Images/Tela_VoiceSnap.jpg)

## Instalação

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em sua máquina. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

### Passo a Passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/VoiceSnap.git
   cd VoiceSnap
   
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    .\venv\Scripts\activate  # Para Windows
   
3. Instale as dependências necessárias:
   ```bash
    pip install -r requirements.txt

4. Execute o aplicativo:
   ```bash
    python voicesnap.py


   
