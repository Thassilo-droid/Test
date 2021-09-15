import time

l = 0
while l < 50:
    l += 1
    time.sleep(0.5)
    print("\a")
    b = open(r"C:\Users\thass\Desktop\LOL"+ str(l) +".txt" , "w")
    b.write("Du bist dumm!")
    b.close()
