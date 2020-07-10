undoValue = []
undoAction = []
redoValue = []
redoAction = []

class EventSourcer():

    def __init__(self):
        self.value = 0


    def add(self, num: int):
        self.value += num
        undoValue.append(num)
        undoAction.append('+')

    def subtract(self, num: int):
        self.value -= num
        undoValue.append(num)
        undoAction.append('-')

    def undo(self):
        if len(undoAction) >0:
            if undoAction[-1] == '+':
                self.value -= undoValue[-1]
                temp = undoValue.pop()
                redoValue.append(temp)
                temp= undoAction.pop()
                redoAction.append(temp)

            
            elif undoAction[-1] == '-':
                self.value += undoValue[-1]
                temp = undoValue.pop()
                redoValue.append(temp)
                temp = undoAction.pop()
                redoAction.append(temp)
        else:
            print("undo cannot be done")

    def redo(self):
        if len(redoAction) >0:
            if redoAction[-1] == '+':
                self.value += redoValue[-1]
                temp = redoAction.pop()
                undoAction.append(temp)
                temp = redoValue.pop()
                undoValue.append(temp)

            elif redoAction[-1] == '-':
                self.value -= redoValue[-1]
                temp = redoAction.pop()
                undoAction.append(temp)
                temp = redoValue.pop()
                undoValue.append(temp)
        else:
            print("redo cannot be done")

    def bulk_undo(self, steps: int):
        for i in range(0,steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range(0,steps):
            self.redo()
