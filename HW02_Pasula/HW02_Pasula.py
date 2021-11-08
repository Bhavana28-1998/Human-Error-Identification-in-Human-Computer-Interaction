import numpy as x
import pandas as y
import matplotlib.pyplot as plt

sd=y.read_csv('Experiment.csv',header=None)

d=y.DataFrame(sd.iloc[0,:])
w=y.DataFrame(sd.iloc[1,:])
div=y.DataFrame(sd.iloc[0,:]).values/y.DataFrame(sd.iloc[1,:])

# print(sd, div)

t_avg=y.DataFrame(sd.iloc[2:,:]).mean()
t_std=y.DataFrame(sd.iloc[2:,:]).std()
t_median=y.DataFrame(sd.iloc[2:,:]).median()

plt.plot(x.sort(t_avg),div)
plt.show()

plt.plot(x.sort(t_std),div)
plt.show()

plt.plot(x.sort(t_median),div)
plt.show()

s_avg=t_avg.nsmallest(3)
s_std=t_std.nsmallest(3)
s_med=t_median.nsmallest(3)


plt.xlabel('user')
plt.ylabel('time')
plt.title('user with smalleest mean vs time')
plt.plot(x.sort(sd.iloc[:,s_avg.index[0]]), ms=3, marker="*")
plt.axhline(s_avg.values[0],color='r',label='Mean')
plt.legend() 

plt.xlabel('user')
plt.ylabel('time')
plt.title('user with smallest mean vs time')
plt.plot(x.sort(sd.iloc[:,s_avg.index[1]]), ms=3, marker="*")
plt.axhline(s_avg.values[1],color='r',label='mean')
plt.legend() 

plt.xlabel('user')
plt.ylabel('time')
plt.title('user with smallest mean vs time')
plt.plot(x.sort(sd.iloc[:,s_avg.index[2]]), ms=3, marker="*")
plt.axhline(s_avg.values[2],color='r',label='mean')
plt.legend() 

plt.xlabel('user')
plt.ylabel('time')
plt.title('user with smallest std vs time')
plt.plot(x.sort(sd.iloc[:,s_std.index[0]]), ms=3, marker="*")
plt.axhline(s_std.values[0],color='r',label='std')
plt.legend() 

plt.xlabel('user')
plt.ylabel('time')
plt.title(' smallest std vs time')
plt.plot(x.sort(sd.iloc[:,s_std.index[1]]), ms=3, marker="*")
plt.axhline(s_std.values[1],color='r',label='std')
plt.legend() 

plt.xlabel('user')
plt.ylabel('time')
plt.title('user with smallest std vs time')
plt.plot(x.sort(sd.iloc[:,s_std.index[2]]), ms=3, marker="*")
plt.axhline(s_std.values[2],color='r',label='std')
plt.legend() 

plt.xlabel('user')
plt.ylabel('time')
plt.title('user with smallest median vs time')
plt.plot(x.sort(sd.iloc[:,s_med.index[0]]), ms=3, marker="*")
plt.axhline(s_med.values[0],color='r',label='median')
plt.legend() 

plt.xlabel('user')
plt.ylabel('time')
plt.title('user with smallest median vs time')
plt.plot(x.sort(sd.iloc[:,s_med.index[1]]), ms=3, marker="*")
plt.axhline(s_med.values[1],color='r',label='median')
plt.legend() 

plt.xlabel('user')
plt.ylabel('time')
plt.title('user with smallest median vs time')
plt.plot(x.sort(sd.iloc[:,s_med.index[2]]), ms=3, marker="*")
plt.axhline(s_med.values[2],color='r',label='median')
plt.legend() 

# print(s_avg, s_std, s_med)

distance=sd.iloc[0:2,s_std.index[0]].values[0]
width=sd.iloc[0:2,s_std.index[0]].values[1]

# print(distance,width)