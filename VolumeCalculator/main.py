# Dongzheng (Elizabeth) Xu
# This program handles prompting and input and output for different shapes.
# Last edited: October 23 2018
from VolumeCalculator import volumes  # imports volume calculations

quitCalculating = False  # sentinel value to quit/end session

# lists volumes calculated of different shapes
cubes = []
pyramids = []
ellipsoids = []


# function that prints out shape categories in a certain format
def print_lists(chosen_shape, shape_list):
    print("{}: ".format(chosen_shape), end="")  # print shape category
    if len(shape_list) < 1:  # no shapes entered
        print("No shapes entered.")
    else:  # shapes entered
        shape_list.sort() # sort calculated volumes from lowest to highest
        for x in range(len(shape_list)):
            print("{:0.1f}".format(shape_list[x]), end="")  # print each value in that category
            if x < (len(shape_list) - 1):  # print comma after each element except last element
                print(", ", end="")
            else:
                print("")  # starts new line for next shape


# prompts for shape and calculates volume
while not quitCalculating:
    print(
        "____________________________________________________")  # Line to separate each shape calculation for easy reading
    shape = input("Enter shape: ").lower()  # prompt user to enter shape

    # calculate the volume of selected shape using functions from volumes.py
    if shape == "cube" or shape == "c":
        shape = "cube"
        sideLength = int(input("Please input length of cube:"))
        calculatedVolume = volumes.cube(sideLength)  # calculate volume
        print("The volume of a cube with sides {:0.1f} is: {:0.1f}. ".format(sideLength, calculatedVolume))
        cubes.append(calculatedVolume)  # record calculated volume to cube list
    elif shape == "p" or shape == "pyramid":
        shape = "pyramid"
        base = int(input("Please input base of pyramid: "))
        height = int(input("Please input height of pyramid: "))
        calculatedVolume = volumes.pyramid(base, height)  # calculate volume
        print("The volume of a pyramid with base {:0.1f} and height {:0.1f} is: {:0.1f}. ".format(base, height,calculatedVolume))
        pyramids.append(calculatedVolume)  # record calculated volume to pyramid list
    elif shape == "e" or shape == "ellipsoid":
        shape = "ellipsoid"
        r1 = int(input("Please input 1st radius:"))
        r2 = int(input("Please input 2st radius:"))
        r3 = int(input("Please input 3st radius:"))
        calculatedVolume = volumes.ellipsoid(r1, r2, r3)  # calculate volume
        print("The volume of an ellipsoid with radii {:0.1f},{:0.1f} and {:0.1f} is: {:.1f}. ".format(r1, r2, r3,calculatedVolume))
        ellipsoids.append(calculatedVolume)  # record calculated volume to ellipsoid list

    # if user quits, print out all the calculated volumes for each shape category in sorted order
    elif shape == "q" or shape == "quit":
        print("You have reached the end of your session.")
        if (len(cubes) == 0 and len(ellipsoids) == 0 and len(pyramids) == 0):  # message if user didn't calculate any volumes
            print("You did not perform any volume calculations.")
        else:
            print("The volumes calculated for each shape are:")

            #  prints each shape list
            print_lists("Cube", cubes)
            print_lists("Pyramid", pyramids)
            print_lists("Ellipsoid", ellipsoids)

        quitCalculating = True  # exits while loop

    else:
        print("ERROR: Invalid shape input.")  # Error message if invalid shape input
