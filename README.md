
# Envio de Arquivos PDF via WhatsApp (Tkinter + Meta Graph API)

Este projeto é uma aplicação desktop desenvolvida em Python para **envio automatizado de arquivos PDF** diretamente para contatos do WhatsApp, utilizando a **WhatsApp Cloud API** (Meta Graph API).

A solução oferece uma forma eficiente e direta para autônomos, empresas ou sistemas que precisam automatizar o envio de documentos, como notas fiscais, comprovantes, relatórios ou boletos, sem depender de plataformas de terceiros.

## Descrição do Projeto

O programa possui uma **interface gráfica simples e intuitiva**, construída com **Tkinter**, que facilita:
1. O upload e a seleção do documento PDF.
2. A configuração e o armazenamento seguro do token de acesso e do Phone Number ID da API.
3. O envio rápido da mensagem para qualquer número de telefone via WhatsApp.

## Funcionalidades Principais

* **Upload de arquivos PDF** para o servidor do WhatsApp Cloud API.
* Envio de documentos a destinatários individuais via mensagem de tipo `document`.
* Interface gráfica amigável e de fácil utilização (**Tkinter**).
* Armazenamento local e seguro de credenciais sensíveis (Token e Phone Number ID) no arquivo `config.json`.
* Opção para mostrar ou ocultar as configurações sensíveis da API na interface.
* Exibição de mensagens de status em tempo real durante o envio (sucesso ou erro).

## Estrutura do Projeto

whatsapp-pdf-sender/
│
├── main.py                 # Código principal com interface Tkinter e integração API
├── config.json             # Arquivo de configuração (token e phone_id)
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto (este arquivo)
└── assets/                 # (opcional) diretório para ícones ou PDFs de teste

## Pré-requisitos

Para executar este projeto, você precisa ter:

1. **Python 3.8+** instalado.
2. Uma conta configurada no [Meta for Developers](https://developers.facebook.com/) com acesso à **WhatsApp Cloud API**.
3. Um **Token de Acesso Permanente** e um **Phone Number ID** válidos da sua aplicação Meta.

## Instalação

Siga os passos abaixo para configurar e rodar o projeto em sua máquina:

1. **Clone o repositório:**
    ```bash
    git clone [https://github.com/seuusuario/whatsapp-pdf-sender.git](https://github.com/seuusuario/whatsapp-pdf-sender.git)
    cd whatsapp-pdf-sender
    ```

2. **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # Linux/Mac
    source venv/bin/activate   
    # Windows
    venv\Scripts\activate      
    ```

3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o arquivo `config.json`:**
    Crie (ou edite) o arquivo de configuração `config.json` na raiz do projeto, substituindo os placeholders:

    ```json
    {
        "token": "SEU_TOKEN_DE_ACESSO",
        "phone_id": "SEU_PHONE_NUMBER_ID"
    }
    ```

## Como Usar

1. **Execute o programa:**
    ```bash
    python main.py
    ```

2. **Selecione o arquivo PDF** que deseja enviar através do botão de seleção.

3. **Informe o número do destinatário** no formato internacional, sem sinais, espaços ou prefixo `+`.
    > Exemplo: `5511999999999` (Brasil, DDD 11).

4. (Opcional) Clique em **"Mostrar Configurações"** para ajustar ou salvar o token e o `phone_id` diretamente na interface.

5. Clique em **"Enviar"** e aguarde a mensagem de confirmação de status.

### Exemplo de Fluxo (Backend)

1. O usuário seleciona o arquivo PDF.
2. O programa realiza o **upload** do arquivo para o Meta Graph API e obtém um `media_id`.
3. O `media_id` é utilizado para enviar a mensagem do tipo `document` via endpoint:
    `https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages`
4. O destinatário recebe o PDF no WhatsApp.

## Dependências

As principais bibliotecas utilizadas neste projeto:

| Biblioteca | Descrição |
| :--- | :--- |
| `tkinter` | Interface gráfica nativa do Python. |
| `requests` | Comunicação HTTP robusta com a API do WhatsApp. |
| `mimetypes` | Detecção automática do tipo MIME do arquivo (necessário para upload). |
| `json` | Manipulação do arquivo de configuração local (`config.json`). |
| `os` | Operações de sistema de arquivos e caminhos. |

O arquivo `requirements.txt` deve conter:

requests>=2.31.0

## Considerações de Segurança

* **Não exponha seu token de acesso** público em repositórios abertos ou arquivos compartilhados.
* O token e o número de telefone da API são armazenados de forma **local e segura** no arquivo `config.json`.
* Recomenda-se o uso de **Tokens de Acesso Permanente** apenas em ambientes de produção.

## Possíveis Erros Comuns

| Erro Exibido | Causa Provável | Solução |
| :--- | :--- | :--- |
| Erro no upload: (#200) | Token inválido ou sem permissão de acesso. | Verifique se o token é válido e se ele tem as permissões necessárias para o número configurado. |
| Por favor, preencha todos os campos. | Campos obrigatórios (Destinatário, Token ou Phone ID) vazios. | Preencha todos os campos da interface antes de iniciar o envio. |
| Erro ao enviar arquivo | `media_id` inválido ou expirado. | Tente reenviar o arquivo. Se persistir, verifique a validade do seu token. |

## Licença

Este projeto é distribuído sob a **Licença MIT**.
