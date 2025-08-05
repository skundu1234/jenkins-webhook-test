from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Dept(BaseModel):
    id: int
    name: str
    position: str


@app.get("/")
def root_app():
    return {"welcome to demo"}


depts: List[Dept] = []


@app.get("/dept")
def get_dept():
    return depts


@app.post("/dept")
def post_dept(dept: Dept):
    depts.append(dept)
    return dept


@app.put("/dept/{dept_id}")
def put_dept(dept_id: int, updated_dept: Dept):
    for index, emp in enumerate(depts):
        if depts.id == dept_id:
            depts[index] = updated_dept
            return updated_dept
    return {"message": "Dept not found"}


@app.delete("/dept/{dept_id}")
def delete_dept(dept_id: int, updated_dept: Dept):
    for index, emp in enumerate(depts):
        if depts.id == dept_id:
            deleted = depts.pop(index)
            return deleted
    return {"message": "Depts not found"}
