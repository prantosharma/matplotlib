import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

minutes=[1,2,3,4,5,6,7,8,9]

player1=[1,1,2,2,3,4,4,4,5]
player2=[1,2,2,2,3,4,5,5,5]
player3=[1,2,3,3,4,4,5,5,6]

labels=['player1','player2','player3']
colors=['#6d904F','#fc4f30','#008fd5']

plt.stackplot(minutes,player1,player2,player3,colors=colors,labels=labels)

plt.legend(loc='upper left')
# plt.legend(loc=(.07,.05))

plt.grid(True)

plt.title('stack plot')
plt.tight_layout()
plt.savefig('stack_plot.png')
plt.show()