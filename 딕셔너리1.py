manga = {"Pokemon": "Pikachu",
 "Digimon": "Agumon",
 "Yugioh": "Black Magician"
 }
word = input()
print(manga.get(word, "I don't know"))

# word = input()
# if word in manga:
#     print(manga[word])
# else:
#     print("I don't know")