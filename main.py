from probability_histogram import *

x = Probability_Histogram([(10, 0.4), (20, 0.6)])
y = Probability_Histogram([(3, 0.1), (4, 0.2), (7, 0.7)])

print((x * y).histogram)