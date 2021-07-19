
''' FIRST TASK
def str_to_dict(some_str):
    some_dict={}
    for i in some_str:
        some_dict[i]=some_str.count(i)
    return some_dict

print(str_to_dict('dataroot_university'))
'''
# Second task
'''
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
'''
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