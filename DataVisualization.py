import pandas as pd
from matplotlib import pyplot as plt

''' sample 1
x = [1,2,3]
y = [1,4,9]
z = [10,5,0]

plt.plot(x,y)
plt.plot(x,z) # jika ingin ada 3 line 

plt.title("test plot") #to create a title
plt.xlabel("x") #to create label in x
plt.ylabel("y and z") #to create label in x

plt.legend(["this is x","this is z"]) #untuk membuat note pada garis
#plt.show()

'''

'''sample 2
sample_data = pd.read_csv('sample_data.csv')
#print(type(sample_data)) #untuk mengetahui tipe data dari variabel, disini sample data menggunakan Dataframe

print(sample_data) #untuk mengetahui seluruh data 
print(sample_data.column_c) #untuk mengetahui value dari spesific kolom
print(sample_data.column_c.iloc[0]) # untuk mendapatkan value dari index 0 
print(sample_data.column_c.iloc[1]) # untuk mendapatkan value dari index 1
print(sample_data.column_c.iloc[2]) # untuk mendapatkan value dari index 2

plt.plot(sample_data.column_a, sample_data.column_b,'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()
'''

#sample 3
data = pd.read_csv('countries.csv')
#print(data)

# print(data.country == 'United States') #untuk mengecek setiap row == united state
# compare the population growth in the us and china
us = data[data.country == 'United States']
china = data[data.country == 'China']

'''
plt.plot(us.year,us.population/10**6)
plt.plot(china.year,china.population/10**6)
plt.legend(['United States','China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()
'''

#untuk mengetahui persentase growth(logic) dalam persentase, populasi dibagi dengan populasi tahun pertama x 100%
plt.plot(us.year,us.population/us.population.iloc[0] * 100)
plt.plot(china.year,china.population/china.population.iloc[0] * 100)
plt.legend(['United States','China'])
plt.xlabel('year')
plt.ylabel('population growth(first year = 100)')
plt.show()







