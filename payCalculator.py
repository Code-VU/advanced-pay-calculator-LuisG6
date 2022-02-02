def calculatePay():
    
    # This first line is provided for you
   hrs = float(input("Enter Hours: "))
   rate = float(input("Enter Rate: "))
   overtime = rate * 1.5
   total = hrs * overtime
   
   print(f"Pay: {total}")
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()