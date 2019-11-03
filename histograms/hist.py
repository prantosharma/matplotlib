import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data=pd.read_csv('E:\\Anaconda files\\meching learning\\Matplotlib\\histograms\\data.csv')
ages=data['Age']
ids=data['Responder_id']


bins=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

plt.hist(ages,bins=bins,edgecolor='red')

# a=ages.median()
# print(a)
median_age=29
color='#fc4f30'
plt.axvline(median_age,color=color,label='age median',linewidth=3)




plt.title('Ages of respondents')
plt.xlabel('ages')
plt.ylabel('total respondents')



plt.legend()

# plt.savefig('hist.png')
plt.tight_layout()
plt.show()