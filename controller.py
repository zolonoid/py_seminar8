from model import Employee, Staff
from pathlib import Path

class Controller:
    def __init__(self,staff: Staff) -> None:
        self._staff=staff

    def add_employee(self,employee: str)->None:
        s=employee.split()
        if len(s) != 4:
            raise ValueError
        pay=round(float(s[3].replace(',','.')),2)
        self._staff.add_employee(Employee(s[0],s[1],s[2],pay))

    def search_employee(self,employee: str) -> list[str]:
        surname=self._param_value(employee,'-surname')
        name=self._param_value(employee,'-name')
        return [str(i) for i in self._staff.search_employee(surname,name)]
    
    def search_by_post(self,post: str) -> list[str]:
        return [str(i) for i in self._staff.search_by_post(post)]

    def search_by_pay(self,pay: str) -> list[str]:
        minmax=pay.replace(',','.').split()
        if len(minmax) != 2:
            raise ValueError
        return [str(i) for i in self._staff.search_by_pay(float(minmax[0]),float(minmax[1]))]
    
    def del_employee(self,id: str) -> None:
        self._staff.del_employee(int(id))
    
    def edit_employee(self,id: str,edit: str) -> None:
        surname=self._param_value(edit,'-surname')
        name=self._param_value(edit,'-name')
        post=self._param_value(edit,'-post')
        pay=self._param_value(edit,'-pay')
        fpay=float(pay.replace(',','.')) if pay is not None else None
        self._staff.edit_employee(int(id),surname,name,post,fpay)

    def export_to_json(self,file: str) -> None:
        self._staff.export_to_json(Path(file))

    def export_to_csv(self,file: str) -> None:
        self._staff.export_to_csv(Path(file))

    def _param_value(self,line: str, param: str) -> str:
        try:
            s=line.split()
            i=s.index(param)
            return s[i+1]
        except:
            return None
