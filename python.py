def fw():
    file_name=input("enter a file: ")
    file_name2="text2.txt" 
    file_name3="text3.txt"
    data=open(file_name,'r')
    data2=open(file_name2, 'r')
    data3=open(file_name3, 'r')
    if (data==data2): 
        print(data3)
    elif(data==data3):  
        print(data2)     
    
fw()
    
