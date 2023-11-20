 #uvicorn main:app --reload --port 5000
from fastapi import Request, FastAPI
from bs4 import BeautifulSoup
import requests
from preprocess import preprocessing


appp = FastAPI()

@appp.post("/json")

async def get_body(request: Request):
    return await request.body()
#uvicorn main:app --reload
#@appp.get("/{user_id}")
@appp.get("/")
#def read_user(user_id: str):
#    return {"user_idNEWAPI2": user_id}
def read_user(url: str):
    filtereded_titles = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    titles = soup.findAll('span')
    #titles=(' '.join(titles))
    for data in titles:
        filtereded_titles.append(data.text)
        #filtereded_titles=titles
    #filtereded_titles=titles
    return{"txt":filtereded_titles}
    #return{"txt":titles}
#uvicorn main:app --reload --port 5000