an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): ")) 

for char in word:
    if char in an_letters:
        print(f'give me {char}')
    else:
        print(f"give me {char}")

