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


def main():
   Ret =  CalculateChecksum("DemoX.txt")
   print("Checksum Of File is ",Ret)

if __name__ == "__main__":
    main()