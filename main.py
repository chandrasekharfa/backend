from fastapi import FastAPI


app = FastAPI()
@app.get('/')
def index():
    return {'hello': {'stu': 'chandu'}}

@app.get('/about')
def about():
    return {'about': {'stu': 'chandu'}}