# Importa as bibliotecas necessárias
import tkinter as tk  # Biblioteca para criar interfaces gráficas
from tkinter import filedialog  # Biblioteca para criar diálogos de arquivo
import requests  # Biblioteca para fazer requisições HTTP
import configparser

# Função para enviar o arquivo via WhatsApp
def enviar_arquivo(arquivo_path, destinatario):
    # Define a URL da API do WhatsApp
    api_url = "https://graph.facebook.com/v13.0/messages"
    
    # Define o token de acesso e o ID do número de telefone
    # Lê o arquivo de configuração
    config = configparser.ConfigParser()
    config.read('config.ini')
    access_token = config['WHATSAPP']['access_token']
    phone_number_id = config['WHATSAPP']['phone_number_id']

    

    # Define os cabeçalhos da requisição
    headers = {
        "Authorization": f"Bearer {access_token}",  # Token de acesso
        "Content-Type": "application/pdf"  # Tipo do arquivo
    }

    # Abre o arquivo em modo binário
    files = {
        "file": open(arquivo_path, "rb")
    }

    # Define os dados da requisição
    data = {
        "messaging_product": "whatsapp",  # Produto de mensagens
        "to": destinatario,  # Número do destinatário
        "type": "document",  # Tipo da mensagem
        "document": {
            "filename": arquivo_path.split("/")[-1]  # Nome do arquivo
        }
    }

    # Faz a requisição POST para enviar o arquivo
    response = requests.post(api_url, headers=headers, files=files, data=data)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 201:
        # Atualiza o texto do label com o resultado
        resultado_label.config(text="Arquivo enviado com sucesso!")
    else:
        # Atualiza o texto do label com o erro
        resultado_label.config(text="Erro ao enviar arquivo: " + response.text)
        print(response.text)

# Função para selecionar o arquivo
def selecionar_arquivo():
    # Abre um diálogo para selecionar o arquivo
    arquivo_path = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("Arquivos PDF", "*.pdf")])
    
    # Limpa o campo de texto do arquivo
    arquivo_entry.delete(0, tk.END)
    
    # Insere o caminho do arquivo no campo de texto
    arquivo_entry.insert(0, arquivo_path)

# Função para enviar o arquivo quando o botão é clicado
def enviar():
    # Obtém o caminho do arquivo e o número do destinatário
    arquivo_path = arquivo_entry.get()
    destinatario = destinatario_entry.get()
    
    # Chama a função para enviar o arquivo
    enviar_arquivo(arquivo_path, destinatario)

# Cria a janela principal
root = tk.Tk()
root.title("Enviar arquivo via WhatsApp")

# Cria o label e o campo de texto para o arquivo
arquivo_label = tk.Label(root, text="Arquivo:")
arquivo_label.grid(row=0, column=0, padx=5, pady=5)

arquivo_entry = tk.Entry(root, width=50)
arquivo_entry.grid(row=0, column=1, padx=5, pady=5)

# Cria o botão para selecionar o arquivo
selecionar_button = tk.Button(root, text="Selecionar", command=selecionar_arquivo)
selecionar_button.grid(row=0, column=2, padx=5, pady=5)

# Cria o label e o campo de texto para o destinatário
destinatario_label = tk.Label(root, text="Destinatário:")
destinatario_label.grid(row=1, column=0, padx=5, pady=5)

destinatario_entry = tk.Entry(root, width=50)
destinatario_entry.grid(row=1, column=1, padx=5, pady=5)

# Cria o botão para enviar o arquivo
enviar_button = tk.Button(root, text="Enviar", command=enviar)
enviar_button.grid(row=2, column=1, padx=5, pady=5)

# Cria o label para exibir o resultado
resultado_label = tk.Label(root, text="")
resultado_label.grid(row=3, column=1, padx=5, pady=5)

# Inicia a janela principal
root.mainloop()