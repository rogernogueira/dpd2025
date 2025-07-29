from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.vectordb.chroma import ChromaDb
from agno.vectordb.lancedb import LanceDb
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.document.chunking.fixed import FixedSizeChunking
from agno.vectordb.search import SearchType

embedder = OllamaEmbedder(id="nomic-embed-text:v1.5",dimensions=768)

vector_store = ChromaDb(
    collection="recipes",
    path="data/chroma",
    embedder=embedder,
)

base_knowledge = PDFKnowledgeBase(
    vector_db=vector_store, 
    path= r'data/pdf/', 
    )

base_knowledge.load(recreate=True)

agent = Agent(
    model=Ollama(id="qwen2.5"),
    debug_mode=True,
    markdown=True,
    knowledge=base_knowledge,
    search_knowledge=True,
    show_tool_calls=True,
    instructions="""
     - Sempre busque (search_knowledge) na base de conhecimento
    - So reponsta com base na base de conhecimento(knowledge)
     - Se não encotrar resposta na base de conhecimento (knowledge), diga que não sabe
     - cheque (search_knowledge) sempre a base de conhecimento (knowledge) antes de responder
    """
)

while True:
    pergunta = input("Digite sua pergunta: ")
    if pergunta.lower() == "sair":
        break
    resposta = agent.run(pergunta)
    print(resposta.content)


