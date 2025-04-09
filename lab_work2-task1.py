slava = str("Слава Україні")
geroy = str("Героям Слава!")
print(slava,geroy)
new = slava + geroy
print(new)
print(slava, geroy, sep="\t")
print(new * 3)
slava_words = slava.split()
geroy_words = geroy.split()

for word in slava_words:
    print(word)

for word in geroy_words:
    print(word)

print(slava[::-1])
print(geroy[::-1])

print(new + "!")