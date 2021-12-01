from input import input

def getSliders(numbers):
    total = []
    for i in range(len(numbers)):
        try:
            total.append(sum(numbers[i:i+3]))
        except:
            break
    return total

def checkIncreased(numbers):
    increased = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            increased += 1
    return increased

def main():
    print("Part 1: " + str(checkIncreased(input.numbers)))
    print("Part 2: " + str(checkIncreased(getSliders(input.numbers))))

if __name__ == "__main__":
    main()
