from collections import Counter

def p1(input):
    theta=""
    epsilon=""
    for i in range(12):
        temp=Counter()
        for line in input:
            temp[line[i]]+=1
        if temp["1"]>temp["0"]:
            theta+="1"
            epsilon+="0"
        else:
            theta+="0"
            epsilon+="1"
    return(int(theta, 2)*int(epsilon, 2))

def p2(input):
    def half(input):
        for i in range(12):
            temp=Counter()
            for line in input:
                temp[line[i]]+=1
            if temp["1"]>=temp["0"]:
                input=[j for j in input if j[i]=="1"]
            else:
                input=[j for j in input if j[i]=="0"]
            if len(input)==1:
                return input[0]
        return input[0]
    def half2(input):
        for i in range(12):
            temp=Counter()
            for line in input:
                temp[line[i]]+=1
            if temp["0"]<=temp["1"]:
                input=[j for j in input if j[i]=="0"]
            else:
                input=[j for j in input if j[i]=="1"] 
            if len(input)==1:
                return input[0]
        return input[0]
    return int(half(input), 2)*int(half2(input), 2)

def main():
    with open("input.txt") as f:
        input=f.read().split("\n")
    print(p1(input))
    print(p2(input))

if __name__ == "__main__":
    main()
