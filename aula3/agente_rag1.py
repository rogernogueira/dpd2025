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
    instructions=""" Você é um assitente juridico que reponde pergurtas com base na sua base conhecimento.
    - Responda as perguntas com base na base de conhecimento
     - Se não souber a resposta, diga que não sabe
    """
)
agent.print_response(" quantos representantes pode ter o campus de gurupi no CPPD?")


