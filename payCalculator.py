def calculatePay():
    
    # This first line is provided for you
    try: 
        hrs = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: ")) 
    
        total = hrs * rate
        overTimeRate = rate * 1.5
        overTimeHours = (hrs - 40) + overTimeRate
        totalOverTime = total + overTimeHours
    
        if hrs > 40:
            print(f"Pay: {totalOverTime}")
        else:
            print(f"Pay: {total}")

    except:
        print("Please input a number")
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()