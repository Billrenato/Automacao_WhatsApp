import tkinter as tk
from tkinter import filedialog
import requests
import mimetypes


# Função para fazer upload do arquivo e obter o media_id
def upload_arquivo(arquivo_path, access_token, phone_number_id):
    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/media"
    mime_type, _ = mimetypes.guess_type(arquivo_path)

    files = {
        'file': (arquivo_path.split("/")[-1], open(arquivo_path, 'rb'), mime_type)
    }

    data = {
        'messaging_product': 'whatsapp'
    }

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        media_id = response.json()['id']
        return media_id
    else:
        resultado_label.config(text=f"Erro no upload: {response.text}")
        print(response.text)
        return None


# Função para enviar o arquivo via WhatsApp
def enviar_arquivo(arquivo_path, destinatario, access_token, phone_number_id):
    # Primeiro faz upload do arquivo
    media_id = upload_arquivo(arquivo_path, access_token, phone_number_id)

    if not media_id:
        return

    # Envia a mensagem com o documento
    url = f"https://graph.facebook.com/v22.0/{phone_number_id}/messages"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": destinatario,
        "type": "document",
        "document": {
            "id": media_id,
            "filename": arquivo_path.split("/")[-1],
            "caption": "Sua confirmação de pedido (PDF)"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        resultado_label.config(text="Arquivo enviado com sucesso!")
    else:
        resultado_label.config(text="Erro ao enviar arquivo: " + response.text)
        print(response.text)


# Função para selecionar arquivo
def selecionar_arquivo():
    arquivo_path = filedialog.askopenfilename(
        title="Selecione o arquivo",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    arquivo_entry.delete(0, tk.END)
    arquivo_entry.insert(0, arquivo_path)


# Função que executa o envio
def enviar():
    arquivo_path = arquivo_entry.get()
    destinatario = destinatario_entry.get()
    access_token = token_entry.get()
    phone_number_id = phone_id_entry.get()

    if not arquivo_path or not destinatario or not access_token or not phone_number_id:
        resultado_label.config(text="Por favor, preencha todos os campos.")
        return

    enviar_arquivo(arquivo_path, destinatario, access_token, phone_number_id)


# Interface Tkinter
root = tk.Tk()
root.title("Enviar PDF via WhatsApp")

# Linha do arquivo
tk.Label(root, text="Arquivo:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
arquivo_entry = tk.Entry(root, width=50)
arquivo_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Selecionar", command=selecionar_arquivo).grid(row=0, column=2, padx=5, pady=5)

# Linha do destinatário
tk.Label(root, text="Destinatário (ex: 5511999999999):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
destinatario_entry = tk.Entry(root, width=50)
destinatario_entry.grid(row=1, column=1, padx=5, pady=5)

# Linha do Token
tk.Label(root, text="Token de Acesso:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
token_entry = tk.Entry(root, width=50, show="*")
token_entry.grid(row=2, column=1, padx=5, pady=5)

# Linha do Phone Number ID
tk.Label(root, text="Phone Number ID:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
phone_id_entry = tk.Entry(root, width=50)
phone_id_entry.grid(row=3, column=1, padx=5, pady=5)

# Botão enviar
tk.Button(root, text="Enviar", command=enviar).grid(row=4, column=1, pady=10)

# Resultado
resultado_label = tk.Label(root, text="")
resultado_label.grid(row=5, column=1, pady=5)

root.mainloop()