from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import google.generativeai as genai
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI()

# Serve the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_index():
    return FileResponse("static/index.html")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text_data = contents.decode("utf-8")
        
        # Load text into LangChain
        loader = TextLoader(text_data)
        docs = loader.load()
        
        # Use Gemini AI to extract topics
        model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        prompt = "Extract key topics from this text: " + text_data
        response = model.predict(prompt)
        
        return {"topics": response}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
