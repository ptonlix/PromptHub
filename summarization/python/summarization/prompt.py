from langchain.prompts import StringPromptTemplate
from pydantic import BaseModel, validator

PROMPT = """\
总结以下文档内容：
```
{documents}
```
要求：
```
{require}
```
总结内容：
"""


class SummarizationPromptTemplate(StringPromptTemplate, BaseModel):
    @validator("input_variables")
    def validate_input_variables(cls, v):
        """Validate that the input variables are correct."""
        if len(v) != 2 or "documents" not in v or "require" not in v:
            raise ValueError("documents and require must be the only input_variable.")
        return v

    def format(self, **kwargs) -> str:
        prompt = PROMPT.format(documents=kwargs["documents"], require=kwargs["require"])
        return prompt

    def _prompt_type(self):
        return "summarization-documents"


if __name__ == "__main__":
    docstr = "Let's suppose we want the LLM to generate English language explanations of \
a function given its name. To achieve this task, we will create a custom prompt template that \
takes in the function name as input, and formats the prompt template to provide the source code of the function."
    summarize_prompt = SummarizationPromptTemplate(
        input_variables=["documents", "require"]
    )
    # prompt = summarize_prompt.format(documents=docstr, require=None)
    prompt = summarize_prompt.format(documents=docstr, require=["字数在十五个字", "言简意赅"])

    print(prompt)
