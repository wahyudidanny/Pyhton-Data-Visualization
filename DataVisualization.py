import pandas as pd
from matplotlib import pyplot as plt

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


sample_data = pd.read_csv('sample_data.csv')
#print(type(sample_data)) #untuk mengetahui tipe data dari variabel, disini sample data menggunakan Dataframe

print(sample_data) #untuk mengetahui seluruh data 
print(sample_data.column_c) #untuk mengetahui value dari spesific kolom
print(sample_data.column_c.iloc[0]) # untuk mendapatkan value dari index 0 
print(sample_data.column_c.iloc[1]) # untuk mendapatkan value dari index 1
print(sample_data.column_c.iloc[2]) # untuk mendapatkan value dari index 2
