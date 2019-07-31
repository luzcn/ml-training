import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def demo():
    rng = np.random.RandomState(12)
    x = 10 * rng.rand(50)
    print(x)

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    # we need to convert the data from a 1-d array to a 2-d array
    # so we use np.newaxis to do that
    # ...let's take a look
    print(x)
    print(x.shape)
    x2 = x[:, np.newaxis]
    print(x2)

    y = 2 * x - 6 + rng.randn(50)  # add some noise to the output
    # plt.scatter(x, y)

    model.fit(x[:, np.newaxis], y)
    xfit = np.linspace(0, 10, 2)
    yfit = model.predict(xfit[:, np.newaxis])
    plt.scatter(x, y)
    plt.plot(xfit, yfit, color='red')

    plt.show()


def exercise():
    data = pd.read_csv('../src/data/skincancer.csv', sep='\t', na_values=[r'\N'])
    print(data)

    x = data['Lat']
    y = data['Mort']
    # plt.scatter(x, y)
    # plt.show()

    model = LinearRegression()
    model.fit(x[:, np.newaxis], y)

    xfit = np.linspace(25, 50, 50)
    yfit = model.predict(xfit[:, np.newaxis])
    plt.scatter(x, y)
    plt.plot(xfit, yfit, color='red')
    plt.show()


exercise()
