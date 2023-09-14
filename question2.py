# jode mustafa
# u41333726
# this program asks for a symbol for the basic of opperations and does the certain  math operation based on the two values


add= lambda x, y: x + y
subtract = lambda x,y: x-y
multiply = lambda x,y: x*y
floating_division = lambda x,y: (x/y)
integer_division = lambda x,y: (x//y)
module_operator = lambda x,y: x%y
exponent_operation = lambda x,y: x**y 


ans=(input("enter the operation as a symbol: "))
values= (input("Enter two values, separated by a space: "))
x=int(values.split()[0])
y=int(values.split()[1])



def basic_math(x,y):
    if ans=="+":
        answer=add(x,y)
        print(f" {x}+{y}= {answer}")

    elif ans =="-":
        answer= subtract(x,y)
        print(f" {x}-{y}= {answer}")

    elif ans=="%":
        answer=module_operator(x,y)
        print(f" {x}%{y}= {answer}")
    elif ans=="*":
        answer=exponent_operation(x,y)
        print(f" {x}*{y}= {answer}")

    elif ans== "/":
        answer= floating_division(x,y)
        print(f" {x}/{y}= {answer}")
    elif ans == "//":
        answer= integer_division(x,y)
        print(f"{x}//{y}= {answer}")
    else:
        print(f" {x}{ans}{y}= invalid operation")
    
basic_math(x, y)