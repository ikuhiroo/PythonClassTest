# クラスの継承のサンプル  

`$ python main.py `  
それぞれの ModelA ～ ModelD までの execute() を実行    
ModelBaseにある getModelData(), execute() を実装しない場合は Exception を投げる  

## コメントアウトなし  
>execute : ModelA / Model Data = ModelA.data  
execute : ModelB / Model Data = ModelB.data  
execute : ModelC / Model Data = ModelA.data  
execute : ModelD / Model Data = ModelB.data  

## ModelA の getModelData() をコメントアウト  
>Exception: getModelData impl error  

## ModelA の execute() をコメントアウト  
>Exception: execute impl error  
