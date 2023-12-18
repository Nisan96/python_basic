'''
Textfile = open("Text.txt",'w')
Textfile.write("Python is interpreted language\n")
Textfile.write("Python is a awesome language\n")
Textfile.write("Python is great for automation\n")

Textfile.close()
'''
'''
Textfile = open("Text.txt",'a')
Textfile.write("automation is crucial for software testing")
Textfile.close()
'''
'''
with open("Text.txt",'r') as Textfile:
    print(Textfile.read())
    Textfile.close()
'''
'''
with open("Text.txt",'r+') as Textfile:
    print(Textfile.read())
    Textfile.write("\nHello world")
    Textfile.close()
'''
with open("Text.txt",'r+') as Textfile:
    for line in Textfile:
        print(line)















