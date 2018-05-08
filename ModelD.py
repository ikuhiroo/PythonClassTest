from ModelB import *

class ModelD(ModelB):
    def __init__(self):
        super().__init__()

    def execute(self):
        print("execute : ModelD / Model Data = " + self.getModelData())
