from fastapi import FastAPI 

app = FastAPI()

@app.get('/')

def index():
    return {'data':{
        'name': 'Ayodimeji'
        }
    }  

@app.get('/about') 
def about():
    return {'data': 'about data'}