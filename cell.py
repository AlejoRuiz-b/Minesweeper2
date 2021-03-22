class Cell (object):
    def __init__(self, positiony, positionx, value, reveled):
        self.positiony = positiony
        self.positionx = positionx
        self.value = value
        self.reveled = reveled

    def getPosition(self):
        return print(self.positiony, self.positionx)

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value

    def setReveled(self,reveled):
        self.reveled = reveled

    def reveledCell(self,show):
        self.reveled = show
        print(self.value)
        '''if(self.reveled == True):
            print(self.value)'''




