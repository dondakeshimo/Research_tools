
# coding: utf-8

# In[2]:

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


# In[18]:

# ベクトルxを [-5.0, ..., 5.0] の区間で作成
n = np.linspace(-5.0, 5.0, 10000)

# 平均0, 標準偏差1の正規分布における、xの確率を求める
p = []
for i in range(len(n)):
    p.append(-1 * norm.pdf(x=n[i], loc=0, scale=1))

# 平均0, 標準偏差1の正規分布における、xの確率を求める
q = []
for i in range(len(n)):
    q.append(-1 * norm.pdf(x=n[i], loc=1, scale=1))

#グラフタイトル
plt.title('Large FWHM')

#グラフの軸
plt.xlabel('Wavelength')
plt.ylabel('Reflectance')

# 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
plt.plot(n, p)
plt.plot(n, q)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
plt.savefig("./images/large_fwhm.png", transparent=True)
plt.show()


# In[22]:

# ベクトルxを [-5.0, ..., 5.0] の区間で作成
n = np.linspace(-5.0, 5.0, 10000)

# 平均0, 標準偏差1の正規分布における、xの確率を求める
p = []
for i in range(len(n)):
    p.append(-1 * norm.pdf(x=n[i], loc=0, scale=0.5))

# 平均0, 標準偏差1の正規分布における、xの確率を求める
q = []
for i in range(len(n)):
    q.append(-1 * norm.pdf(x=n[i], loc=1, scale=0.5))

#グラフタイトル
plt.title('Small FWHM')

#グラフの軸
plt.xlabel('Wavelength')
plt.ylabel('Reflectance')

# 乱数－確率 の特性を散布図で表し、標準正規分布のグラフを作成
plt.plot(n, p)
plt.plot(n, q)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
plt.savefig("./images/small_fwhm.png")
plt.show()


# In[ ]:



