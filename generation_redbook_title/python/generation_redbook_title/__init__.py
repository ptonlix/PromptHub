from generation_redbook_title.prompt import RedbookTitlePrompt, PROMPT_TEMP

PROMPT = RedbookTitlePrompt(input_variables=["keywords", "theme"], template=PROMPT_TEMP)

__all__ = ["PROMPT"]
