
# Question 2:
def nested_list(n):
    if not(isinstance(n,int)):
        raise ValueError(f"The value ({n=}) you entered must be an integer.")
    elif n == 0:
        return []
    elif n > 0:
        output = [[1]]
        for i in range(1, int(n)):
            output.append(output[-1] + [i+1])
    else:
        output = [[-1]]
        for i in range(1, int(-n)):
            output.append(output[-1] + [-i-1])
    return output
