import os

def read_text():
    quotes = open('C:\Python\movies_quotes.txt')
    print(quotes.read())
    quotes.close()

read_text()