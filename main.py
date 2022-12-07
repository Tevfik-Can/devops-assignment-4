print("--------Calculator----------\n")
ext = False
lastnum=0
while (ext== False):
    print("Enter Calculation with spaces: (eg. 3 + 3 | L / 40)")
    print("Operators : + | - | * | / | E = exit | L = Last Number")
    calculate = input()
    if "E" in calculate or "e" in calculate:
        print("Exiting the calculator")
        ext = True
        break
    nums = calculate.split(" ")
    final = 0.0
    if nums[0] == "L" or nums[0] == "l":
        nums[0] = lastnum
    elif nums[2] == "L" or nums[2] == "l":
        nums[2] = lastnum

    if nums[1] == "+":
        final= int(nums[0]) + int(nums[2])
    elif nums[1] == "-":
        final = int(nums[0]) - int(nums[2])
    elif nums[1] == "*":
        final = int(nums[0]) * int(nums[2])
    elif nums[1] == "/":
        if nums[2] == "0" and nums[0] != "0":
            print("NULL")
        else:
            final = int(nums[0]) / int(nums[2])
    lastnum=final
    print("= " + str(final))