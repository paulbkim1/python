# 1. Countdown
def countdown (num):
    count = []
    for i in range(num, -1, -1):
        count.append(i)
    return count
print(countdown(10))

# 2. Print and Return
def print_and_return(a):
    print(a[0])
    return a[1]

print(print_and_return([1,2]))

# 3. First Plus Length
def sum_len (a):
    summ = a[0] + len(a)
    return summ
print(sum_len([1,2,3,4,5]))

# 4. Values Greater than Second
def values_greater (a):
    new_list = []
    if (len(a) > 2):
        for i in range(0,len(a)):
            if a[1] < a[i]:
                new_list.append(a[i])
        return new_list
    else:
        return False
print(values_greater([5, 2, 3, 2, 1, 4]))

# 5. This Length, That Value
def length_value(a,b):
    new_list = []
    for i in range(0,a):
        new_list.append(b)
    return new_list


print(length_value(6,2))