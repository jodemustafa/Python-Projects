# u41333726
# jode mustafa


# this prgram takes an input base and input exponent and then puts the base to the power of the exponent
def __main__():
    global base
    base = int(input("enter the base "))
    global  exponent
    exponent = int(input("enter a whole number between 2and 50 "))
    if exponent<2 or exponent>50:
        exponent=int(input("invalid please enter a whole number between 2 and 50: "))


def raisePower(base, exponent):
    if (exponent == 1):
        print (base)
    if (exponent != 1):
        print (base * raisePower(base, exponent - 1))


__main__()
raisePower(base, exponent)