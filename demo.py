# import matplotlib.pyplot as plt
# import csv
# import pandas as pd
# from matplotlib.animation import FuncAnimation


# x = 0
# y = 0

# def animate(i):
# 	global x
# 	global y
	
# 	data = pd.read_csv('f.csv')

# 	x = data['x']
# 	print(x)
# 	y = data['y']
# 	plt.cla()
# 	plt.plot(x,y)



# ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
# plt.tight_layout()
# plt.show()


import matplotlib.pyplot as plt
import csv
import pandas as pd
from matplotlib.animation import FuncAnimation


x = 0
y = 0
lst1=[]
lst2=[]
lst3=[]
lst4=[]


temp = 0
def animate(i):
	x = []
	y = []
	global temp
	with open('f.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			x.append(row[1])
			y.append(row[0])
		x = x[1:]
		y = y[1:]

	for i in range(len(x)) :
		x[i]=int(x[i])
		y[i] = float(y[i])

		if i % 30 != 0:
			temp = temp + y[i]
		else :
			lst3.append(int(i/ 30))
			lst4.append(temp/30)
			temp = y[i]

	plt.cla()
	plt.plot(lst3,lst4)
	plt.axhline(y=0.29, color='r', linestyle='-')
	lst3.clear()
	lst4.clear()
	x.clear()
	y.clear()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
plt.tight_layout()
plt.show()



# print(lst3)
# print(lst4)

# def animate(i):
	
# 	#data = pd.read_csv('f.csv')
# 	with open('f.csv','r') as f:
# 		reader = csv.readereader(f)

# 		for rows in reader:
# 			print(rows[1])
			

# 			if rows % 15 == 0 :
# 				lst3.append(sum(lst1)/len(lst1))
# 				lst4.append(sum(lst2)/len(lst2))
# 				lst1.clear()
# 				lst2.clear()

	
# 	# plt.cla()
# 	# plt.plot(lst3,lst4)




# ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
# # plt.tight_layout()
# # plt.show()