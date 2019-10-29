import json
import matplotlib.pyplot as plt
import datetime

def callAPI(fileAPI):
    f = open(fileAPI, 'r')
    data = json.load(f)
    f.close()

    tempo = []
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []

    timeSeries = data['Time Series (Daily)']
    for key, value in timeSeries.items():
        #print(key)
        tempo.append(datetime.datetime.strptime(key, '%Y-%m-%d'))
        opens.append(float(value['1. open']))
        highs.append(float(value['2. high']))
        lows.append(float(value['3. low']))
        closes.append(float(value['4. close']))
        volumes.append(float(value['5. volume']))

    plt.plot(tempo,opens, label='Open')
    plt.plot(tempo,highs, label='High')
    tempo.reverse()
    closes.reverse()
    plt.title(data["Meta Data"]["2. Symbol"])
    plt.plot(tempo,closes, label='Close')
    plt.legend()
