import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
#default values
a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"

#calculates your income per monthly
income = float(input("Net income per month? "))
inc_5 = float(income * 0.05)
inc_10 = float(income * 0.1)
inc_25 = float(income * 0.25)
inc_35 = float(income * 0.35)
inc_15 = float(income * 0.15)

#the dictionary that the dataframe will be based on
info = {"Average amount": [(inc_25 + inc_35) / 2, (inc_10 + inc_15) / 2, (inc_10 + inc_15) / 2, (inc_5 + inc_10) / 2, (inc_10 + inc_25) / 2, (inc_5 + inc_10) / 2], "Money Spent": [a, b, c, d, e, f], "Surplus/Deficit": [a, b, c, d, e, f]}
data = pd.DataFrame(info)
data.index = ["Housing", "Transportation", "Food", "Utilities", "Insurance", "Medical + Health Care"]

h = float(input(f"How much money do you spend on Housing per month? "))
t = float(input(f"How much money do you spend on Transportation per month? "))
fed = float(input(f"How much money do you spend on Food per month? "))
u = float(input(f"How much money do you spend on Utilities per month? "))
i = float(input(f"How much money do you spend on Insurance per month? "))
m = float(input(f"How much money do you spend on Medical per month? "))  
    
data["Money Spent"].replace({a: h, b: t, c: fed, d: u, e: i, f: m}, inplace=True)

data["Surplus/Deficit"].replace({a: (inc_25 + inc_35) / 2 - h, b: (inc_10 + inc_15) / 2 - t, c: (inc_10 + inc_15) / 2 - fed, d: (inc_5 + inc_10) / 2 - u, e: (inc_10 + inc_25) / 2 - i, f: (inc_5 + inc_10) / 2 - m}, inplace=True)

info.get("Average amount"[0])

n = data["Money Spent"] 

money = data["Money Spent"].sum()
average = data["Average amount"].sum()
if money > income:
  print(f"You are spending money at a rate quicker than you can produce. Your are {income - money} dollars in debt")
else:
  print(f"You have saved {income - money}, you could use this on savings, debt payment, recreation etc.")  

print(data)

#This part is an explanation (optional)
print("The Average amount column show an approximate amount of money that should be spent on each category based off of your monthly income")
print("The money spent column is how much money you spend on each category per month")
print("The surplus/deficit shows if you are spending more or less than the average and by how much. if the number is negative, your spending is over the average of that category.")
print("If you spend the average, you have remainder money that can be used for nonessential categories.")

graph = data.plot.bar(rot=0, stacked=True)
plt.show()