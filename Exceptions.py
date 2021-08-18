from utils import is_digit
class negativeNum(Exception):
    def __init__(self,string,delimiter):
        numbers = []
        if type(delimiter) is not list:
            for line in string.split("\n"):
                if delimiter in line and not line.startswith("//"):
                    for num in line.split(delimiter):
                        num = int(num)
                        if num < 0:
                            numbers.append(num)
        else:
            stack = string.split("\n")[1:] if "\n" in string else []
            while len(stack) > 0:
                string = stack.pop()
                if not is_digit(string):
                    for D in delimiter:
                        if D in string:
                            stack.extend(string.split(D))
                            break
                else:
                    if int(string) < 0:
                        numbers.append(int(string))
        super().__init__("Negatives not allowed :"+",".join(list(map(str,numbers))))
