from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
	return {"message": "TaskFlow API v4"}

@app.get("/hello")
def read_hello():
	return {"message": "Hello, World!"}