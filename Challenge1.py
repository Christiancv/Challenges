letter = input("please enter a phrase: ")
phrase = list(letter)

for let in phrase:

    if " " in let:
        new_word = chr(ord(let))
    elif "y" in let:
        new_word = chr(ord("a"))
    elif "z" in let:
        new_word = chr(ord("b"))
    else:
        new_word = chr(ord(let) + 2)
    print(new_word, end="")


