from input import input

def main():
    horizontal = 0
    depth = 0
    aim = 0
    newInput = []
    for i in input.input:
        newInput.append(i.split(" "))
    for i in range(len(newInput)):
        if newInput[i][0] == "forward":
            horizontal += int(newInput[i][1])
            depth += (aim*int(newInput[i][1]))
        elif newInput[i][0] == "down":
            aim += int(newInput[i][1])
        elif newInput[i][0] == "up":
            aim -= int(newInput[i][1])
    print(horizontal*depth)

if __name__ == "__main__":
    main()
