from transformers import pipeline
from utils.configs import args
from concurrent.futures import ThreadPoolExecutor, as_completed

class Models(object):
    def __init__(self):
        self.model = None
        self._load_model()
    def _load_model(self):
        self.model = pipeline("summarization", model="philschmid/bart-large-cnn-samsum", max_length=args.max_length)
        print("models initialized")
    def _pre_process(self, text, max_chunk_length=500):
        chunks = []
        words = text.split()
        current_chunk = ''
        print("length of text(characters)", len(text))
        for word in words:
            if len(current_chunk) + len(word) <= max_chunk_length:
                current_chunk += ' ' + word
            else:
                chunks.append(current_chunk.strip())
                current_chunk = word
        if current_chunk:
            chunks.append(current_chunk.strip())
        return chunks
    def infer(self, text):
        if not text.strip():  # Check if text empty
            return "Please enter some text."
        if len(text)>args.chunk_size:
            summary = ""
            for chunk in self._pre_process(text):
                summary += self.model(chunk)[0]["summary_text"]
            return summary
        else:
            try:
                return self.model(text)[0]["summary_text"]
            except Exception as e:
                return "Something went wrong:" + e 
    


models = Models()
