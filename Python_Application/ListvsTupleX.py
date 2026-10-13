#---------------------------------------------
#                   List            Tuple
#--------------------------------------------

##ordered           Yes             Yes
#Indexed            Yes             yes
#Mutable            yes             no
#Hetrogenious       Yes             yes

def main():
   Data1 = [10,3.14,True,"Pune"]        #List
   Data2 = (10,3.14,True,"Pune")        #Tuple

   print(Data1)
   print(Data2)

   print(Data1[0])
   print(Data2[0])

if __name__ == "__main__":
    main()