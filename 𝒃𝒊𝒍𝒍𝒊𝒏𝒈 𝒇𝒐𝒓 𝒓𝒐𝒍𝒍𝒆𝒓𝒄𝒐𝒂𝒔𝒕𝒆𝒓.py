print('WELCOME TO ROLLER COSTER RIDE\n')
height=input('what is your height in centi-meters?\n')
if int(height)>=120:
  print('you can have the ride') 
  age=input (f'what is your current "age"?\n') 
  if int(age)<12:
    bill1=+5
    print('child ticket cost is $5')
  elif int(age)<=18 :
    bill1=+7
    print('your ticket cost is $7')
  elif int(age)<45:
    bill1=+12
    print('your ticket cost is $12')
  elif int(age)<=55:
    bill1=+0
    print('you can have the ride for free')
  else:
    bill1=+0
    print('you cannot have the ride!')
  if int(age)<45:
    photos=input(('do you like to have photos say in yes or no ?\n'))
    if photos=="yes":
       bill2=+3
       print('cost for photos is $3')
    else:
       bill2=+0
       print('okay sir/mam')
  elif int(age)<=55:
      photos=input(('do you like to have photos say in yes or no ?\n'))
      if photos=="yes":
           bill2=+0
           print('cost for photos is $0')
      else:
           bill2=+0
           print('okay sir/mam')
  if int(age)<=55:
   total_bill=bill1+bill2
   print(f'The total cost of ride is ${total_bill}')
   print('ENJOY YOUR RIDE ')
  else:
     print(' THANKS FOR VISITING')
else:
  print('you cannot have the ride sir/mam!\n THANKS FOR VISITING')

  