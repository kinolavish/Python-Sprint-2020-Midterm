import csv
import matplotlib.pyplot as plt

dates=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,
   35,36,37,38,39,40,41,42,43,44]
cases=[1,1,1,2,3,5,5,5,6,7,8,11,11,11,12,12,12,12,12,13,13,14,15,15,15,15,25,25,25,27,30,30,30,43,
   45,60,60,65,70,88,104,125,161,228]
#plt.plot(dates,cases)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, cases, c='red')

# Format plot.
plt.title("Daily covid cases - 2020", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("cases", fontsize=16)
plt.xlabel("days", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()