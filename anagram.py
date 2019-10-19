import avl
import red_black


def print_anagrams(english_words, word, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if str in english_words:
            print(prefix + word)
        else:
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                print_anagrams(english_words, before + after, prefix + cur)


def greatest_anagrams(english_words):
    greatest = []
    for word in english_words:
        if not greatest:
            greatest.append(word)
            greatest.append(_count_anagrams(english_words, word, []))
        else:
            count = _count_anagrams(english_words, word, [])
            if count > greatest[1]:
                greatest[0] = word
                greatest[1] = count
    print(greatest[0], 'has the greatest number of anagrams with a total of', greatest[1])


def count_anagrams(english_words):
    print("Count anagrams of: ")
    word = input()
    word = word.replace("\n", "")
    print('Total anagrams of ', word, ': ', _count_anagrams(english_words, word, []))


def _count_anagrams(english_words, word, li, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        if english_words.contains(str):
            li.append(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                _count_anagrams(english_words, before + after, li, prefix + cur)
    return len(li)


def get_avl_tree():
    english_words = avl.AVL()
    file = 'tops.txt'
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            english_words.insert(curr_line)
    return english_words


def get_rb_tree():
    english_words = red_black.RBTree()
    file = 'tops.txt'
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            english_words.insert(curr_line)
    return english_words


def main():
    print('1. AVL Tree')
    print('2. Red-Black Tree')
    type_tree = input()
    print('1. Count Anagrams')
    print('2. Greatest Num of Anagrams')
    response = input()
    if type_tree is '1':
        english_words = get_avl_tree()
    elif type_tree is '2':
        english_words = get_rb_tree()
    else:
        print('Invalid option')
        return
    if response is '1':
        count_anagrams(english_words)
    elif response is '2':
        greatest_anagrams(english_words)
    else:
        print('Invalid option')


main()
