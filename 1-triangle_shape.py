try: 
   n = int(input("Enter row: "))

   if n%2!=0:
      for i in range(n):
          for j in range(i):
              print(" ", end="")
          for j in range(n-i):
              print("*", end=" ")
          print()
   else:
       print("Should be an odd number")
except:
    print("Enter number only")
