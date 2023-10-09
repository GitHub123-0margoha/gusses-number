import random
i=0
x =  random.randint(1,20)
print ("*****OMAR GOHA WELCOMES YOU *****")
print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
while True :
    print ("guess the number ")
    print ("you are allowed three attempts") 
    p= int (input("entar your number from 1 to 20 : ")) 
    i+=1
   
    if p == x :
                 print ( str(p) + " is the correct guess " )
                 break
               
    if p > x :
                  print ( str(p) + " The number you gussed is large ")
                  print ("//------------------------------------//")
    if p < x :
                  print ( str(p) + " The number you gussed is small ")
                  print ("//------------------------------------//")
    
    if i == 3:
                print ("you have used all your attemots . the correct number was = " + str (x))
    if i == 4:
                break
   
            
            
    
            
              
   
        
            
    

   




        
       
        