


no_of_students = int(input("Enter number of students Whose marks are to be filled : "))
FDS = {}
FDS_absent = {}

for i in range (0,no_of_students):
    name = input("Name Of Student : ")
    ask = input("Is student Present or Absent (P/A) : ")
    if (ask == "P"):    
        marks = int(input("Enter Marks (out of 100): "))
        FDS[name]=marks
    elif(ask=="A"):
        FDS_absent[name]="Abesnt"
        
    else:
        pass

print(FDS_absent)
values = FDS.values()

keys = FDS.keys()

# Average marks
avg = sum(values)/len(values)
print("Average of marks are : ",avg)

# highest score of class
highest = max(values)
print("Highest Score of class : ",highest)


low = min(values)
print("Lowest Score of class : ",low)

new_list = list(FDS.values())
# print(new_list)

count = {}
for i in new_list:
    count[i]=count.get(i,0)+1


val = count.values()
key = count.keys()
print(max(key)," : ",max(val))


