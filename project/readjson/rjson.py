import json

with open('static/Cars.json', 'r') as carfile:
    datas = json.load(carfile)
    
    # for data in datas :
    #     print(data)