import csv
import os

class FileObject:
    def __init__(self, name, content):
        self.name = name
        self.content = content
    def read(self):
        return self.content

def readFile(name, content):
    file = FileObject(name, content)
    print(f"{file.content}{file.name}")

def writeFileToCsv(name, content):
    file_exists = os.path.exists('test.csv')
    
    with open('test.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['name', 'content'])
        writer.writerow([name, content])
    print(f"数据已追加到 test.csv")

if __name__ == '__main__':
    readFile("test.txt", "Hello World")
    writeFileToCsv("示例文件", "这是一段测试内容")
