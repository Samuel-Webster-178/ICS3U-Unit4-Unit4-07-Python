#!/usr/bin/env python3

# Created by Samuel Webster
# Created on April 2022
# Output number block within range
#   1000-2000 range at initial commit


import constants


def main():
    # I calculate circumference

    # output
    i = constants.MIN
    while i <= constants.MAX:
        # if statement determines when endline is needed
        if i % constants.NUMBERS_PER_LINE == 0:
            print("\n", end="")
        else:
            print(" ", end="")
        # Outputing numbers in series
        print(i, end="")
        # Increment counter for loop
        i += 1
    print("\n\nDone.")


if __name__ == "__main__":
    main()
