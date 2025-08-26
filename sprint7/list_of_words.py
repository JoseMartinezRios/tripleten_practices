#list_of_words.py

def list_of_words(text: str, sep: str = " ") -> list:
    return text.split(sep)

list_of_words("Mary had a little lamb", sep="a")
print("Hola en list_of_words.py")

