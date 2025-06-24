# Imports necessários
from flask import Flask, jsonify, request # Flask, jsonify para formatar resposta, request para acessar dados da requisição
from flask_cors import CORS # Para lidar com Cross-Origin Resource Sharing
from google import genai # Biblioteca para interagir com o modelo Gemini
import os # Módulo para interagir com o sistema operacional (usaremos para variáveis de ambiente)
from dotenv import load_dotenv # Importa a função para carregar .env (se python-dotenv foi instalado)
import json 

# Carrega variáveis de ambiente do arquivo .env (se existir)
# BOA PRÁTICA: Armazenar chaves API em variáveis de ambiente para segurança.
load_dotenv()

# Cria uma instância da aplicação Flask
# '__name__' é um nome especial de variável Python que Flask usa para descobrir a raiz da aplicação
app = Flask(__name__)

# Habilita o CORS para a aplicação inteira
# Isso permitirá que qualquer origem (qualquer domínio/porta) faça requisições ao seu back-end.
# Para produção, você pode querer restringir as origens permitidas.
CORS(app)

#=================================================================
# Passo 3: Configurando a API Key do Gemini
API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY)

#=================================================================
# Passo 4: Definindo o Modelo Gemini
def criar_lista(tema,materia,quantidade,dificuldade):
		# Cria o prompt para a API Gemini, instruindo-a a gerar a lista com base
    # nas informações fornecidas e a formatar a resposta como JSON.
    prompt = f"""
        Você é um assistente de estudos, sua missão é criar uma lista de exercícios baseadas em informações fornecidas pelo estudante.
        Gere uma lista de exercícios sobre o tema: {tema} da materia: {materia}, gere {quantidade} exercícios com nível de dificuldade dificuldade: {dificuldade}.
        Não gere exercícios caso a materia informada não for uma matéria educacional de estudo, como as ensinadas nas escolas.
        Não gere exercícios caso apareçam temas ou matérias imprópias, como conteudo sexual explícito, preconceitos, ódio, assedio, drogas, cigarro, ataque de ódio a uma pessoa ou coisa.
        Não gere exercícios caso apareçam temas e matérias que não se relacionem entre si, exemplo: história e bhaskara
        Nesses casos o título da lista deverá ser "alerta" e uma mensagem de aviso aparecerá na lista, dizendo para o estudante rever as informações e utilizar a plataforma com respeito e responsabilidade.
        A mensagem de aviso, neste caso de "alerta", pode ser colocada no campo "materia" ou como um enunciado no primeiro item do array "exercicios".

        Cada exercício deve possuir um enunciado em um parágrafo curto e ter 4 alternativas de a até d.
        Diversifique as alternativas corretas, para não haver uma sequência grande de mesmas alternativas certas exemplo"b,b,b".
        Preciso que gere as alternativas e forneça o gabarito com as respostas certas dos exercícios no final da lista, apenas o corpo da resposta, não traga a alternativa pois já está colocada no front-end
        Certifique-se que o campo "resposta_correta" dentro de cada exercício e o campo "gabarito" global sejam consistentes e se refiram ao texto da alternativa correta.
        
        Devolva no formato JSON se acordo com o modelo de exemplo:
        {{
        "titulo": "Lista de Bhaskara",
        "materia": "Matemática",
        "tema": "Bhaskara",
        "quantidade": 5,
        "exercicios": [
            {{
            "numero": 1,
            "enunciado": "Enunciado do exercício 1",
            "alternativas": [
                "alternativa_a",
                "alternativa_b",
                "alternativa_c",
                "alternativa_d"
            ],
            "resposta_correta": "alternativa_a"
            }},
            {{
            "numero": 2,
            "enunciado": "Enunciado do exercício 2",
            "alternativas": [
                "alternativa_a",
                "alternativa_b",
                "alternativa_c",
                "alternativa_d"
            ],
            "resposta_correta": "alternativa_b"
            }},
            {{
            "numero": 3,
            "enunciado": "Enunciado do exercício 3",
            "alternativas": [
                "alternativa_a",
                "alternativa_b",
                "alternativa_c",
                "alternativa_d"
            ],
            "resposta_correta": "alternativa_c"
            }},
            {{
            "numero": 4,
            "enunciado": "Enunciado do exercício 4",
            "alternativas": [
                "alternativa_a",
                "alternativa_b",
                "alternativa_c",
                "alternativa_d"
            ],
            "resposta_correta": "alternativa_d"
            }},
            {{
            "numero": 5,
            "enunciado": "Enunciado do exercício 5",
            "alternativas": [
                "alternativa_a",
                "alternativa_b",
                "alternativa_c",
                "alternativa_d"
            ],
            "resposta_correta": "alternativa_a"
            }}
        ],
        "gabarito": {{
        "1": "alternativa_b",
        "2": "alternativa_b",
        "3": "alternativa_c",
        "4": "alternativa_b",
        "5": "alternativa_b"
        }}
        }}
        """
		# Envia a requisição para a API Gemini para gerar a lista.
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
        "response_mime_type": "application/json",
        }
    )
    
    # Tenta decodificar a resposta da API Gemini como JSON.
    response = json.loads(response.text)
    return response
#=========================================================
# Passo 5: Criando a Rota da API (função completa agora)
@app.route('/estudar', methods=['POST'])
def make_exercicios():
    try:
        # Tenta obter os dados da requisição como JSON.
        dados = request.get_json()

        # Valida se a requisição contém um JSON válido.
        if not dados or not isinstance(dados, dict):
            return jsonify({'error': 'Requisição JSON inválida. Esperava um dicionário.'}), 400

        # Obtém as informações do JSON.
        materia = dados.get('materia')
        tema = dados.get('tema')
        quantidade = dados.get('quantidade')
        dificuldade = dados.get('dificuldade')


        # Valida se tem todas as informações (materia, tema, quantidade, dificuldade)
        if not materia or not tema or not quantidade or not dificuldade:
            return jsonify({'error':'Requisição JSON inválida. Está faltando informações'}), 400

        # Chama a função criar_lista para gerar a lista com base nos ingredientes.
        response = criar_lista(materia, tema, quantidade, dificuldade)

        # Retorna a lista como JSON com o código de status 200 (OK).
        return jsonify(response), 200

    except Exception as e:
        # Se ocorrer algum erro durante o processo, imprime o erro no console
        # e retorna um JSON com a mensagem de erro e o código de status 500
        # (Internal Server Error).
        print(f"Um erro interno ocorreu na API: {e}")
        return jsonify({'error': str(e)}), 500  # Retorna código 500 para erros internos

if __name__ == '__main__':
    app.run(debug=True)