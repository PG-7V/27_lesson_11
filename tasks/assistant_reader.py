import os
from chardet.universaldetector import UniversalDetector

class Reader:

    def __init__(self, path_folder, search_str=input("Enter search str:")):
        self.path_folder = path_folder
        self.search_str = search_str
        self.books = []

    def serch_str_to_file(self, file_name):
        detector = UniversalDetector()
        with open(file_name, 'rb') as fn:
            for line in fn:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()

        with open(file_name, encoding=f"{detector.result.get('encoding')}") as f:
            if self.search_str in f.read():
                self.books.append(file_name)

    def check_books(self):
        count = 0
        print(len(os.listdir(self.path_folder)))
        for file in os.listdir(self.path_folder):
            print(count)
            self.serch_str_to_file(f"{self.path_folder}/{file}")
            count += 1

        print(*self.books, sep='\n')

a = Reader('/home/dima/Рабочий стол/books_by_tim/books')
a.check_books()




