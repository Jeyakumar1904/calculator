while True:
  choice = input("Please enter choice (a/ b/ c/ d): ")    
      
  num_1 = int (input ("Please enter the first number: "))    
  num_2 = int (input ("Please enter the second number: "))    
      
  if choice == 'a':    
    print (num_1, " + ", num_2)    
      
  elif choice == 'b':    
    print (num_1, " - ", num_2,num_1-num_2)    
      
  elif choice == 'c':    
    print (num1, " * ", num2)    
  elif choice == 'd':    
    print (num_1, " / ", num_2)    
  else:    
    print ("This is an invalid input")