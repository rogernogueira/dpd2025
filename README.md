# Desenvolvimento de Produto de Dados 2025

Este repositório contém exemplos de agentes utilizando a biblioteca `agno`.

## Scripts da pasta `aula1`

Nesta pasta, você encontrará os seguintes scripts:

- `agent_deepseek.py`: Este script utiliza o modelo DeepSeek para criar um agente conversacional.
- `agent_gemini.py`: Este script utiliza o modelo Gemini para criar um agente conversacional.
- `agente_ollama.py`: Este script utiliza um modelo Ollama (qwen3:0.6b) para criar um agente conversacional com uma instrução específica de limite de palavras.

## Instalação do uv (Windows)

Para instalar o `uv` no Windows, powershell ou Prompt de comando:

1. Digite:
   ```bash
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   ```

## Como executar os scripts

Para executar qualquer um dos scripts na pasta `aula1`, siga os passos abaixo:

1. Certifique-se de ter as dependências instaladas. Você pode instalá-las utilizando `uv`:
   ```bash
   uv sync
   ```
2. Certifique-se de ter as variáveis de ambiente configuradas no arquivo `.env`, caso necessário para os modelos utilizados.
 ```bash
   DEEPSEEK_API_KEY=chava_da_api_deepseek
   GOOGLE_API_KEY=chava_da_api_studio_ia_google
 ```


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
