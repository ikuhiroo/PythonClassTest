class ModelBase:

    def __init__(self):
        print('親クラスのinit')
        pass

    def getModelData(self):
        raise Exception("getModelData impl error")

    def execute(self):
        raise Exception("execute impl error")
