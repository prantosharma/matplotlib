import matplotlib.pyplot as plt
plt.style.use('ggplot')

plt.title('pie charts')

#basic pie code
# slices=[43,30,55]
#labels=['fourtythree','thirty','fiftyfive']
# colors=['#6bb1bf','#48d1cc','#3b5998']
# plt.pie(slices, colors=colors,labels=labels,wedgeprops={'edgecolor':'black'})

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode=[0,0,.1,0,0]

plt.pie(slices,labels=labels,explode=explode,shadow=True,
startangle=90,autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})


#tight_layout automatically adjusts subplot params 
# so that the subplot(s) fits in to the figure area.
plt.tight_layout()
plt.savefig('pie.png')
plt.show()