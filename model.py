from pathlib import Path
import re
import json


class Employee:
    last_id = 0
    
    def __init__(self,surname: str,name: str,post: str,pay: float) -> None:
        self._surname=surname
        self._name=name
        self._post=post
        self._pay=pay
        Employee.last_id+=1
        self._id=Employee.last_id

    def __str__(self) -> str:
        return f"{self._id} {self._surname} {self._name} {self._post} {self._pay}"
    
    def to_dict(self)-> dict:
        return {'surname': self._surname,'name': self._name,'post': self._post,'pay': self._pay}
    
    def surname(self) -> str:
        return self._surname

    def name(self) -> str:
        return self._name

    def post(self) -> str:
        return self._post

    def pay(self) -> float:
        return self._pay

    def id(self) -> int:
        return self._id
    
    def edit(self,surname: str=None,name: str=None,post: str=None,pay: float=None) -> None:
        if surname is not None:
            self._surname=surname
        if name is not None:
            self._name=name
        if post is not None:
            self._post=post
        if pay is not None:
            self._pay=pay
    
    def is_valid(self)->bool:
        if re.fullmatch(r'^\w+$',self._surname) is None:
            return False
        if re.fullmatch(r'^\w+$',self._name) is None:
            return False
        if re.fullmatch(r'^\w+$',self._post) is None:
            return False
        if self._pay < 0:
            return False
        return True


class Staff:
    def __init__(self) -> None:
        self._staff=[]
        self._load()

    def add_employee(self,employee: Employee,save=True) -> None:
        if not employee.is_valid():
            raise ValueError
        self._staff.append(employee)
        if save:
            self._save()

    def search_employee(self,surname: str=None,name: str=None) -> list[Employee]:
        return [i for i in self._staff if (i.surname()==surname or surname is None) and (i.name()==name or name is None)]
    
    def search_by_post(self,post: str) -> list[Employee]:
        return [i for i in self._staff if i.post()==post]
    
    def search_by_pay(self,pay_min: float,pay_max: float) -> list[Employee]:
        return [i for i in self._staff if i.pay()>=pay_min and i.pay()<=pay_max]
    
    def del_employee(self,id: int) -> None:
        del self._staff[self._index_by_id(id)]
        self._save()
    
    def edit_employee(self,id: int,surname: str=None,name: str=None,post: str=None,pay: float=None) -> None:
        employee=self._staff[self._index_by_id(id)]
        employee.edit(surname,name,post,pay)
        if not employee.is_valid():
            raise ValueError
        self._save()
    
    def export_to_json(self,file: Path) -> None:
        file.write_text(json.dumps([i.to_dict() for i in self._staff]),'utf-8')

    def export_to_csv(self,file: Path) -> None:
        file.write_text('\n'.join([f"{i.surname()};{i.name()};{i.post()};{i.pay()}" for i in self._staff]),'utf-8')

    
    def _save(self) -> None:
        Path("staff.csv").write_text('\n'.join([f"{i.surname()};{i.name()};{i.post()};{i.pay()}" for i in self._staff]),'utf-8')

    def _load(self) -> None:
        for i in Path("staff.csv").read_text('utf-8').split('\n'):
            employee=[c for c in i.split(';')]
            if len(employee) != 4: continue
            self.add_employee(Employee(employee[0],employee[1],employee[2],float(employee[3])),False)
    
    def _index_by_id(self,id: int) -> int:
        index=[i[0] for i in enumerate(self._staff) if i[1].id()==id]
        if len(index) != 1:
            raise ValueError
        return index[0]