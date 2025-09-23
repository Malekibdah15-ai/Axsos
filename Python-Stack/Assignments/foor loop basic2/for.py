# # # 1
def biggie_size(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 0:
            numbers[i] = "big"
    return numbers
result = biggie_size([-1, 3, 5,-1])
print(result) 

#2
def postive_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    numbers[-1] = count
    return numbers
result = postive_numbers([1, -3,-2,-1 ])
print (result)

#3
def sum_total(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(sum_total([1, 2, 3, 4]))

#4 
def average(numbers):
    if len(numbers) == 0:
        return (0)
    total = 0
    for num in numbers:
        total += num
    count = len(numbers)
    avg = total / count
    return avg
result = average([1,2,3,4])
print(result)

5
def list_length(list):
    count = 0
    for i in list:
        count += 1
    return count
result = list_length([2,5,10,3])
print(result)

#6
def mini_list(list):
    if list == 0: 
        return False
    main_value = list[0]
    for i in list:
         if i < main_value:
             main_value = i
    return main_value
result = mini_list([4,6,3,-2])
print (result)

#7
def maximum(list):
    if list == 0:
        return False
    x = list[0]
    for i in list:
        if x > i:
            x = list[0]
    return x
result = maximum([47, 2, 3, -9])
print(result)

8
def Analisis(numbers):
    if not numbers:
        return False
    result = {
        'sumTotal': sum(numbers),
        'average': round(sum(numbers) / len(numbers), 2), 
        'minimum': min(numbers),
        'maximum': max(numbers),
        'length': len(numbers)
    }
    return result

print(Analisis([37, 2, 1, -9]))  
print(Analisis([]))  

#9
def list(numbers):
    left = 0
    right = len(numbers)-1
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
        return numbers

print(list([37, 2, 1, -9]))

    

