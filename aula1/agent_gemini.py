from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
load_dotenv()


agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    markdown=True,
)

while True:
    pergunta = input("Digite sua pergunta: ")
    if pergunta.lower() == "sair":
        break
    resposta = agent.run(pergunta)
    print(resposta.content)