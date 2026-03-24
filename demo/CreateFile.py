class FileObject:
    def __init__(self, name, content):
        self.name = name
        self.content = content
    def read(self):
        return self.content

def readFile(name, content):
    file = FileObject(name, content)
    print(f"{file.content}{file.name}")

if __name__ == '__main__':
    readFile("test.txt", "Hello World")
