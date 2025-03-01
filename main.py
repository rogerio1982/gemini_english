from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configuração da API do Gemini
genai.configure(api_key='')

# Inicializando o modelo
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_treino', methods=['POST'])
def gerar_treino():
    nivel = request.form.get('nivel', 'iniciante')
    objetivo = request.form.get('objetivo', 'geral')

    prompt = f"Crie três frases em inglês de {nivel}, usadas em {objetivo}. Mostre a tradução."
    try:
        response = model.generate_content(prompt)
        treino = response.text

        return render_template('index.html', treino=treino)
    except Exception as e:
        return render_template('index.html', treino=f'Erro: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)
