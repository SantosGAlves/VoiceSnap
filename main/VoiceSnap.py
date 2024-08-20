import whisper
import customtkinter
from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

# Função para selecionar o arquivo de áudio
def selecionar_audio():
    return askopenfilename(
        title="Selecione o arquivo de áudio", 
        filetypes=[("Arquivos de áudio", "*.mp3 *.wav *.m4a *.flac *.mp4 *.wmv *.opus")]
    )

# Carrega o modelo Whisper
modelo = whisper.load_model("medium")

# Função principal para transcrever o áudio
def transcrever_audio():
    caminho_audio = selecionar_audio()
    if caminho_audio:
        resposta = modelo.transcribe(caminho_audio)
        transcricao = resposta['text']
        print("Transcrição:", transcricao)
        label.configure(text=transcricao)  # Exibe a transcrição na label

# Função para copiar o texto da label para a área de transferência
def copiar_texto():
    janela.clipboard_clear()  # Limpa o conteúdo da área de transferência
    janela.clipboard_append(label.cget("text"))  # Copia o texto da label
    print("Texto copiado para a área de transferência")

# Funções para mudar a cor da borda quando o mouse interage com os botões
def on_enter1(event):
    button1.configure(border_color="#59f56a")

def on_leave1(event):
    button1.configure(border_color="#696969")

def on_enter2(event):
    button2.configure(border_color="#59f56a")

def on_leave2(event):
    button2.configure(border_color="#696969")

# Configurações da aparência do CustomTkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Configurações da janela principal
janela = CTk()
janela.title("VoiceSnap")
janela.geometry("800x500")
janela.iconbitmap("images/ouvindo.ico")
janela.resizable(False, False)

# Carrega e redimensiona a imagem
img = Image.open("images/HEAD.png")
img_resized = img.resize((400, 400))  # Ajusta as dimensões conforme necessário
img_tk = ImageTk.PhotoImage(img_resized)

# Exibe a imagem redimensionada
label_img = CTkLabel(master=janela, image=img_tk, text='')
label_img.place(x=-25, y=50)

# Criação do frame principal
frame = CTkFrame(master=janela, width=450, height=496, fg_color="#303030", border_color="#59f56a", border_width=2)
frame.pack(side="right")

# Botão para selecionar o arquivo de áudio
button1 = CTkButton(
    master=frame, 
    text="Selecione o arquivo", 
    text_color="#59f56a", 
    fg_color="#696969",
    border_color="#696969", 
    border_width=2, 
    corner_radius=50, 
    command=transcrever_audio,
    hover_color="#696969"  # Mantém a cor original quando clicado
)
button1.place(relx=0.5, rely=0.1, anchor="center")
button1.bind("<Enter>", on_enter1)
button1.bind("<Leave>", on_leave1)

# Botão para copiar o texto transcrito
button2 = CTkButton(
    master=frame, 
    text="Copiar", 
    text_color="#59f56a", 
    fg_color="#696969",
    border_color="#696969", 
    border_width=2, 
    corner_radius=50, 
    command=copiar_texto,
    hover_color="#696969"  # Mantém a cor original quando clicado
)
button2.place(relx=0.5, rely=0.9, anchor="center")
button2.bind("<Enter>", on_enter2)
button2.bind("<Leave>", on_leave2)

# Criação do frame rolável para exibir a transcrição
scroll_frame = CTkScrollableFrame(
    master=frame, 
    fg_color="#969696", 
    scrollbar_button_color="white", 
    width=400, 
    height=300, 
    orientation="vertical"
)
scroll_frame.place(relx=0.5, rely=0.53, anchor="center")

# Label para exibir o texto transcrito
label = CTkLabel(
    master=scroll_frame, 
    text="", 
    text_color="white", 
    width=300, 
    height=300, 
    wraplength=380
)
label.pack(anchor="center", expand=True, pady=10, padx=10)

# Inicia a janela principal
janela.mainloop()
