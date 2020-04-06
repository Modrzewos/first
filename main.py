from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict


class Patient(BaseModel):
    name: str
    surename: str


app = FastAPI()
app.counter: int = 0
app.storage: Dict[int, Patient] = {}


@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}


@app.api_route(path="/method", methods={"GET", "POST", "DELETE", "PUT", "OPTIONS"})
def read_request(request: Request):
    return {"method": request.method}


@app.post("/patient")
def show_data(patient: Patient):
    resp = {"id": app.counter, "patient": patient}
    app.storage[app.counter] = Patient
    app.counter += 1
    return resp


@app.get("/patient/{pk}")
def show_patient(pk: int):
    if pk in app.storage:
        return app.storage.get(pk)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# def counter():
#     app.counter += 1
#     return str(app.counter)
#
# @app.get("/hello/{name}", response_model = HelloResp)
# async def read_item(name: str):
#     return HelloResp(msg=f"Hello {name}")
#
# class GiveMeSomethingRq(BaseModel):
#     first_key: str
#
#
# class GiveMeSomethingResp(BaseModel):
#     received: dict
#     constant_data: str = "python jest super"
#
#
# @app.post("/dej/mi/coś", response_model=GiveMeSomethingResp)
# def receive_something(rq: GiveMeSomethingRq):
#     return GiveMeSomethingResp(received=rq.dict())
