import json
# 写入 JSON 数据

 
# 读取数据
preload = []
with open('config.json', 'r') as f:
    data = json.load(f)

print(data["color-scheme"])

#print(preload)
