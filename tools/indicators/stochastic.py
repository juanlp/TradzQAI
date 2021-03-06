import numpy as np
from tools.indicators.catch_errors import check_for_period_error
from tools.indicators.function_helper import fill_for_noncomputable_vals
from tools.indicators.simple_moving_average import simple_moving_average as sma

np.seterr(divide='ignore', invalid='ignore')

def percent_k(data, period):
    """
    %K.

    Formula:
    %k = data(t) - low(n) / (high(n) - low(n))
    """
    check_for_period_error(data, period)
    percent_k = list(map(
        lambda idx:
        ((data[idx] - np.min(data[idx+1-period:idx+1])) /
         (np.max(data[idx+1-period:idx+1]) -
          np.min(data[idx+1-period:idx+1]))),
        range(period-1, len(data))
        ))
    percent_k = fill_for_noncomputable_vals(data, percent_k)

    return percent_k


def percent_d(data, period):
    """
    %D.

    Formula:
    %D = SMA(%K, 3)
    """
    p_k = percent_k(data, period)
    percent_d = sma(p_k, 3)
    return percent_d
