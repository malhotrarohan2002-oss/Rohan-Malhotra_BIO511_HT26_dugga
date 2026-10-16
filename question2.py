#a)
my_list =[1,5,"4","six",3.14]

for items in my_list:
    try:
        new_list = int(items)
        print(new_list)

    except(ValueError,TypeError):
        print(f"Cannot convert {items} to an integer.")

#b)
def clean_list(items):
    new_list = []

    for item in items:
        try:
            new_list.append(int(item))
        except(ValueError,TypeError):
            print(f"Cannot convert {item} to an integer.")

    return new_list
new_list = clean_list(my_list)
print(new_list)

#c 
def sum_neighbours(numbers):       
    sums=[]

    for i in range(len(numbers)-1): ##AI help
        sums.append(numbers[i]+ numbers[i+1])
    return sums
print(sum_neighbours(new_list))
            

