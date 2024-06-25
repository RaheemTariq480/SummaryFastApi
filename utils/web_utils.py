from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str
    is_news: bool
