#Author: Md. Obaydullah
#Date: 2026--07
#auto fill was enabled but suggestion not taken
words = ["hi", "python", "is", "cool", "code", "a"]

is_long = lambda word: len(word) > 3

big_words = [word for word in words if is_long(word)]

print(big_words)