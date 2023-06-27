def clean(sentence):
    cleaned = ""
    for character in sentence:
        if character.isalnum():
            cleaned = cleaned + character
    return cleaned

def reverse():
    sentence = "li.l"
    cleaned = clean(sentence)
    reversed = ""
    for character in cleaned:
        reversed = character + reversed
    for i in range(len(cleaned)):
        if cleaned[i] == reversed[i]:
            continue
        else:
            print("It is not a palindrome.")

reverse()