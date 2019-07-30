import matplotlib.pyplot as plt
import numpy as np


def demo():
    # setup fig style and x, y limits
    plt.figure(figsize=(8, 8))
    plt.style.use('seaborn-whitegrid')
    plt.xticks(range(10, 31, 5))
    plt.xlim(10, 30)
    plt.ylim(10, 40)

    # line 1 points
    x1 = [10, 20, 30]
    y1 = [20, 40, 10]
    plt.plot(x1, y1, label="this line", color='red')

    # line 2 points
    x2 = [10, 20, 30]
    y2 = [40, 10, 30]
    # plotting the line 2 points
    plt.plot(x2, y2, label="that line", color='green')

    plt.legend()
    plt.show()


demo()
