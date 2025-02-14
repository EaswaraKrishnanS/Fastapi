from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data' : {'Name' : 'Sarath','ID':'2981','Location':'Bangalore'}}

@app.get('/about')
def about():
    return {'data':'About Page'}