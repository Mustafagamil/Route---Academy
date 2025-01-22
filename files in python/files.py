# Write a Python program to read an entire text file.
f = open("session.txt", "r")
print(f.read())

# write program to find longest word
f = open('session.txt', mode='r')
s=f.read()
words = s.split()
max_len = len(max(words, key=len))
for word in words:
    if len(word)==max_len:
        longest_word=word
print(longest_word)


# write program to find n of lines of the file
n = int(input("\n\t\tEnter Lines To Read : "))
f = open("session.txt", "r")
for i in range(n):
 print(f.readline())

 # import module
 import shutil

 # use copyfile()
 shutil.copyfile('session.txt.', 'session2.txt.')

