from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# funcion cek status http
@app.get("/cek-status/{url}")
def cekstatus(url: str):
    data = "https://"+url
    regGet = requests.get(data)
    if regGet.status_code == 200:
        return "Status HTTP " + str(regGet.status_code) + " " + data
    else:
        return {"Status HTTP tidak aman ", regGet.status_code, " ", data}
    
# funcion cek header http
@app.get("/cek-header/{url}")
def cekheader(url: str):
    data = "https://"+url
    try:
        regGet = requests.get(data)
        return str(regGet.headers)
    except requests.exceptions.ConnectionError:
        return {"Mungkin URL yang kamu masukan tidak valid ", data}
    
