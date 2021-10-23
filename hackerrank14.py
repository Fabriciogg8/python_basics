def run():
    total_students= int(input(""))
    if 0 < total_students < 1000:
        set1= set()
        num = input("")
        for i in num.split(" "):
            i = int(i) 
            set1.add(i)
        set2= set()
        b= input("")
        if 0 < b < 1000:
            for i in b.split(" "):
                i = int(i) 
                set2.add(i)
        final_set = set1 | set2
    print(len(final_set))           
    
        
if __name__ == "__main__":
    run()