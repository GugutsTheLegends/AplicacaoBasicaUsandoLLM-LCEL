# AplicacaoBasicaUsandoLLM-LCEL

# Tradução de Texto com LangChain e Groq

Este projeto utiliza a biblioteca LangChain e a API do Groq para traduzir textos automaticamente para diferentes idiomas.

## Tecnologias Utilizadas

- Python
- [LangChain](https://python.langchain.com/)
- [Groq API](https://groq.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Groq:
```env
GROQ_API_KEY=sua-chave-aqui
```

## Uso

Este código carrega variáveis de ambiente, configura um modelo de LLM da Groq e executa um pipeline de tradução.

### Executando a Tradução

1. Execute o script Python:
   ```bash
   python main.py
   ```
2. O resultado será impresso no terminal com a tradução da frase "hello" para alemão.

## Estrutura do Código

- **Carregamento das variáveis de ambiente**: `dotenv` carrega a chave da API.
- **Configuração do modelo Groq**: O modelo `Gemma2-9b-It` é utilizado para tradução.
- **Definição do prompt**: Utiliza `ChatPromptTemplate` para formatar a entrada.
- **Pipeline de processamento**: `prompt | llm | parser` executa a tradução.
- **Execução do teste**: Traduz "hello" para alemão.

## Melhorias Futuras

- Implementar suporte para múltiplos idiomas dinamicamente.
- Adicionar interface de usuário para seleção de idioma.
- Melhorar a engenharia de prompts para maior precisão.

## Licença

Este projeto está licenciado sob a MIT License.
