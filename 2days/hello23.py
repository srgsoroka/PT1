f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

f=open("demofile2.txt","rt")

print(f.tell())

print(f.read())
print(f.read())
