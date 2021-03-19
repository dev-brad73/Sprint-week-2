###  Newfoundland Chocolate Company  ###
 ##       Travel Claims System       ##
### Author: Brad Rice & Chris Osmond ###
 ## Date: Wednesday March 17th 2021  ##

import backpack as bp

# Constants: Found in the TCDef.dat file in order they are seen and read into their corresponding constants placeholder.
f = open("TCDef.dat", "r")
CLAIM_NUM = int(f.readline())
HST = float(f.readline())
LOW_PER_DIEM_RATE = float(f.readline())
HIGH_PER_DIEM_RATE = float(f.readline())
MILEAGE_RATE = float(f.readline())
RENTAL_CAR_RATE = float(f.readline())
f.close()

# Inputs: Runs all the inputs from a function in the backpack
if __name__ == "__main__":
    bp.main()