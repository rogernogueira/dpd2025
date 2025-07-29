from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.vectordb.chroma import ChromaDb
from agno.vectordb.lancedb import LanceDb
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.document.chunking.fixed import FixedSizeChunking
from agno.vectordb.search import SearchType
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb

embedder = OllamaEmbedder(id="nomic-embed-text:v1.5",dimensions=768)

vector_store = ChromaDb(
    collection="recipes",
    path="data/chroma",
    embedder=embedder,
)
memory  = Memory(
    model=Ollama(id="qwen2.5"),
    db=SqliteMemoryDb(
        table_name="memory",
        db_file="data/db/memory.db",
    )
)

base_knowledge = PDFKnowledgeBase(
    vector_db=vector_store, 
    path= r'data/pdf/', 
    )

sqlite_storage = SqliteStorage(
    db_file="data/db/doc_analizer.db",
    table_name="agent_sessions",
)


base_knowledge.load(recreate=True)

agent = Agent(
    name = "DocAnalizer",
    model=Ollama(id="qwen2.5"),
    session_id= "doc_analizer",
    user_id="roger",
    #num_history_sessions=3,
    #read_chat_history=True,
    #add_history_to_messages=True,
    debug_mode=True,
    markdown=True,
    knowledge=base_knowledge,
    search_knowledge=True,
    show_tool_calls=True,
    storage=sqlite_storage,
    memory=memory,
    enable_agentic_memory=True,

    instructions="""
     - Sempre busque usando a ferramenta 'search_knowledge' para acessar 'knowledge'
     - Se não encotrar resposta 'knowledge', diga que não sabe
     - para todas as perguntas use a 'search_knowledge
    """
)

#agent.print_response(" Onde posso salvar foto e videos do meu celular?")
playgd = Playground( agents=[agent] )
app = playgd.get_app()

if __name__ == "__main__":
    playgd.serve("playground:app", reload=True)
