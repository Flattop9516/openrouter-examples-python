from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from os import getenv
from dotenv import load_dotenv

load_dotenv()

template = """Question: {question}

Answer: Let's think step by step."""
#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

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI(
    openai_api_key=getenv("OPENROUTER_API_KEY"),
    openai_api_base=getenv("OPENROUTER_BASE_URL"),
    model_kwargs={
        "headers": {
            "HTTP-Referer": getenv("APP_URL"),
            "X-Title": getenv("APP_TITLE"),
        }
    },
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

print(llm_chain.run(question))
