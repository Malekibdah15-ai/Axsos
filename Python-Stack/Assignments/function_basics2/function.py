#1
def count(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
print (count(5))
        

#2
def result_pm(num):
    i = 0
    while i < 2:
        if i == 0:
            print (num[i])
        elif i == 1:
            return num[i]
        i +=1

result_pm([5,7])

#3
def list_sum(numbers):
    return numbers[0]+ len(numbers)

result = list_sum([5, 10, 15])
print (result)

#4
def values(numbers):
    print(numbers)
    seconed_value=numbers[1]
    result = []
    for i in range(len(numbers)):
        if numbers[i] > seconed_value:
            result.append(numbers[i])
            return result
numbers=[1,2,3]
print(values(numbers))

#5
def length_value(a,b):
    list = [] 
    for i in range(0,a,1):
        list.append(b)
    return list
print(length_value(3, 4))

def count(nums):
    list = []
    for i in range (5, -1, -1):
        list.append(i)
    return list
print(count(5))