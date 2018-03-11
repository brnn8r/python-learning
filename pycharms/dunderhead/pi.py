import sys
import math
import ptvsd

def pii_fraction(divisor):
    print("pii divided by {} is {}".format(divisor, math.pi/divisor))
    return math.pi/divisor

if __name__ == "__main__":

    if len(sys.argv) == 1:
        sys.exit(0)
    
    nums=sys.argv[1:]

    if sys.argv[1] == "-d":
        print("DEBUG_MODE")
        nums = sys.argv[2:]
        ptvsd.enable_attach("dunderhead", address=('0.0.0.0', 5400))
        #ptvsd.wait_for_attach()

    for num in nums:
        try:
            parsed_num = float(num)
            val = pii_fraction(parsed_num)
        except ValueError:
            print("{} is not a number".format(num))
