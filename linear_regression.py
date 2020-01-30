import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class LineaerRegression:

    def read_csv(self, file):
        return pd.read_csv(file, header=None)

    def train(self, data_train):

        a_11 = len(np.array(data_train[:][0]))
        a_12 = sum(np.array(data_train[:][0]))
        a_21 = sum(np.array(data_train[:][0]))
        a_22 = sum([x **2 for x in np.array(data_train[:][0])])
        y_1 = sum(np.array(data_train[:][1]))
        y_2 = sum([l[0] * l[1] for l in np.array(data_train)])

        y_vec = np.array([y_1, y_2])
        A = np.array([[a_11,a_12],[a_21,a_22]])

        A_inverse = np.linalg.inv(A)
        w_vec = np.dot(A_inverse, y_vec)

        return w_vec


    def plot(self, vec_w,train):
        x = np.arange(0, 10, 0.1)
        y = [vec_w[0] + i * vec_w[1] for i in x]
        plt.plot(x, y)

        x =np.array(train[:][0])
        y =np.array(train[:][1])
        plt.plot(x, y ,'o')
    #    plt.show()
        plt.savefig('./static/result.png')

    def work(self):
        data = self.read_csv('sample.csv')

        vec_w = self.train(data)

        self.plot(vec_w, data)

if __name__ == '__main__':
    l = LineaerRegression()
    data = l.read_csv('sample.csv')
    vec_w = l.train(data)
    l.plot(vec_w, data)
