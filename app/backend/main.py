from fastapi import FastAPI
import uvicorn
from classes.driver import DriverOperations
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
from classes.school import SchoolOperations
app = FastAPI()

# origins = [
#     "http://localhost:3000",
#     "http://localhost:8000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     #allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

class SearchInfo(BaseModel):
    type_school: str
    number_schools: int
@app.post("/")
async def home():
    return {"status": "sucessful"}
@app.post("/receber-opcao")
async def executar_back(search_info: SearchInfo): 
    driver_chrome = DriverOperations()
    driver_chrome.start_driver()

    school = SchoolOperations(driver_chrome.driver)
    school.search_school(search_info.number_schools,search_info.type_school)
    return {"message": "Ação executada com sucesso"}

@app.get("/download-file")
async def return_file():
    return FileResponse("US_Schools.csv")
    
if __name__== "main":    
    uvicorn.run("main:app", host="0.0.0.0", reload= True, port=8000)  
