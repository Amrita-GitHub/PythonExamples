# Dealing with an indefinite number of positional arguments
#function to find the maximum in a list of numbers

def maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
           if n > maxnum:
                maxnum = n
        return maxnum

print(maximum(3,6,1,9))


