import json

f = open('apiAlpha.json', 'r')
data = json.load(f)
f.close()

timeSeries = data['Time Series (5min)']
for key, value in timeSeries.items():
    for inner_key, inner_value in value.items():
        print(key)
        print(value['1. open'])
