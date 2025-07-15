from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.yfinance import YFinanceTools
from agno.tools.file import FileTools
from agno.tools.jina import JinaReaderTools

agent = Agent(
    model=Ollama(id="qwen2.5"),
    tools=[YFinanceTools(stock_price=True), FileTools() ],
    debug_mode=True,
    instructions="Use tabelas para mostrar os dados e responda em portugues," \
    "e salve um formato html",
    markdown=True,
)
#agent.print_response("Qual o preço das ações da Apple?", stream=True)


agent_suco = Agent(
    model=Ollama(id="qwen2.5"),
    tools=[JinaReaderTools()],
)
resporta = agent_suco.print_response("summarize: https://docs.agno.com/tools/introduction" \
"")