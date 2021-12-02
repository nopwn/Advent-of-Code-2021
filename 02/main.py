from input import input

def calc(newInput, p2):
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(newInput)):
        if newInput[i][0] == "forward":
            horizontal += int(newInput[i][1])
            if (p2==1):
                depth += (aim*int(newInput[i][1]))
        elif newInput[i][0] == "down":
            if (p2 == 1):
                aim += int(newInput[i][1])
            else:
                depth += int(newInput[i][1])
        elif newInput[i][0] == "up":
            if (p2 == 1):
                aim -= int(newInput[i][1])
            else:
                depth-= int(newInput[i][1])
    return(horizontal*depth)

def main():
    newInput = []
    for i in input.input:
        newInput.append(i.split(" "))
    print("Part 1: " + str(calc(newInput, 0)))
    print("Part 2: " + str(calc(newInput, 1)))


if __name__ == "__main__":
    main()
