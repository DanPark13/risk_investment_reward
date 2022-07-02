"""
Helper Functions Library for Notebook
"""

def display_as_percentage(val):
    return '{:.1f}%'.format(val*100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

from math import log, sqrt

# Calculate Log Return
def calculate_log_return(start_price, end_price):
    return log(end_price / start_price)

# Calculate Variance
def calculate_variance(dataset):
    mean = sum(dataset)/len(dataset)
    numerator = 0
    for data in dataset:
        numerator += (data-mean) ** 2
    return numerator / len(dataset)

# Calculate Standard Deviation
def calculate_stddev(dataset):
    variance = calculate_variance(dataset)
    return sqrt(variance)

# Calculate Correlation Coefficient
def calculate_correlation(set_x, set_y):
    sum_x = sum(set_x)
    sum_y = sum(set_y)
    
    sum_x2 = sum([x ** 2 for x in set_x])
    sum_y2 = sum([y ** 2 for y in set_y])
    sum_xy = sum([x * y for x,y in zip(set_x, set_y)])
    
    n = len(set_x)
    numerator = n * sum_xy - sum_x * sum_y
    denominator = sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
    return numerator / denominator