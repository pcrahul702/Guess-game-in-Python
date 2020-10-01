n=18
guess_the_number =1
while(guess_the_number<5):
 a = int(input("Enter the guess number\n"))
 if(a<n):
    a=int(input("enter number greter than last enterd\n"))
 elif(a>n):
     a = int(input("enter number less than last enterd\n"))
 else:
     print("you guesse right")
     print(guess_the_number,"no guess you take to find")
     break
 print(5-guess_the_number,"guess is left")












