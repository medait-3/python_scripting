import re 

content = "i game m a devloppeur im goodm gameg"
word = "good"
sp = "\s"
regex = "go\w*"
f=input('your word : ')

def findword(word, str):
    content= re.findall(word, str)
    print(content)

findword(word, content)


def splitstr(sp, str):
    content= re.split(sp, str)
    print(content)

splitstr(sp, content)


def findword(regex, str):
    content= re.findall(regex, str)
    print(content)

findword(regex, content)


def findword(f, str):
    content= re.findall(f, str)
    print(content)

findword(f, content)
