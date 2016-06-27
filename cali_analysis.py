import numpy as np
import pandas as pd
import math

f = open('probe_calibration.txt', 'w')

for i in range(1,5):

    density_cup1 = raw_input("Cup 1 density: ")

    f.write(density_cup1, ' ')

    data = pd.read_csv('cup1.txt', skiprows = 6, sep = " ", names = ['date', 'time', 'V'])

    data = data.V.dropna()

    probe_reading_cup1 = np.mean(data)

    f.write(data_mean_cup1)

data2 = pd.read_csv('probe_calibration.txt', sep = " ", names = ['density', 'probe_reading'])

plt(density, probe_reading)

slope, intercept = np.polyfit(np.array(density), np.array(probe_reading),1)

inv_slope = 1/slope

inv_intercept = 1/intercept

  
data3 = pd.read('exp160621220022.txt', skiprows = 6, sep = " ", names = ['date', 'time', 'steps', 'z', 'V'])
data3.rho = inv_slope * data3.V + inv_intercept
plt.plot(data5.rho, data5.z)

slope, intercept = np.polyfit(np.array(data3.rho.dropna()), np.array(data3.z.dropna()),1)
strat_freq = math.sqrt((1/slope)*980)
inv_slope = 1/slope
inv_intercept = 1/intercept

print(strat_freq)

