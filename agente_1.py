from agno.agent import Agent
from agno.models.ollama import Ollama
agent = Agent( model=Ollama(id="qwen3:0.6b"), 
             debug_mode=False,
             markdown=False,
             instructions=" o texto de deve conter no máximo 100 palavras em texto sem formatação"
             )
while True:
    pergunta = input("Digite sua pergunta: ")
    if pergunta.lower() == "sair":
        break
    resposta = agent.run(pergunta)
    print(resposta.content)