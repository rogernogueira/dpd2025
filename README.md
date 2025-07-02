# Desenvolvimento de Produto Dados 2025

Este repositório contém exemplos de agentes utilizando a biblioteca `agno`.

## Scripts da pasta `aula1`

Nesta pasta, você encontrará os seguintes scripts:

- `agent_deepseek.py`: Este script utiliza o modelo DeepSeek para criar um agente conversacional.
- `agent_gemini.py`: Este script utiliza o modelo Gemini para criar um agente conversacional.
- `agente_ollama.py`: Este script utiliza um modelo Ollama (qwen3:0.6b) para criar um agente conversacional com uma instrução específica de limite de palavras.

## Como executar os scripts

Para executar qualquer um dos scripts na pasta `aula1`, siga os passos abaixo:

1. Certifique-se de ter as dependências instaladas. Você pode instalá-las utilizando `uv`:
   ```bash
   uv sync
   ```
2. Certifique-se de ter as variáveis de ambiente configuradas no arquivo `.env`, caso necessário para os modelos utilizados.
DEEPSEEK_API_KEY=
GOOGLE_API_KEY=
3. Execute o script desejado utilizando o Python:
   ```bash
   uv run aula1/agent_deepseek.py
   ```
   ou
   ```bash
   uv run aula1/agent_gemini.py
   ```
   ou
   ```bash
   uv run aula1/agente_ollama.py
   ```
4. Digite sua pergunta quando solicitado e pressione Enter. Para sair, digite "sair".
