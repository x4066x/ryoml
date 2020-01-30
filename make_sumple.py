import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class MakeSumple():
    def makesumple(self):

        a = 5
        b = 3

        x = np.arange(0, 10, 0.1)
        # y = [i * a + b + np.random.randn() * 2 for i in x]

        # plt.plot(x, y, 'o')
        # plt.show()

        data_sample = [[i , i * a + b + (np.random.randn()) * 100 ] for i in x]

        df = pd.DataFrame(data_sample)
        #print(df)

        df.to_csv('./sample.csv', index=None , header=None)

