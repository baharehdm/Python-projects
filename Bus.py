# Let's assume that at some less inhabited area (Teisko?), buses leave for Tampere according to the following schedule:

# 6.30
# 10.15
# 14.15
# 16.20
# 17.20
# 20.00
# Design and implement a program that asks the user what time it is and prints the times for the next three buses, based of the entered time.

# To be able to concentrate on the essential matter (presenting the schedule as a list), simplify the presentation of the time 
# by saving the time as one integer where the minutes and the hours are expressed in the same number, ie. 6.30 as 630 and 10.15 as 1015. 
# Times presented this way can easily be compared with each other (ie. does a certain time come before another time) using the normal comparison operators. Examples of how the program functions:

# Enter the time (as an integer): 1000
# The next buses leave:
# 1015
# 1415
# 1620
# Enter the time (as an integer): 1800
# The next buses leave:
# 2000
# 630
# 1015





def main():
    bus()

def bus():
    time=[630,1015,1415,1620,1720,2000]
    enteredtime=int(input("Enter the time (as an integer): "))
    counter=3
    print("The next buses leave:")
    for i in range(0,len(time)):
        if time[i]>= enteredtime:
            print(time[i])
            counter-=1
            if counter==0:
                break

    if counter==3:
        print(time[0])
        print(time[1])
        print(time[2])
    elif counter==2:
        print(time[0])
        print(time[1])
    elif counter==1:
        print(time[0])


main()
