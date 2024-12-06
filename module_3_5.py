def get_multiplied_digits(number): #1
    str_number = str(number) #2

    if len(str_number) > 1:
        first = int(str_number[0]) #3
        return first * get_multiplied_digits(int(str_number[1:])) #4
    else:
        return int(str_number)


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(4020301)
print(result2)