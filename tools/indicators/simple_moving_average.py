import numpy as np
import warnings
from tools.indicators.function_helper import fill_for_noncomputable_vals
from tools.indicators.catch_errors import check_for_period_error


def simple_moving_average(data, period):
    """
    Simple Moving Average.

    Formula:
    SUM(data / N)
    """
    check_for_period_error(data, period)
    # Mean of Empty Slice RuntimeWarning doesn't affect output so it is
    # supressed
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        sma = list(map(
            lambda idx:
            np.mean(data[idx-(period-1):idx+1]),
            range(0, len(data))
            ))
    sma = fill_for_noncomputable_vals(data, sma)
    return sma
