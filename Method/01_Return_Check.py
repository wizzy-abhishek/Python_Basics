def multiple(word):
    if not any(char.isupper() for char in word):
        return False
    if not any(char.isdigit() for char in word):
        return 'Hello'
## by default it returns None, if none of the if works.

print(multiple("A"))