a=[]
x=int(input("Enter the number of elements: "))
for i in range (x):
    m=int(input("Enter the elements: "))
    a.append(m)
print("Unsorted list: ",a)

def SelectionSort():
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if(a[min]>a[j]):
                min=j
        a[i],a[min] = a[min],a[i]
    print("Selection sorted list: ",a)
SelectionSort()