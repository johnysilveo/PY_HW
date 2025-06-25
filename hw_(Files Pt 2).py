import pickle
from itertools import zip_longest


# text_py = "Python is widely known for its flexibility, especially when compared to Java. Python’s simple syntax and dynamic typing allow for faster development and easier debugging. Unlike Java, which is verbose and strictly object-oriented, Python supports multiple paradigms, including procedural and functional programming. This makes Python more adaptable for different tasks like scripting, automation, or AI. Python’s vast library ecosystem also speeds up development. While Java is better for large, structured systems, Python offers quick solutions and rapid prototyping. Developers often choose Python for its readability and ease of use. In short, Python provides flexibility where Java can feel rigid."
# with open('python.txt','wb') as file:
#     pickle.dump(text_py,file)

def change_py(word1,word2):
    with open('python.txt','rb') as file:
        content = pickle.load(file)
        edited = content.lower().replace(word1,word2)
        with open('python.txt','wb') as file:
            pickle.dump(edited,file)
change_py('python','java')


def count_chars_in_lines():
    with open('data.txt', 'rb') as file:
        content = pickle.load(file)
        lines = content.splitlines()

        result = []
        for i, line in enumerate(lines, 1):
            result.append(f"Line {i}: {len(line)} characters")

    with open('char_count.txt', 'wb') as pedofile:
        pickle.dump(result, pedofile)


def compare(file1,file2):
    with open('text11.txt', 'rb') as file1, open('text22.txt', 'rb') as file2:
        data1 = pickle.load(file1)
        data2 = pickle.load(file2)
        words1 = data1.split()
        words2 = data2.split()
    for i, (word1, word2) in enumerate(zip_longest(words1, words2, fillvalue='---missing---'), start=1):
        if word1 != word2:
            print(f'Mismatch at line {i}:')
            print('File1:', word1)
            print('File2:', word2)




