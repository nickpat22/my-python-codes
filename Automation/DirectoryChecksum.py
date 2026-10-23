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

    for FolderName, SubFolder, Filename in os.walk(DirectoryName):
        for fname in Filename:
            fname = os.path.join(FolderName, fname)

            Checksum = CalculateChecksum(fname)

            print(f"{fname} : {Checksum}")


def main():
   FindDuplicate("Test")

if __name__ == "__main__":
    main()