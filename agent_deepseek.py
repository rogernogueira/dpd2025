from agno.agent import Agent
from agno.models.deepseek import DeepSeek
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=DeepSeek(id="deepseek-chat" ),
    debug_mode=False,
)
while True:
    pergunta = input("Digite sua pergunta: ")
    if pergunta.lower() == "sair":
        break
    resposta = agent.run(pergunta)
    print(resposta.content)