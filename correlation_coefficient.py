import stats

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
while True:
    print("Enter data for the first dataset")
    data1 = get_data()
    print("Enter data for the second dataset")
    data2 = get_data()


    stats.correlation_coefficient(data1,data2)
        
