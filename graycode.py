def gray_code(n):
    if n == 0:
        return ["0"]
    if n == 1:
        return ["0", "1"]
    
    # Get the gray code for n-1
    previous_gray = gray_code(n - 1)
    # Create the new list with 2^n elements
    new_gray = []
    
    # Add a 0 to the beginning of each code from the previous list
    for code in previous_gray:
        new_gray.append("0" + code)
    
    # Add a 1 to the beginning of each code from the reversed previous list
    for code in reversed(previous_gray):
        new_gray.append("1" + code)
    
    return new_gray

array = gray_code(int(input()))
for val in array:
    print(val)