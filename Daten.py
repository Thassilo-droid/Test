A = open("huch.py", "rb+")
A.seek(3)
A.seek(10, 1)
print(A.read())
A.close()
