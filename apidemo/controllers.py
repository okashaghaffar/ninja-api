from ninja import NinjaAPI,Schema
from datetime import date
from django.shortcuts import get_object_or_404
from typing import List,Optional
from django.core.files.storage import FileSystemStorage
from ninja import UploadedFile ,File


from .models import *

api=NinjaAPI()

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None
    first_name: str = None
    last_name: str = None


@api.get("/me", response=UserSchema)
def me(request):
    return request.user

class DepartmentSchema(Schema):
    title: str
    

class UserSchemaAuth(Schema):
    username: str
    email: str
    first_name: str
    last_name: str

class Error(Schema):
    message: str

@api.get("/me/user", response={200: UserSchemaAuth, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user 
#APPLICATION

STORAGE = FileSystemStorage(location='media/uploads')

class EmployeeIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None

class EmployeeOut(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None
    cv: Optional[str]

@api.post("/employees")
def create_employee(request, payload: EmployeeIn,cv:UploadedFile =File(...)):
    employee = Employee.objects.create(**payload.dict())
    employee.cv.save(cv.name,cv)
    return {"id": employee.id}



@api.post("/dept")
def create_department(request, payload: DepartmentSchema):
    dept = Department.objects.create(**payload.dict())
    return {"id": dept.id}

@api.get("/employees/{employee_id}", response=EmployeeOut)
def get_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee

@api.get("/employees", response=List[EmployeeOut])
def list_employees(request):
    qs = Employee.objects.all()
    return qs

@api.put("/employees/{employee_id}")
def update_employee(request, employee_id: int, payload: EmployeeIn):
    employee = get_object_or_404(Employee, id=employee_id)
    for attr, value in payload.dict().items():
        setattr(employee, attr, value)
    employee.save()
    return {"success": True}

@api.delete("/employees/{employee_id}")
def delete_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return {"success": True}


