from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
import uuid

app = FastAPI()

class VideoRequest(BaseModel):
    prompt: str

@app.post("/generate-video/")
def generate_video(data: VideoRequest):
    video_id = str(uuid.uuid4())
    return {"status": "processing", "video_id": video_id}
