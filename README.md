### Curso Técnico de Desenvolvimento de Sistemas - Senai Itapeva
![Imagem de capa](/EstudAI.gif)

**Descrição:**

Esta API RESTFUL, desenvolvida com Flask e integrada ao modelo Gemini da Google, oferece uma solução para a geração automática de listas de exercícios educacionais. A aplicação permite criar listas personalizadas com base em informações fornecidas pelo usuário, como matéria, tema, quantidade de questões e nível de dificuldade. Além disso, implementa validações de conteúdo e formatação padronizada das respostas no formato JSON.

## Índice

* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Endpoints](#endpoints)
* [Configuração da API Gemini](#configuração-da-api-gemini)
* [Instalação](#instalação)
* [Execução](#execução)
* [Autor](#autor)
* [Licença](#licença)

## Funcionalidades

* Geração automática de listas de exercícios personalizadas.
* Personalização por tema, matéria, quantidade de questões e nível de dificuldade.
* Validação de conteúdo impróprio ou incoerente.
* Retorno das listas no formato JSON, incluindo gabarito.
* Comunicação segura com a API Gemini através de variável de ambiente.

## Tecnologias Utilizadas

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![image](https://img.shields.io/badge/Gemini%20API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![image](https://img.shields.io/badge/Flask--CORS-003545?style=for-the-badge)

## Endpoints

* **POST `/estudar`**: Gera uma lista de exercícios personalizada.

    * **Request Body:**
    ```json
    {
      "materia": "Matemática",
      "tema": "Bhaskara",
      "quantidade": 5,
      "dificuldade": "Médio"
    }
    ```

    * **Resposta (200 OK):** Lista de exercícios no formato JSON.
    
    * **Resposta (400 Bad Request):** Caso falte algum dado obrigatório ou JSON inválido.
    ```json
    { "error": "Requisição JSON inválida. Está faltando informações" }
    ```

    * **Resposta (500 Internal Server Error):** Em caso de falha na comunicação com a API ou erro interno.
    ```json
    { "error": "Mensagem de erro" }
    ```

## Configuração da API Gemini

Para utilizar a API, é necessário definir sua chave da API Gemini em uma variável de ambiente no arquivo `.env`:

GOOGLE_API_KEY=SUACHAVEAQUI

Certifique-se de ter configurado sua conta na Google AI Studio e gerado uma chave válida.

## Instalação

1.  Clone este repositório:  
    `git clone <repositório>`
    
2.  Navegue até o diretório do projeto:  
    `cd <diretório>`
    
3.  Instale as dependências:  
    `pip install -r requirements.txt`
    
4.  Crie o arquivo `.env` e adicione sua API key:
    ```
    GOOGLE_API_KEY=SUACHAVEAQUI
    ```

## Execução

Para executar a API, use o comando:  
`python app.py`

A API será executada em modo de debug na porta 5000 (http://localhost:5000).

## Autor

- Richard - https://github.com/Richard15151 - richard.oliveira.senai@gmail.com

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
