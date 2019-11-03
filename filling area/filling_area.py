import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('E:\\Anaconda files\\meching learning\\Matplotlib\\filling area\\data.csv')

ages=data['Age']
devs_salaries=data['All_Devs']
py_salaries=data['Python']
js_salaries=data['JavaScript']

overall_median=66657.00

plt.plot(ages,devs_salaries,linestyle='--',color='#957ddc',label='all_developers')
plt.plot(ages,js_salaries,color='#444444',label='javascripts')
plt.plot(ages,py_salaries,color='red',label='python')



plt.fill_between(ages,js_salaries, devs_salaries,where=(js_salaries>devs_salaries),
                    interpolate=True,alpha=.25)


# plt.fill_between(ages,js_salaries, overall_median,where=(js_salaries<=overall_median),
#                     interpolate=True,color='red',alpha=.25)

plt.fill_between(ages,py_salaries,devs_salaries,where=(py_salaries<devs_salaries),
                 interpolate=True,color='black',alpha=.25)



plt.title('median salary by ages')
plt.xlabel('ages')
plt.ylabel('median salary')



plt.legend()

# plt.savefig('fill_area.png')
plt.tight_layout()
plt.show()