from summarization.prompt import SummarizationPromptTemplate

PROMPT = SummarizationPromptTemplate(input_variables=["documents", "require"])

__all__ = [
    SummarizationPromptTemplate,
    PROMPT
]