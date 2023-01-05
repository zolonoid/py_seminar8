import cmd
from controller import Controller

class StaffShell(cmd.Cmd):
    intro = 'Введите help или ? для получения перечня команд.\n'
    prompt = 'Сотрудники >>> '

    def __init__(self,controller: Controller):
        super().__init__()
        self._controller=controller

    def do_search(self,arg):
        'Найти сотрудника:  search [-surname Фамилия] [-name Имя]'
        print('\n'.join(self._controller.search_employee(arg)))

    def do_bypost(self,arg):
        'Сделать выборку по должности:  bypost Должность'
        print('\n'.join(self._controller.search_by_post(arg)))

    def do_bypay(self,arg):
        'Сделать выборку по зарплате:  bypay Минимум Максимум'
        print('\n'.join(self._controller.search_by_pay(arg)))
    
    def do_add(self,arg):
        'Добавить сотрудника:  add Фамилия Имя Должность Зарплата'
        self._controller.add_employee(arg)

    def do_del(self,arg):
        'Удалить сотрудника:  del ID'
        self._controller.del_employee(arg)

    def do_edit(self,arg):
        'Обновить данные сотрудника:  edit ID [-surname Фамилия] [-name Имя] [-post Должность] [-pay Зарплата]'
        self._controller.edit_employee(arg)


    def do_tojson(self,arg):
        'Экспортировать данные в формате json:  tojson Файл'
        self._controller.export_to_json(arg)

    def do_tocsv(self,arg):
        'Экспортировать данные в формате csv:  tocsv Файл'
        self._controller.export_to_csv(arg)