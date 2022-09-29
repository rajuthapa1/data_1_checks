#task 3
my_vehicle = {"Make":"Tesla", "Model": "Y"}
print("select - Make or Model")
index = input("Make a selection from above list: ")
if (index == "make"):    
    text = my_vehicle["Make"]  
else:
    text = my_vehicle["Model"]    
print(text)