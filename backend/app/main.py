from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getHome():
  return {"message": "Dungeons And Dragons"}