import avl
import red_black


def red_black_tree():
    print('do something')


def print_anagrams(english_words, word, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if str in english_words.root:
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
    for word in english_words.root:
        if not greatest:
            greatest.append(word.key)
            greatest.append(counting_anagrams(english_words, word.key, []))
        else:
            count = counting_anagrams(english_words, word.key, [])
            if count > greatest[1]:
                print(word.key)
                greatest[0] = word.key
                greatest[1] = count
    print(greatest)
    return 0


def count_anagrams(english_words):
    print("Count anagrams of: ")
    word = input()
    print('Total anagrams of ', word, ': ', counting_anagrams(english_words, word, []))


def counting_anagrams(english_words, word, li, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if str in english_words.root:
            li.append(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                counting_anagrams(english_words, before + after, li, prefix + cur)
    return len(li)


# for personal testing: https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
# Link above provides a visualization for insertion (has to be manually inserted though)
def avl_option():
    english_words = avl.AVL()
    file = 'example.txt'
    with open(file) as f:
        for curr_line in f:
            curr_line = curr_line.replace('\n', '')
            english_words.insert(curr_line)
    print('1. Count Anagrams')
    print('2. Greatest Num of Anagrams')
    response = input()
    if response is "1":
        count_anagrams(english_words)
    elif response is "2":
        greatest_anagrams(english_words)
    else:
        print('Invalid Option')


def main():
    print('1. AVL Tree')
    print('2. Red-Black Tree')
    type_tree = input()
    if type_tree is "1":
        avl_option()
    elif type_tree is "2":
        red_black_tree()
    else:
        print('Invalid Option')


main()
