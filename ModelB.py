from ModelBase import *

class ModelB(ModelBase):
    def __init__(self):
        super().__init__()

    def getModelData(self):
        return "ModelB.data"

    def execute(self):
        print("execute : ModelB / Model Data = " + self.getModelData())
