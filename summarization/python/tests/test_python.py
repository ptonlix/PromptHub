from langchain import OpenAI
from langchain.chains import LLMChain

def test_prompt():
    # 使用api2d访问openai
    OpenAI.openai_api_base = "https://oa.api2d.net"

    ai = OpenAI()
    ai.openai_api_base = "https://oa.api2d.net/v1" 

    from summarization import PROMPT

    chain = LLMChain(llm=ai, prompt=PROMPT)

    doc="""
    Feature stores are a concept from traditional machine learning that make sure data fed into models is up-to-date and relevant. For more on this, see here.

    This concept is extremely relevant when considering putting LLM applications in production. In order to personalize LLM applications, you may want to combine LLMs with up-to-date information about particular users. Feature stores can be a great way to keep that data fresh, and LangChain provides an easy way to combine that data with LLMs.

    In this notebook we will show how to connect prompt templates to feature stores. The basic idea is to call a feature store from inside a prompt template to retrieve values that are then formatted into the prompt.
    """
    print(chain.run(documents=doc, require=["字数限定在30个字左右"]))