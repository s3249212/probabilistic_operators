import numbers
import numpy as np
import operator

class Probability_Histogram:
    def __init__(self, histogram):
        # histogram = [(8, 0.1), (9, 0.9)]
        self.histogram = histogram

    def handle_function(self, other, element_operator, reverse=False):
        if isinstance(other, numbers.Number):
            other = Probability_Histogram([(other, 1)])
        
        if not isinstance(other, Probability_Histogram):
            raise ValueError

        hist_0, hist_1 = self, other

        if reverse:
            hist_0, hist_1 = hist_1, hist_0

        new_histogram = []

        for (value_0, prob_0) in hist_0.histogram:
            for (value_1, prob_1) in hist_1.histogram:
                value_res = element_operator(value_0, value_1)
                prob_res = prob_0 * prob_1
                new_histogram.append((value_res, prob_res))

        return Probability_Histogram(new_histogram)

    def __mul__(self, other):
        return self.handle_function(other, operator.__mul__)

    def __rmul__(self, other):
        return self.handle_function(other, operator.__mul__)

    def __add__(self, other):
        return self.handle_function(other, operator.__add__)

    def __radd__(self, other):
        return self.handle_function(other, operator.__add__)

    def __sub__(self, other):
        return self.handle_function(other, operator.__sub__)

    def __rsub__(self, other):
        return self.handle_function(other, operator.__sub__, reverse=True)

    def __div__(self, other):
        return self.handle_function(other, np.div)

    def __rdiv(self, other):
        return self.handle_function(other, np.div, reverse=True)

    def __truediv__(self, other):
        return self.handle_function(other, np.true_divide)

    def __rtruediv__(self, other):
        return self.handle_function(other, np.true_divide, reverse=True)

    def __floordiv__(self, other):
        return self.handle_function(other, np.floor_divide)

    def __rfloordiv__(self, other):
        return self.handle_function(other, np.floor_divide, reverse=True)

    def __mod__(self, other):
        return self.handle_function(other, np.mod)

    def __rmod__(self, other):
        return self.handle_function(other, np.mod, reverse=True)

    def __divmod__(self, other):
        return self.handle_function(other, np.divmod)

    def __rdivmod__(self, other):
        return self.handle_function(other, np.divmod, reverse=True)

    def __pow__(self, other):
        return self.handle_function(other, np.pow)
    
    def __rpow__(self, other):
        return self.handle_function(other, np.pow, reverse=True)
    
    def __lshift__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __rlshift__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __rshift__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __rrshift__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __and__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __rand__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __xor__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __rxor__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __or__(self, other):
        return self.handle_function(other, np.pow, reverse=True)

    def __ror__(self, other):
        return self.handle_function(other, np.pow, reverse=True)