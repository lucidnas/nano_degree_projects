import time
import webbrowser


breaks = 3

while breaks > 0:
    time.sleep(10)
    print "Break time!"
    webbrowser.open("https://www.youtube.com/watch?v=WyGq6cjcc3Q")
    breaks = breaks - 1
    

