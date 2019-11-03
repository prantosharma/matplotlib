import matplotlib.pyplot as plt

#this are the style of ghraph
# plt.style.use('fivethirtyeight')
plt.style.use('ggplot')

#develpoer age and salaries
ages=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[30600,32000,33567,34900,36700,40689,43890,42789,47897,50987,65987]
#python evelopers and salaries
py_dev_y=[40500,42390,44389,45678,48908,52098,55678,59098,62756,64321,67857]
#js evelopers and salaries
js_dev_y=[12313,43434,23124,21313,34455,45664,55757,65547,75645,65453,60343]

plt.xlabel('Ages')
plt.ylabel('Salary(USD) of developers')
plt.title('Median salary by age')

plt.plot(ages,dev_y,color='#459845',linestyle='--',marker='.',label='dev_x')
plt.plot(ages,py_dev_y,color='#987645',linestyle='-',marker='o',label='py_dev_y')
plt.plot(ages,js_dev_y,color='#081240',marker='h',label='js_dev_y')
plt.grid(True)
plt.tight_layout()#fit the ghraph in the figure
plt.legend()#identifier of each line
plt.savefig('fplot.png')#location will be change 
plt.show()