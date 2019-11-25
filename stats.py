import math

class statistics:
    def __init__(self, dataset):
        self._dataset = dataset
        self._dataset.sort()
    def average(self):
        total = 0
        n = len(self._dataset)
        for i in self._dataset:
            total += i
        return total/n

    def median(self):
        if len(self._dataset)%2 == 0:
            median = ((self._dataset[(len(self._dataset)//2)-1]+self._dataset[-((len(self._dataset)//2))])/2)
            return median
        else:
            median = (self._dataset[(len(self._dataset)//2)])
            return median
    def standard_deviation(self):
        mean = self.average()
        holder = []
        total = 0
        for i in self._dataset:
            value = (i-mean)
            value = value ** 2
            holder.append(value)
        for i in holder:
            total += i
        n = len(holder)
        total = total/(n-1)
        return math.sqrt(total)
    def lower_quartile(self):
        if len(self._dataset)%2 == 0:
            data_median = ((len(self._dataset)//2))
            dataset = self._dataset[0:int(data_median)]
            data_quartile = dataset[int(len(dataset)//2)]
            return data_quartile
        else:
            data_median = ((len(self._dataset)//2))
            dataset = self._dataset[0:int(data_median)]
            if len(dataset)%2 == 0:
                first = dataset[(len(dataset)//2)-1]
                second = dataset[(len(dataset)//2)]
                data_quartile = ((first+second)/2)
            else:
                data_quartile = dataset[(len(dataset)//2)]
            return data_quartile
        
    def upper_quartile(self):
        if len(self._dataset)%2 == 0:
        
            data_median = ((len(self._dataset)//2))
            dataset = self._dataset[int(data_median):len(self._dataset)]
            data_quartile = dataset[int(len(dataset)//2)]
            return data_quartile
        else:
             data_median = ((len(self._dataset)//2))
             dataset = self._dataset[int(data_median)+1:len(self._dataset)]
             if len(dataset)%2 == 0:
                 first = dataset[(len(dataset)//2)-1]
                 second = dataset[(len(dataset)//2)]
                 data_quartile = ((first+second)/2)
             else:
                 data_quartile = dataset[(len(dataset)//2)]
             return data_quartile
            
    def lower_fence(self):
        lower = self.lower_quartile()
        upper = self.upper_quartile()
        IQR = (upper-lower)
        return (lower - (1.5 * IQR))

    def upper_fence(self):
        lower = self.lower_quartile()
        upper = self.upper_quartile()
        IQR = (upper-lower)
        return (upper + (1.5 * IQR))

    def display_stats(self):
        print("The length of the dataset is", len(self._dataset))
        print("The average is : ", self.average())
        print("The lower quartile is : ",self.lower_quartile())
        print("The median is : ", self.median())
        print("Standard Deviation is : ", self.standard_deviation())
        print("The upper quartile is : ",self.upper_quartile())
        print("Upper fence is : ", self.upper_fence())
        print("Lower fence is : ", self.lower_fence())
        print("Minimum value is : ", min(self._dataset))
        print("Maximum value is : ", max(self._dataset))
        
def linear_regression():
    def line_of_regression(y_mean, x_mean, sd_x, sd_y, r):

        mean = ((sd_y/sd_x)*r)
        y_intercept = (y_mean -((mean)*x_mean))
        y_int = str(float("{0:.3f}".format(y_intercept)))
        strmean = str(float("{0:.3f}".format(mean)))
        line = f"The line is y = {strmean}x + {y_int}"

        return mean, y_intercept,line


    y_mean = float(input("Type mean of Y : "))
    x_mean = float(input("Type mean of X : "))
    sd_y = float(input("Type standard deviation of y : "))
    sd_x = float(input("Type standard deviation of x : "))
    r = float(input("Type r value : "))

    mean, y_intercept, line = line_of_regression(y_mean, x_mean, sd_x, sd_y, r)

    print("The mean is...", float("{0:.3f}".format(mean)))
    print("The Y-intercept is...", float("{0:.3f}".format(y_intercept)))
    print(line)


def correlation_coefficient(dataset_x,dataset_y):
    
    data_x = dataset_x[:]
    data_y = dataset_y[:]
    stats_x = statistics(data_x)
    stats_y = statistics(data_y)
    product_total = 0

    x_container = []
    y_container = []
    product_container = []
    x_average = stats_x.average()
    y_average = stats_y.average()
  
    for number in dataset_x:
        total = number - x_average
        x_container.append(total)

    for number in dataset_y:
        total = number - y_average
        y_container.append(total)

    for i in range(len(x_container)):
        total = float("{0:.5f}".format((x_container[i])*(y_container[i])))
        product_container.append(total)
        
    for number in product_container:
        product_total += number
    
    x_sd = float("{0:.5f}".format(stats_x.standard_deviation()))
    y_sd = float("{0:.5f}".format(stats_y.standard_deviation()))
  
    length = len(product_container)
    final_total = float("{0:.5f}".format((length-1)*(x_sd) * (y_sd)))
  
    r = product_total/final_total
    return print("The correlation coefficient is :", r)
