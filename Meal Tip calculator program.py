mealcost = float(input("Please enter the cost of your meal"))
tip = float(input("Please enter the % tip required"))
tipcost = (mealcost) * (tip) / 100
Total = (mealcost) + (tipcost)
print("This is the cost of your tip: {0:.2f} and This is the total cost of your meal: {1:.2f}".format(tipcost,Total))
