def str_and_pad(dollar_value):

    dollar_valueStr = "${:,.2f}".format(dollar_value)
    dollar_valuePad = "{:>10}".format(dollar_valueStr)


def val_int_number(number_value, min_value, max_value):

    is_valid = True
    try:
        number_value = int(number_value)
    except:
        print("Invalid input - must be a valid number.")
        is_valid = False
    else:
        if number_value < min_value or number_value > max_value:
            print("Invalid input - number must be between " + str(min_value) + " and " + str(max_value) + ".")
            is_valid = False

    return is_valid


def edit_default_values():
        while True:
            f = open("TCDef.dat", "r")
            CLAIM_NUM = int(f.readline())
            HST = float(f.readline())
            LOW_PER_DIEM_RATE = float(f.readline())
            HIGH_PER_DIEM_RATE = float(f.readline())
            MILEAGE_RATE = float(f.readline())
            RENTAL_CAR_RATE = float(f.readline())
            f.close()
            try:
                change_values = int(input("Do you want to change the default values (1) or return to main menu (2): "))
            except:
                print("Please enter 1 or 2 - try again.")
            else:
                while True:
                    if change_values == 1:
                        f = open("Password.dat", "r")
                        pass_conf = input("Enter password to make changes to the default values: ")
                        if pass_conf == f.readline():
                            f = open("TCDef.dat", "r")
                            print()
                            print("1. Claim Number" + " " + f.readline())
                            print("2. HST Rate" + " " + f.readline())
                            print("3. Low Per Diem Rate" + " " + f.readline())
                            print("4. High Per Diem Rate" + " " + f.readline())
                            print("5. Mileage Rate" + " " + f.readline())
                            print("6. Rental Car Rate" + " " + f.readline())
                            print("7. Exit")
                            print()
                            f.close()
                            while True:
                                item_change = int(input("Which default value would you like to change(1-7): "))
                                IsValid = val_int_number(item_change, 1, 7)
                                if IsValid:
                                    item_change = int(item_change)
                                    break
                            if item_change == 1:
                                while True:
                                    try:
                                        claim_num_change = int(input("What is the new starting Claim Number: "))
                                    except:
                                        print("Invalid entry - Please enter a valid number.")
                                    else:
                                        CLAIM_NUM = int(claim_num_change)
                                        break
                                f = open("TCDef.dat", "w")
                                f.write("{}\n".format(str(CLAIM_NUM)))
                                f.write("{}\n".format(str(HST)))
                                f.write("{}\n".format(str(LOW_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(HIGH_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(MILEAGE_RATE)))
                                f.write("{}\n".format(str(RENTAL_CAR_RATE)))
                                f.close()
                            elif item_change == 2:
                                while True:
                                    try:
                                        hst_change = float(input("What is the new HST amount(enter decimal version ie 0.15 for 15%): "))
                                    except:
                                        print("Invalid entry - Please enter a valid number.")
                                    else:
                                        HST = float(hst_change)
                                        break
                                f = open("TCDef.dat", "w")
                                f.write("{}\n".format(str(CLAIM_NUM)))
                                f.write("{}\n".format(str(HST)))
                                f.write("{}\n".format(str(LOW_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(HIGH_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(MILEAGE_RATE)))
                                f.write("{}\n".format(str(RENTAL_CAR_RATE)))
                                f.close()
                            elif item_change == 3:
                                while True:
                                    try:
                                        low_per_diem_change = float(input("What is the new Low Per Diem amount(enter dollar amount without the $): "))
                                    except:
                                        print("Invalid entry - Please enter a valid number.")
                                    else:
                                        LOW_PER_DIEM_RATE = float(low_per_diem_change)
                                        break
                                f = open("TCDef.dat", "w")
                                f.write("{}\n".format(str(CLAIM_NUM)))
                                f.write("{}\n".format(str(HST)))
                                f.write("{}\n".format(str(LOW_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(HIGH_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(MILEAGE_RATE)))
                                f.write("{}\n".format(str(RENTAL_CAR_RATE)))
                                f.close()
                            elif item_change == 4:
                                while True:
                                    try:
                                        high_per_diem_change = float(input("What is the new High Per Diem amount(enter dollar amount without the $): "))
                                    except:
                                        print("Invalid entry - Please enter a valid number.")
                                    else:
                                        HIGH_PER_DIEM_RATE = float(high_per_diem_change)
                                        break
                                f = open("TCDef.dat", "w")
                                f.write("{}\n".format(str(CLAIM_NUM)))
                                f.write("{}\n".format(str(HST)))
                                f.write("{}\n".format(str(LOW_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(HIGH_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(MILEAGE_RATE)))
                                f.write("{}\n".format(str(RENTAL_CAR_RATE)))
                                f.close()
                            elif item_change == 5:
                                while True:
                                    try:
                                        mileage_rate_change = float(input("What is the new Mileage Rate(enter dollar amount without the $): "))
                                    except:
                                        print("Invalid entry - Please enter a valid number.")
                                    else:
                                        MILEAGE_RATE = float(mileage_rate_change)
                                        break
                                f = open("TCDef.dat", "w")
                                f.write("{}\n".format(str(CLAIM_NUM)))
                                f.write("{}\n".format(str(HST)))
                                f.write("{}\n".format(str(LOW_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(HIGH_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(MILEAGE_RATE)))
                                f.write("{}\n".format(str(RENTAL_CAR_RATE)))
                                f.close()
                            elif item_change == 6:
                                while True:
                                    try:
                                        rental_car_rate_change = float(input("What is the new Rental Car Rate(enter dollar amount without the $): "))
                                    except:
                                        print("Invalid entry - Please enter a valid number.")
                                    else:
                                        RENTAL_CAR_RATE = float(rental_car_rate_change)
                                        break
                                f = open("TCDef.dat", "w")
                                f.write("{}\n".format(str(CLAIM_NUM)))
                                f.write("{}\n".format(str(HST)))
                                f.write("{}\n".format(str(LOW_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(HIGH_PER_DIEM_RATE)))
                                f.write("{}\n".format(str(MILEAGE_RATE)))
                                f.write("{}\n".format(str(RENTAL_CAR_RATE)))
                                f.close()
                            else:
                                break
                        elif pass_conf != f.readline():
                            break
                        f.close()
                    elif change_values != 1:
                        break
                    break
                break


def main():     # Runs the opening menu for the program, allows user to choose the option they want, and run until they choose quit.
    while True:
        print()
        print("NL Chocolate Company")
        print("Travel Claims Processing System")
        print()
        print("1. Enter an Employee Travel Claim.")
        print("2. Edit System Default Values.")
        print("3. Print the Travel Claim Report.")
        print("4. Graph Monthly Claim Totals.")
        print("5. Quit Program.")
        print()
        print()
        print()
        
        while True:
            # Allows user to input a number from 1-5, validate that the number is between 1-5, return if that value is true,
            # int that number, and then use that number to select a menu item to run
            Choice = input("Enter choice: (1-5): ")
            IsValid = val_int_number(Choice, 1, 5)
            if IsValid:
                Choice = int(Choice)
                break
        if Choice == 1:
            print()
            emp_travel_claim()
        elif Choice == 2:
            print()
            edit_default_values()
        elif Choice == 3:
            print()
            print_travel_claim()
        elif Choice == 4:
            print()
            graph_monthly_claims()
        else:
            exit(0)
            
def emp_travel_claim():
    import datetime
    while True:
        
        #inputs
        print("=" * 50)
        print("Welcome to the employee travel claims system!")
        print("Fill in the required information below")
        print("=" * 50)
        print()
        emp_num = input("Employee number: ")
        if emp_num.upper() == "END":
            exit(0)
        emp_name_f = input("Employee first name: ")
        emp_name_l = input("Employee last name: ")
        emp_name = emp_name_f + " " + emp_name_l
        trip_loc = input("Location of trip: ")
        date_startStr = input("Start date (YYYY-MM-DD): ")
        date_endStr = input("End date (YYYY-MM-DD): ")
        
         # Calculating number of days:
        date_start = datetime.datetime.strptime(date_startStr, "%Y-%m-%d")
        date_end = datetime.datetime.strptime(date_endStr, "%Y-%m-%d")
        days_num = (date_end - date_start).days
    
        # Asking user whether they used their own car or a rental and only allowing them to answer with O or o for own
        # and R or r for rental
        car_used = input("Enter O for own car or R for rental: ")
        if car_used.upper() != "O" and car_used.upper() != "R":
            print("You must enter O or R")
            car_used = input("Enter O for own car or R for rental: ")
            if car_used == "R":
                km_trav = int(input("Kilometers traveled: "))
            else:
                break
        
        # Processes:

        # Calculating per diem amount:
        per_diem = 0
        if days_num <= 3:
            f = open("TCDef.dat", "r")
            f.readline()
            f.readline()
            LOW_PER_DIEM_RATE = float(f.readline())
            per_diem = LOW_PER_DIEM_RATE * days_num
            
        elif days_num > 3:
            f = open("TCDef.dat", "r")
            f.readline()
            f.readline()
            f.readline()
            HIGH_PER_DIEM_RATE = float(f.readline())
            per_diem = HIGH_PER_DIEM_RATE * days_num
    
        # Calculating mileage amount:
        mile_amt = 0
        if (car_used == "O") or (car_used == "o"):
            f = open("TCDef.dat", "r")
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            Mileage = float(f.readline())
            mile_amt = Mileage * km_trav
        elif (car_used == "R") or (car_used == "r"):
            f = open("TCDef.dat", "r")
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            Rental_rate = float(f.readline())
            mile_amt = Rental_rate * days_num
        
        
        # Calculating claim amount:
        claim_amt = per_diem + mile_amt
    
        # Calculating HST:
        f = open("TCDef.dat", "r")
        f.readline()
        HST = float(f.readline())
        hst = HST * per_diem
        f.close()
    
        # Calculating claim total:
        claim_tot = claim_amt + hst
        
        # Appending claim values to "Claims.dat" on a single line:
        
        f = open('Claims.dat', 'a')
        
        
        return [emp_num, emp_name, trip_loc, date_startStr, date_endStr, car_used, days_num, mile_amt, claim_amt, hst, claim_tot]
        
        ClaimCtr = 0
        ClaimAmtAcc = 0
        HSTAcc = 0
        ClaimTotalAcc = 0
        BonusAcc = 0
        TotalAfterBonusAcc = 0
        
        ClaimsList = emp

f = open('Claims.dat', 'r')
for claims in f:
    ClaimList = claims.split(",")
    ClaimNum = ClaimList[0]
    EmpName = ClaimList[1].strip()
    ClaimAmt = float(ClaimList[2].strip())
    HST = float(ClaimList[3].strip())
    ClaimTotal = float(ClaimList[4].strip())
    Bonus = ClaimTotal * .10
    TotalAfterBonus = ClaimTotal + Bonus