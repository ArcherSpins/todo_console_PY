class Todo:
    def __init__(self):
        self.list = []

    def createTask(self, value):
        self.list.append(value)

    def deleteTask(self, idx):
        self.list.remove(self.list[idx - 1])

    def getTasks(self):
        idx = 1
        for i in self.list:
            print(str(idx) + ': ' + i)
            idx += 1

    def getEvents(self):
        print('1: добавить таску (введите 1): ')
        print('2: удалить таску (введите индекс): ')
        print('3: показать таски (введите 3): ')

list = Todo()
list.getTasks()
list.getEvents()


def checkEvent(event):
    if (event == '3'):
        list.getTasks()
    elif (event == '1'):
        event = input('Введите текст таски: ')
        list.createTask(event)
    elif (event == '2'):
        event = int(input('Введите индекс для удаления таски: '))
        list.deleteTask(event)
    eventFunc()

def eventFunc():
    event = input('Введите действие: ')
    checkEvent(event)


eventFunc()

