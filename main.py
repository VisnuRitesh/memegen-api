import base64

from enum import Enum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from memegen import Memegen
from memegen.meme_template import MemeTemplate


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://0.0.0.0:8080"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/meme/{template_id}")
async def root(template_id: MemeTemplate):
    generator = Memegen(template=MemeTemplate.DRAKE)
    meme, top, bottom = generator.predict()

    return {
        "top": top,
        "bottom": bottom,
        "image": base64.b64encode(meme)
    }
