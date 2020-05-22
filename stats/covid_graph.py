import csv
import matplotlib.pyplot as plt


dates=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,
   35,36,37,38,39,40,41,42,43,44]
cases=[88,104,125,161,228,311,428,547,748,1018,1263,1668,2224,2898,3600,4507,5905,8345,12384,17990,
       24511,33043,43477,53892,68489,85497,102729,123581,142194,163589,188049,214711,244034,276501,
       311536,336711,397748,429316,463684,49614,528397,555327,580853,607285]
deaths = [3,6,10,12,12,15,19,22,26,31,37,43,50,60,68,91,116,157,203,343,435,550,731,989,1275,1648,
          2134,2487,3068,3911,4841,5952,7121,8499,9654,10958,12957,14803,16673,18710,10958,12957,
          14803,16673]
recoveries = [39,42,46,48,48,151,155,158,162,167,173,179,186,196,204,229,293,439,679,786,997,1025,1311,1684,
              3000,3897,4023,5389,5777,6229,8398,7873,10923,11234,13623,14792,17397,19938,14902,20093,
              30098,38894,34994,49487
]
#plt.plot(dates,cases)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, cases, c='red')
ax.plot(dates, deaths, c='green')
ax.plot(dates, recoveries, c='blue')
## Format plot.
plt.title("Daily covid cases and deaths - 2020", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("cases(red), death(green) and recoveries(blue)", fontsize=16)
plt.xlabel("days", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()