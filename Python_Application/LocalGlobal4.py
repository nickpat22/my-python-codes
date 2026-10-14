no = 11         

def Display():
    global no
    no = no + 1
    print("From Display",no)
    

print("Before : ",no)
Display()
print("After : ",no)