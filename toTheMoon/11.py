import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = [a for a in range(0, 480)]
data1 = pd.read_csv('10011001#2001#1023#71.txt', names=['timestamp','data'])
data1['timestamp'] = x

data2 = pd.read_csv('10011001#2001#1023#711.txt', names=['timestamp','data'])
data2['timestamp'] = x
data2['data'][:160] = data1['data'][:160]

data3 = pd.read_csv('10011001#2001#1023#71111.txt', names=['timestamp','data'])
data3['timestamp'] = x
data3['data'][:160] = data1['data'][:160]

data4 = pd.read_csv('10011001#2001#1023#733.txt', names=['timestamp','data'])
data4['timestamp'] = x
data4['data'][:160] = data1['data'][:160]

data5 = pd.read_csv('10011001#2001#1023#744.txt', names=['timestamp','data'])
data5['timestamp'] = x
data5['data'][:160] = data1['data'][:160]

fig = plt.figure(1)
ax1 = fig.add_subplot(2, 2, 1)
data    = plt.plot(data1['timestamp'], data1['data'], ls='-.', label='Ground Truth', c='b')
lstm    = plt.plot(data5['timestamp'], data5['data'], ls='-.', label='Classical Single Layer LSTM', c='r')
plt.title('Classical Single Layer LSTM')
plt.xlabel('timestamp')
plt.ylabel('value')

ax2 = fig.add_subplot(2, 2, 2)
data    = plt.plot(data1['timestamp'], data1['data'], ls='-.', label='Ground Truth', c='b')
stacked = plt.plot(data4['timestamp'], data4['data'], ls='-.', label='Stacked LSTM', c='r')
plt.title('Stacked LSTM')
plt.xlabel('timestamp')
plt.ylabel('value')

ax3 = fig.add_subplot(2, 2, 3)
data    = plt.plot(data1['timestamp'], data1['data'], ls='-.', label='Ground Truth', c='b')
Bi      = plt.plot(data3['timestamp'], data3['data'], ls='-.', label='Bidirectional LSTM', c='r')
plt.title('Bidirectional LSTM')
plt.xlabel('timestamp')
plt.ylabel('value')

ax4 = fig.add_subplot(2, 2, 4)
data    = plt.plot(data1['timestamp'], data1['data'], ls='-.', label='Ground Truth', c='b')
EncoDeco= plt.plot(data2['timestamp'], data2['data'], ls='-.', label='Encoder-Decoder LSTM', c='r')
plt.title('Encoder-Decoder LSTM')

plt.xlim(0, 480)
plt.xticks(np.arange(0, 480, step=80))
plt.ylim(20.50, 21.50)
plt.yticks(np.arange(20.50, 21.50, step=0.25))
plt.tight_layout()
plt.xlabel('timestamp')
plt.ylabel('value')
plt.show()