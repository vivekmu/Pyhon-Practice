
try:
    # f = open("message.txt", "r")
    f = open("E:\Python\FileHandling\message.txt", "r")

    content = f.read()
    # content = f.read(6)
    print(content)

except FileNotFoundError:
    print("No such a file or directory found here")

finally:
    f.close()

#close the file "with" and no need of explicit close
with  open("E:\Python\FileHandling\message.txt", "r") as f1:
    content = f1.read(6)
    print(content)

#python writing a file

with open("E:\Python\FileHandling\message1.txt","w") as f2:
    f2.write("Python is a cool language\n")
    f2.write("I love reading")

#python appending a file
with open("E:\Python\FileHandling\message1.txt","a") as f2:
    f2.write("\nPython is awesome")

#python readlines from file
with open("E:\Python\FileHandling\message1.txt","r") as f3:
    lines = f3.readlines()
    print(lines)

#python writelines to file
with open("E:\Python\FileHandling\javascript.txt","w") as f4:
    lines = ['JS is also awesome', '\nJS is my second programming language.']
    f4.writelines(lines)


