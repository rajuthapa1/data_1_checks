# task 1
greeting = "Hello, World!"
print(greeting)

#task 3
my_disc = {"Make":"Tesla", "Model": "Y"}
print("select - Make or Model")
index = input("Make a selection from above list: ")
if (index == "make"):    
    text = my_disc["Make"]  
else:
    text = my_disc["Model"]    
print(text)