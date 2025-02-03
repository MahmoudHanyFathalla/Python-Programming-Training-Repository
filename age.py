a = 0
while a != 3:
 year = int(input("What year were you born?[1900,1901,....]:"))
 month = int(input("what month were you born?[1,2,3,4,5,6,...12]:"))
 day = int(input("what day were you born?[1,2,3,4,5,...31]:"))
 print(f"you were born in {day}/{month}/{year}")
 current_year = int(input("what is the current year?:"))
 current_month =int(input("what is the current month?:"))
 current_day = int(input("what is the current day?:"))
 actually_year = current_year-year
 actually_month = current_month-month
 actually_day = current_day-day
 if current_month < month:
     actually_month = 12 + actually_month 
     actually_year = actually_year - 1
 if current_day < day : 
     actually_day = 30 + actually_day
     actually_month = actually_month - 1
 print(f"you are {actually_year} years and {actually_month} month and {actually_day} days")
 option = str(input("Do you want to know more specific informations about your age ?[yes \ no]:"))
 if option == "yes":
      dayes = (actually_year * 365) + (actually_month * 30) + actually_day
      hours = dayes * 24
      minutes = hours * 60
      seconds = minutes * 60
      print(f"you lived {dayes} day...\nyou lived {hours} hour...\nyou lived {minutes} minute...\nyou lived {seconds} second!")
 elif option == "no":
      print("okay'_'")
 else:
      print("Error")
 g = str(input("press [c] to play again or write [done] to exit :"))
 if g == "c":
      a = 0
 else:
      a = 3
 