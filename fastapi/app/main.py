from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.get("/test")
def test():
    return {"message": "test"}

