def reverse(input_string):
    words=input_string.split()
    reversed_words=words[::-1]
    reverse_string=' '.join(reversed_words)
    return reverse_string
user_input=input("enter a sttring ")
reversed_string=reverse(user_input)
print(reversed_string)




