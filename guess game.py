n=18
for i in range(1,5):
  a=int(input("Enter the no \n"))
  if a<n :
    print("Number is greater than",a)
  elif a>n :
    print("Number is smaller than",a)
  else:
    print("You guess the correct number")
    break
  print(4-i,"chances left")












