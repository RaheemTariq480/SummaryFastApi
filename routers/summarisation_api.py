from fastapi import APIRouter
from utils.web_utils import SummarizationRequest
from utils.ai_utils import models
import time 

summary_app = APIRouter()




@summary_app.post("/summarize/")
async def summarize_text(request: SummarizationRequest):
    if request.is_news:
        start_time = time.time()
        summary = models.infer(request.text)
        end_time = time.time()
        print("Time taken: {} seconds".format(end_time - start_time))
        return {"summary": summary}
    else:
        return {"message": "It is not a news."}
