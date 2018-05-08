from ModelA import *

class ModelC(ModelA):
    def __init__(self):
        super().__init__()

    def execute(self):
        print("execute : ModelC / Model Data = " + self.getModelData())
