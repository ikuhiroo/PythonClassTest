from ModelBase import *

class ModelA(ModelBase):
    def __init__(self):
        super().__init__()

    def getModelData(self):
        return "ModelA.data"

    def execute(self):
        print("execute : ModelA / Model Data = " + self.getModelData())
