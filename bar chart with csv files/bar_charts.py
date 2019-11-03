import numpy as np
import matplotlib.pyplot as plt

#this are the style of ghraph
plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')

#develpoer age and salaries
ages=[25,26,27,28,29,30,31,32,33,34,35]
x_indexs=np.arange(len(ages))
width=0.25

dev_y=[30600,32000,33567,34900,36700,40689,43890,42789,47897,50987,65987]
#python evelopers and salaries
py_dev_y=[40500,42390,44389,45678,48908,52098,55678,59098,62756,64321,67857]
#js evelopers and salaries
js_dev_y=[12313,43434,23124,21313,34455,45664,55757,65547,75645,65453,60343]
#django developers salaries
django_dev_y=[20313,25434,23124,25313,34455,29664,31757,33547,35645,38453,40343]

plt.xlabel('Ages')
plt.ylabel('Salary(USD) of developers')
plt.title('Median salary by age')

plt.bar(x_indexs,dev_y,color='#459845',width=width,linestyle='--',label='all devs')
plt.bar(x_indexs-width,py_dev_y,color='#987645',width=width,linestyle='-',label='python')
plt.bar(x_indexs+width,js_dev_y,color='#081240',width=width,label='javascripts')
plt.bar(x_indexs+width+width,django_dev_y,color='k',width=width,label='django')
plt.xticks(ticks=x_indexs,labels=ages)
plt.grid(True)

plt.tight_layout()#fit the ghraph in the figure
plt.legend()#identifier of each line

# plt.savefig('fplot.png')#location will be change 

plt.show()