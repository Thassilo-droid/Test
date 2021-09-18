FileName = input("Wie wollen Sie ihr file nennen?: ")

while FileName != "":
    FileContent = input(f'Was wollen Sie in { FileName} schreiben? ')
    if FileContent != "":
        NewFile = open("C:\\Users\\thass\\Desktop\\"+FileName+".txt", "a")
        NewFile.write(FileContent+"\n")
        NewFile.close()
    else:
        break
