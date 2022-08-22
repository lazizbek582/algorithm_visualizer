import time


def bubbleSort(data, drawData, timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ["red" if x == j or x == j+1 else "snow"
                                for x in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ["red" for x in range(len(data))])