import math
import random
from typing import Callable

def linear_regression(X: list[int], Y: list[int]):
    n = len(X)

    sum_x = sum([x for x in X])
    sum_x_sqd = sum([x**2 for x in X])
    sum_y = sum([y for y in Y])
    sum_xy = sum([X[i]*Y[i] for i in range(n)])

    denominator = n*sum_x_sqd - sum_x**2
    theta1 = (n*sum_xy - sum_x*sum_y) / denominator
    theta2 = (sum_y*sum_x_sqd - sum_x*sum_xy) / denominator

    return theta1, theta2

def MSE(y_observed: list[int], y_predicted: list[int]):
    n = len(y_observed)
    MSE = 1/n * sum([(y_observed[i]-y_predicted[i])**2 for i in range(n)])
    return MSE

def line_points_y(slope, y_intercept, number, starting_x):
    return [slope*x+y_intercept for x in range(starting_x, starting_x+number)]

def test_linear_regression(function: Callable[[int], int], noise_amount: float, size: int):
    xpoints = []
    ypoints = []
    xpoints_noise = []
    ypoints_noise = []

    # make line y points from x with noise
    for x in range(size):
        xpoints.append(x)
        y = function(x)
        ypoints.append(y)

        noise = random.random()*noise_amount-noise_amount/2
        xpoints_noise.append(x + noise)
        noise = random.random()*noise_amount-noise_amount/2
        ypoints_noise.append(y + noise)

    # index to split list at 75%
    split_75 = int(size*0.75)

    # using the first 75% of data fit linear regression
    theta1, theta2 = linear_regression(xpoints_noise[:split_75], ypoints_noise[:split_75])

    # learned parameters of theta 1, 2
    print("learned parameters of theta 1: {t1} and theta 2: {t2}".format(t1=theta1, t2=theta2))

    # compare MSE over training dataset
    print("MSE over the training dataset:", MSE(ypoints, ypoints_noise))

    # create the last 25 percent at the end of the line created by linear regression
    predicted_y = line_points_y(theta1, theta2, size-split_75, split_75)

    # compare MSE: data points to linear regression prediction
    print("MSE over the evaluation dataset:", MSE(ypoints_noise[split_75:], predicted_y))


# TESTING
# linear test function: slope: 4, y intercept: 13
linear_func = lambda x : 4*x + 13

print("collection of points where a single line can go through every point. (slope: 4, y intercept: 13)")
test_linear_regression(linear_func, 0, 40)
print()

print("collection of points that follow linear relationship, but not perfectly. (slope: 4, y intercept: 13)")
test_linear_regression(linear_func, 2, 40)
print()

# non linear test function: range: [11, 23], period: 2pi
sin_func = lambda x : 6*math.sin(x) + 17
print("collection of points that do not follow linear relationship. (sine function)")
test_linear_regression(sin_func, 0, 40)