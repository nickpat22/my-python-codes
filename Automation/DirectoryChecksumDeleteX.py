import sys
import os
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0 ):
        hobj.update(Buffer)
        Buffer = fobj.read(1024) #beacuse of no wasted of space
    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    ret = False

    ret = os.path.exists(DirectoryName)

    if ret == False:
        print("Path is Invalid")
        return

    ret = os.path.isdir(DirectoryName)

    if ret == False:
            print("It is not a Directory")
            return 
    Duplicate = {}

    Unique = 0
    Same = 0

    for FolderName, SubFolder, Filename in os.walk(DirectoryName):
        for fname in Filename:
            fname = os.path.join(FolderName, fname)

            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                
                Duplicate[Checksum].append(fname)
            else:
               
                Duplicate[Checksum] = [fname]

    return Duplicate


def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)
    

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))
    count = 0
    totaldelated = 0
    for value in Result:
        for subvalue in value:
            count = count+1
            if(count > 1):
                print("Duplicate Found : ",subvalue)
                totaldelated = totaldelated +1
        count = 0
    
    print("Total Delated Files : ",totaldelated)


def main():
   Data = DeleteDuplicate("Test")

   


if __name__ == "__main__":
    main()