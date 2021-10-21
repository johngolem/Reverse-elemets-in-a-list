

names = ["john", " ", "paul", " ", "odero", " ", "is", " ", "my" " ", "name",
         " ", "Moringa", " ", "is", " ", "the", " ", "bootcamp", " ", "togo"]
newstri = " "


def reverse_words(names):
    newstri = ""
    for word in names:
        newstri += word
        # creating a new string by adding every word in the list

    print(newstri)
  # after splitting the new string to form a sentence, we split it into individual words and then reverse the words.
    # This avoid direct reversal
    split_words = newstri.split()[::-1]
    print(split_words)

    # to rejoing the splits after reversing to form a reversed sentence
    reversee = " ".join(split_words)

    print(reversee)
    names = []
    for noun in split_words:
        names.append(noun)

    return names


print(reverse_words(names))
