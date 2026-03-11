from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

from models.refactor_output import RefactorOutput


# Pydantic parser
parser = PydanticOutputParser(
    pydantic_object=RefactorOutput
)


# Strong prompt to FORCE JSON
template = """
You are an expert Python code refactoring agent.

IMPORTANT:

You MUST respond ONLY with valid JSON.

DO NOT explain.

DO NOT write text.

DO NOT write code block.

ONLY JSON.

Format:

{format_instructions}


CODE:
{code}
"""


prompt = PromptTemplate(
    template=template,
    input_variables=["code"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


llm = Ollama(
    model="codellama",
    temperature=0
)


chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True
)
