import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("data/partial_sphere_beads_140deg_500000.txt",
                   delim_whitespace=True, header=None)

data.head()
data.index = data[0].map(lambda x: int(x))
data.drop(0, axis=1, inplace=True)
data.drop([4, 5, 6, 7, 8, 9], axis=1, inplace=True)
data.columns = ["x", "y", "z"]

data_1 = data.loc[1:500000, :]
data_2 = data.loc[500001:1000000, :]
data_3 = data.loc[1000001:1500000, :]
data_4 = data.loc[1500001:2000000, :]
data_5 = data.loc[2000001:2500000, :]

data_all = [data_1, data_2, data_3, data_4, data_5]

data_all_scr = []
for d in data_all:
    tmp = d.dropna(axis=0)
    tmp = d[np.round(d["x"]) == 33]
    tmp = d.drop("x", axis=1)
    data_all_scr.append(tmp)

data_all_scr[1]
plt.scatter(data_all_scr[1][:, "y"])
data_all_scr[3].plot(x='y', y='z', kind='scatter')
plt.show()

cut_range = [i for i in range(0, 2500001, 500000)]
data["dim"] = pd.cut(data.index, cut_range)
data.tail()
