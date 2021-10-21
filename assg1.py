#names = ["john", "", "paul", "", "odero", "", "is", "", "my", "", ]
# "name", "", "opiyo", "", "peter", "", "is", "", "my", "", "dad"]
A = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']
STR = " "

# A = ['t','h','i','s',' ','i','s',' ','g','o','o','d'] reverseSentence(A) A // ['g','o','o','d',' ','i','s',' ','t','h','i','s']


def reverse(A):
    string = ""
    # create a string from passed list
    for element in A:
        string += element

    print(string)

    # split string
    splits = string.split()[::-1]

    print(splits)
    # to join splits to form sentence
    new_string = " ".join(splits)
    print(new_string)
    A = []
    for character in new_string:
        A.append(character)

    return A


print(reverse(A))
