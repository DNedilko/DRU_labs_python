
# FIRST TASK
def str_to_dict(some_str):
    some_dict={}
    for i in some_str:
        some_dict[i]=some_str.count(i)
    return some_dict

print('Str to dict:', str_to_dict('dataroot_university'))
# Second task
def sec_smallest(numbers):
    get_list=[]
    length= len(numbers)
    for i in range(length):
        for j in range(0,length-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    for i in range(0,length-1):
        if numbers[i]!=numbers[i+1]:
            get_list.append(numbers[i])
    return get_list[1]
    
print('Sec_smallest: ', sec_smallest([1, 2, -8, -8, -2, 0]))
# Task 3
def prime_nums(n):
    prime_numbers=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    list_n=[]
    for i in range(0, len(prime_numbers)-1):
        if prime_numbers[i]<n:
            list_n.append(prime_numbers[i])
        else:
            return list_n

print('Prime numbers: ', prime_nums(30))

# task4
def max_sum_index(tuples):
    max_sum=0
    index=0
    for i in range (0,len(tuples)-1):
        temp_sum=0
        for j in tuples[i]:
            temp_sum+=j
        if temp_sum>max_sum:
            max_sum = temp_sum
            index = i

    return index

print('Index: ', max_sum_index([(10, 20, 1, 2), (51, 32), (30, 25, 5)]))
print('Index: ', max_sum_index([(47, 22, 11), (23, 17)]))


# TAsk5
def gcd(x,y):
    while (y>0):
        x,y=y,x%y
    return x

print('GCD: ', gcd(160, 188))

#Task6
def recursive_list_sum(data_list):
    list_sum=0
    for i in data_list:
        if isinstance(i,list):
            list_sum+=recursive_list_sum(i)
        else:
            list_sum+=i
    return list_sum

print('The sum of a list is ', recursive_list_sum([1, 2, [3, 4], [5, 6], [7, 8, 9, [10]]]))

# Task7
