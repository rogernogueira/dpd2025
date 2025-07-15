from agno.agent import Agent
from agno.models.ollama import Ollama
from datetime import datetime
from agno.tools import tool
from agno.tools.googlesearch import GoogleSearchTools
import json
from pydantic import BaseModel, Field
import requests
import bs4

class TaxaResponse(BaseModel):
    taxa: float = Field(..., description="Taxa de exportação para os EUA a partir de 1 de agosto de 2025")


@tool(show_result=True, stop_after_tool_call=True)
def get_date_now():
    """ função que retorna a data atual no formato dd/mm/yyyy
        Args:
            None
        Returns:
            str: data atual no formato dd/mm/yyyy
    """
    return datetime.now().strftime("%d/%m/%Y")

agent = Agent( model=Ollama(id="qwen2.5"), 
             debug_mode=False,
             markdown=True,
             tools=[get_date_now, 
                    GoogleSearchTools()
                    ],
             show_tool_calls=True, 
             
             instructions=""" siga as instruções abaixo:
              - o texto de deve conter no máximo 100 palavras em texto sem formatação
              - Quando peguntar a data atual, use a ferramenta get_date_now
                    - não crie uma data
                    - A data dever ser retornada no formato dd/mm/yyyy 
                    - Certifique que a resposta está no formato Dia/Mês/Ano 
              - buscar informações na internet use a ferramenta GoogleSearchTools
              """
             )

agent2 = Agent( model=Ollama(id="qwen3:0.6b"), 
             debug_mode=False,
             markdown=False,
             use_json_mode=True,
             show_tool_calls=True, 
             response_model=TaxaResponse,   
             instructions=""" 
             siga as instruções abaixo:
              - Com base no  texto extraia o valor numerico da taxa
              - Retorne o valor json com a chave "taxa" e o valor numérico
              """
             )
resposta  = agent.run('busque na internet qual será a taxa de exportaçao para EUA, aparti de 1 de agosto de 2025?')
valor_taxa = agent2.run(resposta.content)
print(valor_taxa.content.taxa)

html = requests.get('https://br.investing.com/commodities/orange-juice')
soap  = bs4.BeautifulSoup(html.text, 'html.parser')
suco = soap.find('div', {'data-test': "instrument-price-last"}).text
suco= float(suco.replace(',', '.'))
suco_eua = ((valor_taxa.content.taxa)/100 * suco)+ suco
print(f"Valor do suco exportado para os EUA: {suco_eua:.2f} reais")



