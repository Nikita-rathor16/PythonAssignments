input_String=input("enter any string ")
words = input_String.strip('"').split()
reversed_string = ' '.join(reversed(words))
result = f'"{reversed_string}"'
print(result)