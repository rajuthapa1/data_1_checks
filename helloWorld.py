# task 1
greeting = "Hello, World!"
print(greeting)

# task 2
my_list = ["apple", "orange", "mango", "banana"]
index = input("Input from 1-4 and see fruits selected: ")
index = int(index) - 1
print(my_list[index])

#task 3
my_disc = {"Make":"Tesla", "Model": "Y"}
print("select - Make or Model")
index = input("Make a selection from above list: ")
if (index == "make"):    
    text = my_disc["Make"]  
else:
    text = my_disc["Model"]    
print(text)