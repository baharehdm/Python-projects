# Fill in all TODOs in this file
# Introduction to programming
# car
# Bahareh the Material Coder, 256276

from math import sqrt

# Task: 
# create a simple driving simulation where the user drives a car through a 
# two-dimensional desert surface, using a textual interface. The program 
# calculates where the car moves and how much gas it uses.The program 
# prints a menu, which the user can use to select the executed operation. 
# Such operations include the filling of the car’s gas tank, driving the 
# car, and quitting the program.
# If the user selects driving a car as the operation, the car drives to 
# the target entered by the user (coordinates x and y) via straightest 
# possible route (direct line). If the user tries to drive a longer 
# distance than the gas allows, the car will only for as long as it can.
# If the user selects the filling of the tank as an operation, the car’s 
# information must also be taken into account. The user should not be able 
# to fill in more gas than the tank can hold. The program will continue to 
# operate normally, however - extra printouts are not needed in this case, either.


def menu():
    tank_size  = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " + \
                                 "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    MENU_TEXT =  "1) Fill 2) Drive 3) Quit \n-> "

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input(MENU_TEXT)

        if choice == "1":
           to_fill = read_number("How many liters of gas to fill up? ")
           gas = fill(tank_size,to_fill,gas)

        elif choice == "2":
           new_x = read_number("x: ")
           new_y = read_number("y: ")
           gas,x,y = drive(x,y,new_x,new_y,gas,gas_consumption)

        elif choice == "3":
           break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently
#
# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
#
# The function does not print anything and does not ask for any
# input.
def fill(tanksize,requestfill,currentgas):
    tank_gas_after = requestfill + currentgas
    if tanksize >= tank_gas_after:
        return tank_gas_after
    else:
        return tanksize
    # if requestfill<=tanksize-currentgas:
    #     tankafter=currentgas+requestfill
    # else:
    #     tankafter=currentgas
    # return float(tankafter)

# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car
#
# The parameters have to be in this order.
# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
#
# The return values have to be in this order.
# The function does not print anything and does not ask for any
# input.
def drive(currentx,currenty,destinationx,destinationy,currentgas,consumption):
    # It might be usefull to make one or two helper functions to help
    # the implementation of this function (drive)
    m = amount_ofkilometer(currentx, destinationx, currenty, destinationy)
    gasafter = float(currentgas - gasconsumption(m, consumption))
    if gasafter>0.0:
        return float(gasafter),float(destinationx),float(destinationy)
    else:
        km = currentgas * 100 / consumption
        newx = (destinationx-currentx) * km / m + currentx
        newy = (destinationy-currenty) * km / m + currenty
        gasafter = 0.0
        return float(gasafter),float(newx),float(newy)



def amount_ofkilometer(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    power = x * x + y * y
    m = sqrt(power)
    return float(m)

def gasconsumption(consumption, m):
    consump = (m * consumption / 100)
    return float(consump)
    # Implement your own functions here. It is required to implement at least
    # two functions that take at least one parameter and return at least one
    # value.
    # The functions have to be used somewhere in the program.


def read_number(prompt, error_message="Incorrect input!"):

    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError as e:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()

main()
