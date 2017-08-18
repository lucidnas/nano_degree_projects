import urllib

def read_text():
    quotes = open('C:\Python\movies_quotes.txt')
    quote = quotes.read()
    print quote
    quotes.close()
    check_profanity(quote)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    print(connection.read())
    connection.close()
read_text()