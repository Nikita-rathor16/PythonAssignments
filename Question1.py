def OccurenceCharcters(input_string):
    char_count = {}
    for char in input_string:
        if char.isalpha(): 
            char_count[char] = char_count.get(char, 0) + 1
    
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    for i in range(min(3, len(sorted_chars))):
        print(f"{sorted_chars[i][0]}: {sorted_chars[i][1]}")

input_string =input("enter any string ")
OccurenceCharcters(input_string)