import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import csv

# plt.style.use('fivethirtyeight')
plt.style.use('ggplot')
#cvs file open
with open('E:\\Anaconda files\\meching learning\\Matplotlib\\bar chart with csv files\\data.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file)

    row=next(csv_reader)
    languages_count=Counter()

    for row in csv_reader:
        languages_count.update(row['LanguagesWorkedWith'].split(';'))
    # print(languages_count.most_common(18))

languages=[]
popularity=[]

for item in languages_count.most_common(18):
    languages.append(item[0])
    popularity.append(item[1])

# print(languages)
# print(popularity)

plt.xlabel('Number of people who use')
plt.ylabel('Programming languages')
plt.title('Most popular languages')

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)

plt.tight_layout()#fit the ghraph in the figure
plt.legend()#identifier of each line

plt.savefig('cvsplot.png')#location will be change 

plt.show()