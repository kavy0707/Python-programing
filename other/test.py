# # # a = ["k","kavty","boricha"]
# # # k = ["kdwcdw","ddcefvcefced","borsdcvsdicha"]

# # # print("borichaa" not in a)

# # # b= (1,2,3,4,5,6)
# # # print(type(b))


# # # m= "kavy"
# # # n="boricha"

# # # print(min(a))

# # # k.extend(a)
# # # print(k)
# # # a[1]
# # # print(a)

# # # for num in range(10,20):
# # #     for i in range(2,num):
# # #         if(num%i==0):
# # #             break
# # #     else:
# # #         print(num,'is a prime number')


# # print("Python programming is fun!".rsplit())
# # print("***Python programming is fun***".lstrip('*'))


# c = complex(1,2)
# print(c)
# print(c.real)
# print(c.imag)

# coord = (0,1)
# 'X: {0[0]}; Y: {0[1]}'.format(coord)
# print(coord)

# name = "kavy boricha"
# a = name.index(" ")
# fname = name[:a]
# sname = name[a+1:]

# print(f"{fname} and {sname}")
# print(name[-4:-1:])

# print(name>fname)
# print(name>sname)

# a =set([1,2,3,4,5,6])
# b=set([4,5,6,7,8,9])
# print(b.issubset(a))

# a= {1,2,3,4}
# print(type(a))

# with open("D:\kavy\Python\other\colors.txt","rb") as open_file:
#     for ele in open_file:
#         print("contrent:"+str(ele))

# import pandas as pd

# table = pd.io.parsers.read_table("D:\kavy\Python\other\colors.txt")
# print(table)

# from skimage.io import imread
# from skimage.io import imshow
# from skimage.transform import resize
# from matplotlib import pyplot as py

# file = imread(r"D:\kavy\web desining\logo.png")
# img = imread(file)
# py.imshow(img)
# py.show()

# import pandas as pd
# series = pd.DataFrame([("kavy",1),("jay",2),("kavy",1),("kishan",4)],columns=("name","id"))

# dup = series[series.duplicated()]
# print(dup)
# rm = series.drop_duplicates()
# print(rm)


# import pandas as pd 
# df = pd.DataFrame({'A': [0,0,0,0,0,1,1], 'B': [1,2,3,5,4,2,5], 
# 'C': [5,3,4,1,1,2,3]}) 
# a_group_desc= df.groupby('A').describe()
# print(a_group_desc)

# unstacked = a_group_desc.unstack() 
# print(unstacked)

# import pandas as pd
# car_colors= pd.Series(['Blue', 'Red', 'Green'], dtype='category')
# car_data= pd.Series(pd.Categorical(['Yellow', 'Green', 'Red', 
# 'Blue','Purple'],categories=car_colors, ordered=False))
# print(car_data)
# # car_colors.cat.categories= ["Purple", "Yellow"]
# # car_data.cat.categories= car_colors
# # print()
# # print()
# # print()
# # print(car_data)
# print(car_data.isin[car_data.isin(['Red'])])

# import datetime as dt

# print(str(dt.datetime.now()))
# print(dt.datetime.now().strftime("%a %d %B %Y"))

# import numpy as np
# x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],], [[11,12,13], [14,15,16], [17,18,19],], [[21,22,23], 
# [24,25,26], [27,28,29]]])
# print( x[1,1])
# print (x[:,1,1])
# print (x[1,:,1])
# print ("x=",x[1:2, 1:2])

# import pandas as pd 
# df = pd.DataFrame({'A': [2,3,1], 'B': [1,2,3], 'C': [5,3,4]}) 
# df1 = pd.DataFrame({'A': [4], 'B': [4], 'C': [4]}) 
# df = df._append(df1)
# print(df)
# print()
# df = df.reset_index(drop=True)
# print(df)
# print()
# df.loc[df.last_valid_index() + 1] = [5, 5, 5] 
# print(df)
# print()
# df2 = pd.DataFrame({'D': [1, 2, 3, 4, 5]}) 
# df = pd.DataFrame.join(df, df2) 
# print(df)
# print() 

# import pandas as pd 
# df = pd.DataFrame({'A': [2,3,1], 'B': [1,2,3], 'C': [5,3,4]}) 
# df = df.drop(df.index[[1]]) 
# print (df) 
# df = df.drop('B',1)
# print (df) 

import matplotlib.pyplot as py

# values = [1,2,3,4,5,6,47,8,9,10]
# py.plot(range(1,11),values,"r-:")
# ax = plt.axes()
# ax.set_xlim([1,11])
# ax.set_ylin([1,11])
# ax.set_xticks()
# ax.set_yticks()
# ax.grid()
# py.show()
# plt.savefig("grapg.png",format="png")


# values = [1,2,3,4,5,6]
# colors = [k,g,c,m,r,w]
# lables = [a,b,c,d,e,f]
# explode = [0,0,0,5,6,4]

# py.pie(values,colors=colors,labels=lables,explode=explode,autopct="%1.1f%%",counterclock=True,shadow=true)
# py.title("values:")
# py.show()

# values = [1,2,3,4,5,6]
# colors = [k,g,c,m,r,w]
# width = [1,2,4,5,1,3]
# py.bar(range(0,6),values,colors=colors,width=width,align="center")
# py.title("bar chart:")
# py.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = 20 * np.random.randn(10000)
# print(x)
# print(len(x))
# plt.hist(x,25, range=(-50, 50), align='mid', color='g',label='TestData')
# plt.legend()
# plt.title('Step Filled Histogram') 
# plt.show()

# y = 3 * np.random.randn(5)
# print(y)

# import numpy as np
# import matplotlib.pyplot as plt
# spread = 100 * np.random.rand(100)
# center= np.ones(50) * 50
# flier_high= 100 * np.random.rand(10) + 100 
# flier_low= -100 * np.random.rand(10)
# data = np.concatenate((spread, center, flier_high, flier_low))
# plt.boxplot(data, sym='gd', widths=.50, notch=True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.pylab as plb
# x1 = 5 * np.random.rand(40)
# x2 = 5 * np.random.rand(40) + 25 
# x3 = 25 * np.random.rand(20)
# x = np.concatenate((x1, x2, x3))
# y1 = 5 * np.random.rand(40)
# y2 = 5 * np.random.rand(40) + 25 
# y3 = 25 * np.random.rand(20)
# y = np.concatenate((y1, y2, y3))

# color_array= ['b'] * 50 + ['g'] * 25 + ['r'] * 25 
# plt.scatter(x, y, s=[90], marker='d', c=color_array)
# z = np.polyfit(x, y, 1) 
# p = np.poly1d(z) 
# plb.plot(x, p(x), 'y:')
# plt.scatter(x, y, s=[100], marker='^', c='r') 
# plt.show()

# import datetime as dt
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# df = pd.DataFrame(columns=('Time', 'Sales'))
# start_date= dt.datetime(2015, 7,1)
# end_date= dt.datetime(2015, 7,10)
# daterange= pd.date_range(start_date, end_date)
# for single_date in daterange:
#     row = dict(zip(['Time', 'Sales'],[single_date, int(50*np.random.rand(1))]))
#     row_s= pd.Series(row)
#     row_s.name= single_date.strftime('%b %d') 
#     df = df.append(row_s)
# df.ix['Jul 01':'Jul 07', ['Time', 'Sales']].plot()
# plt.ylim(0, 50)
# plt.xlabel('Sales Date')
# plt.ylabel('Sale Value')
# plt.title('Plotting Time') 
# plt.show()

# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.DiGraph()
# nodes = [1,2,3,4,5,6]
# G.add_nodes_from(nodes) 
# G.add_edge(1, 2)
# G.add_edges_from([(1,4), (4,5), (2,3), (3,6), (5,6)])
# nx.draw_networkx(G)
# plt.show()

# from sklearn.linear_model import LinearRegression
# hypothesis = LinearRegression(normalize=True) 
# hypothesis.fit(X,y)
# print (hypothesis.coef_)


# print(abs(hash("python")) % 1000)

# def hashing_trick(input_string, vector_size=20): 
#     feature_vector= [0] * vector_size
#     for word in input_string.split(' '):
#         index = abs(hash(word)) % vector_size
#         print(index)
#         feature_vector[index] = 1
#         return feature_vector

# a = hashing_trick("python")
# print(len(a))
# print(a)

# sklearn_hashing_trick= txt.HashingVectorizer( n_features=20, binary=True, norm=None) # type: ignore
# text_vector= sklearn_hashing_trick.transform( ['Python for data science','Pythonfor machine learning']) 
# print(text_vector)

# %timeit l = [k for k in range(10**6)]

# import pandas as pd
# data = [1,2,3,4,5]
# data = pd.DataFrame(data)
# print(data.mean())
# print(data.std())

d = {
    "batters":{
        "batter" :
        [{
           "batter":[{
                    "batter" :[{
                        "type" :"regular"
                    }]
           }]
        }]
    }
}

# print(d["batters"]["batter"][0])
# s  = {1,2,3,4,5}
# print(s[0]) // set is unorder

# name = input("enter the name:")
# print(f"name : (string) : {name}")

# name = input("enter the number:")
# name1 = input("enter the number2:")
# print(f"{name+name1}")
# print(5+10)
# import numpy as np
# x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],], [[11,12,13], [14,15,16], [17,18,19],], [[21,22,23], 
# [24,25,26], [27,28,29]]])

# print(x[1,:,1])
# print(x[1:2,1:2])

# import pandas as pd

# d = pd.DataFrame({'a':[1,2,3],'b':[2,3,1],'c':[3,1,2]})
# d1 = pd.DataFrame({'a':[4],'b':[5],'c':[6]})
# print(d)
# df = d.append(d1)
# print(df)

# import pandas as pd 
# df = pd.DataFrame({'A': [2,3,1], 'B': [1,2,3], 'C': [5,3,4]}) 
# df = df.drop(df.index[1]) 
# print (df) 
# df = df.drop('B', 1)
# print (df) 

# import re
# data1 = 'My phone number is: 800-555-1212.' 
# data2 = '800-555-1234 is my phone number.'
# pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# dmatch1 = pattern.search(data1).groups() 
# dmatch2 = pattern.search(data2).groups()
# print(dmatch1)
# print(dmatch2

import numpy as np
import pandas as pd

# s = pd.Series([1,2,3,None,np.nan])
# print(s[s.isnull()])

# arr = np.array(['a','b','c','a','c','c'])
# count = np.char.count(arr,'c').sum()
# print(count)\

import matplotlib.pyplot as plt
import numpy as np

# values = [1,8,3,4,9,6,1,2,9]
# ax = plt.axes()
# ax.grid()
# ax.set_xticks(range(1,10))
# ax.set_yticks(range(1,10))
# plt.title("charts")
# ax.set_xlabel("share")
# ax.set_ylabel("price")
# plt.savefig("im.png",format="png")
# plt.annotate(xy=[2,8],text="second") 
# line1 = plt.plot(range(1,10),values,"r-.s")
# line2 = plt.plot(range(1,10),[8,9,7,5,1,2,6,4,3],"b-.v")
# plt.legend(['first','second'],loc=1)
# plt.show()

# values = [2,6,3,5,4]
# marker = ['a','b','c','d','e']
# colors= ['b', 'g', 'r', 'c', 'y'] 
# exp = (0,0,0.3,0,0.1)
# plt.pie(values,colors=colors,labels=marker,explode=exp,shadow=True,autopct="%1.1f%%")
# plt.title("valkues")
# plt.show()

# x = 20 * np.random.random(100)
# print(x)
# plt.hist(x,range(-50,50),histtype="stepfilled",color='g',align="left")
# plt.legend("Histogram")
# plt.title("hist")
# plt.show()

# spread = 50 * np.random.rand(50)
# print("spread:",spread)
# high = 100 * np.random.rand(10)
# low = -100 * np.random.rand(10)
# center = np.ones(50)
# print("high:",high)
# print("low:",low)
# data = np.concatenate((spread,center,high,low))
# plt.boxplot(data,sym="g*",notch=True,widths=2)
# plt.show()

# x = 50 * np.random.rand(100)
# y = 50 * np.random.rand(100)
# print(f"x={x},y={y}")
# plt.scatter(x,y,s=[100],marker='d',c='r')
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# # Example: Creating a time series dataset
# data = {
#     "Date": pd.date_range(start="2024-01-01", periods=15),  # 10 days starting from Jan 1, 2024
#     "Sales": [120, 150, 170, 130, 160, 180, 200, 190, 210, 220,100,120,210,310,150],  # Example sales data
# }

# # Convert to a DataFrame
# df = pd.DataFrame(data)

# # Plotting the time series
# plt.plot(df["Date"], df["Sales"], marker='o', linestyle='-', color='blue', label="Sales Over Time")
# plt.title("Sales Trend Over Time")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.grid(True)
# plt.legend()
# plt.xticks(rotation=30)
# plt.tight_layout()
# plt.show()

# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt

# # Coordinates for two cities
# city1 = (-77.01, 78.90)  # Washington, D.C.
# city2 = (-118.25, 34.05)  # Los Angeles

# # Create a Basemap
# m = Basemap(projection='merc', llcrnrlat=20, urcrnrlat=50, llcrnrlon=-130, urcrnrlon=-60, resolution='l')

# # Draw map features
# m.drawcoastlines()
# m.drawcountries()
# m.fillcontinents(color='lightgray', lake_color='lightblue')
# m.drawmapboundary(fill_color='aqua')

# # Plot the cities
# x, y = m(*zip(*[city1, city2]))
# m.plot(x, y, 'ro')  # 'ro' = red circles for markers

# # Title and display
# plt.title("Basic Geographic Plot")
# plt.tight_layout()
# plt.show()

# import networkx as nx
# G = nx.DiGraph()


# G.add_nodes_from(range(0, 4))
# G.add_edges_from([(0,1),(0,2),(2,1),(2,3),(3,0)])
# nx.draw_networkx(G)
# plt.show()

# import matplotlib.pyplot as plt

# # Example data
# data = [22, 25, 26, 24, 25, 30, 35, 28, 29, 30, 40, 41, 42, 38, 37]

# # Create a histogram
# plt.hist(data, bins=5,histtype="stepfilled", color='lightgreen', edgecolor='black')
# plt.title("Histogram Example")
# plt.xlabel("Age Groups")
# plt.ylabel("Frequency")
# plt.show()


# import matplotlib.pyplot as plt
# languages = [ 'Java', 'Python', 'PHP','JavaScript', 'C#','C++ ']
# Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7 ]

# plt.pie(Popularity,labels=languages,autopct="%1f%%")
# plt.show()

# import matplotlib.pyplot as plt

# # Data for marks
# Maths = [100, 82, 76, 51, 88]
# Physics = [92, 89, 81, 83, 80]
# Chemistry = [71, 90, 75, 88, 45]

# # Combine data for plotting
# data = [Maths, Physics, Chemistry]

# # Create a boxplot
# plt.figure(figsize=(8, 6))
# plt.boxplot(data, labels=['Maths', 'Physics', 'Chemistry'], patch_artist=True)
# plt.title("Boxplot of Marks in Three Subjects")
# plt.ylabel("Marks")
# plt.xlabel("subject")
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()


# import matplotlib.pyplot as plt
# temp = [30, 34, 35, 32, 38, 26, 29, 45, 42, 32, 40, 
# 33, 36, 34, 36]

# plt.hist(temp,bins=5)
# plt.title("Tempreture graph")

# plt.show()

# import matplotlib.pyplot as plt

# # Temperature data
# temp = [30, 34, 35, 32, 38, 26, 29, 45, 42, 32, 40, 33, 36, 34, 36]

# # Create a histogram with 4 bins
# plt.figure(figsize=(8, 6))
# plt.hist(temp, bins=4, color='skyblue', edgecolor='black', alpha=0.7)

# # Add labels and title
# plt.title("Histogram of Average Temperature")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Frequency")
# plt.grid(axis='y', linestyle='-.', alpha=0.7)
# plt.show()


# print(hash('pythonsxscdscdsvc') % 100)
# import pandas as pd
# i = {1,2,3,4,5,6,7,8,9}
# print(max(i) - min(i))
# print()


# j = [1,2,3,4,5,6,7,8,9]
# print(j.std())

# for j in range(1,5):
#     print("*"*j)

# for i in range(1,8):
#     for j in range(i,-1,-1):
#         print(pow(2,j),end=" ")
#     print()

# x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],], [[11,12,13], [14,15,16], [17,18,19],], [[21,22,23], 
# [24,25,26], [27,28,29]]])

# print( x[1,1])
# print (x[1:2, 1:2])


# def prime(num):
#     for i in range(2,num - 1):
#         if(num%i == 0):
#             return 1
#         else:
#             return 0
        

# num = int(input("Enter the number:"))
# if(prime(num)==0):
#     print("num is prime")


# import pandas as pd 
# import numpy as np 
# df = pd.DataFrame({'A': [2,1,2,3,3,5,4], 'B': [1,2,3,5,4,2,5], 'C': [5,3,4,1,1,2,3]}) 
# df = df.sort_index(by=['A', 'B'], ascending=[True, True]) 
# df = df.reset_index(drop=True)
# print (df) 
# index = df.index.tolist() 
# np.random.shuffle(index)
# df = df.ix[index]
# df = df.reset_index(drop=True) 
# print() 
# print (df)

# import numpy as np
# import matplotlib.pyplot as plt
# x = 20 * np.random.randn(10000)
# plt.hist(x, 25, range=(-50, 50), histtype='stepfilled', align='mid', color='g',label='Test Data')
# plt.legend()
# plt.title('Step Filled Histogram') 
# plt.show()


a = [2,5,3,1,4,9,52,45,100,8]

for i in range(1,10):
    for j in range(0,10-i):
        if(a[j]>a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
        
print(a)
