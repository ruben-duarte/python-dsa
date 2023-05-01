def linear_complex(list):
    sum = 0   #O(1)
    mult = 1  #O(1)

    for number in range(len(list)):    #O(n)
        sum  += number

    for number in range(len(list)):   #O(n)
        mult *= number
    #O(n) + O(n) + O(1) + O(1) : O(2n) : O(n)
    return sum, mult

number_list= [3,4,5]

result = linear_complex(number_list)
print(result)