import stats
import random

def get_data():
    container = []
    data = 0
    i = 1
    print("Enter any amount of numbers to be analyzed")
    while True:
        data = input("Input Number -->")
        if data != 'done':
            data = int(data)
            container.append(data)
            i += 1
        else:
            break
    return container

data_object = stats.statistics(get_data())
data_object.display_stats()
