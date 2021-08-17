class negativeNum(Exception):
    def __init__(self,string,delimiter):
        numbers = []
        for line in string.split("\n"):
            if delimiter in line and not line.startswith("//"):
                for num in line.split(delimiter):
                    num = int(num)
                    if num < 0:
                        numbers.append(num)
        super().__init__("Negatives not allowed :"+",".join(list(map(str,numbers))))


if __name__ == "__main__":
    try:
        raise negativeNum("1,-12,3\n3,-2,1",",")
    except negativeNum as e:
        print(e)