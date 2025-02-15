from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : 'Lists'}

@app.get('/about/{id}')
def about(id : int):
    return {'data':id}

@app.get('/about/{id}/comments')
def about_comments(id):
    return {'data' : {'1','2'}}