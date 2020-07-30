import numbers
import numpy as np

class Probability_Histogram:
    def __init__(self, histogram):
        # histogram = [(8, 0.1), (9, 0.9)]
        self.histogram = histogram

    def handle_function(self, other, element_operator):
        if isinstance(other, numbers.Number):
            other = Probability_History([(other, 1)])
        
        if not isinstance(other, Probability_Histogram):
            raise ValueError

        new_histogram = []

        for (value_0, prob_0) in self.histogram:
            for (value_1, prob_1) in other.histogram:
                value_res = element_operator(value_0, value_1)
                prob_res = prob_0 * prob_1
                new_histogram.append((value_res, prob_res))

        return Probability_Histogram(new_histogram)

    def __mul__(self, other):
        return self.handle_function(other, np.multiply)

    def __rmul__(self, other):
        return self.handle_function(other, np.multiply)

    def __add__(self, other):
        return self.handle_function(other, np.add)

    def __radd__(self, other):
        return self.handle_function(other, np.add)