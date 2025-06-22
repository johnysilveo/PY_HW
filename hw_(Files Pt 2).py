import pickle

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

def count_line_s():
    with open('python.txt','rb') as file:
        content = pickle.load(file)
        content_m = content.splitlines()

        for line in content_m:



