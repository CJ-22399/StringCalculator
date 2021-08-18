import regex as re
from utils import is_digit
from Exceptions import negativeNum
class StringCalcultor:
    def __init__(self):
        self.count = 0
    def Get_delimiter(self,string):
        lines = string.split("\n")        
        if len(lines) > 1:
            if len(lines[0]) == 3:
                return lines[0][-1] if lines[0].startswith("//") else None
            elif lines[0].startswith("//"):
                delimiters =  re.findall(r'\[.+?\]', lines[0])
                if len(delimiters) == 1 :
                    return delimiters[0][1:len(delimiters[0])-1]
                elif len(delimiters) > 1:
                    for i in range(len(delimiters)):
                        delimiters[i] = delimiters[i][1:len(delimiters[i])-1]
                    return delimiters
        return None
    def GetCalledCount(self):
        return self.count
    def Add(self,numbers):
        self.count += 1
        if len(numbers) > 0:
            delimiter = self.Get_delimiter(numbers) 
            if delimiter  is None:
                delimiter = ","
            if type(delimiter) == str and delimiter in numbers :
                try:
                    if "\n" in numbers:
                        total = 0
                        for line in numbers.split("\n"):
                            if line.startswith("//"):
                                continue
                            elif delimiter == "_"  or "_" not in line:
                                for number in line.split(delimiter):
                                    number = int(number)
                                    if number < 0:
                                        raise negativeNum(numbers,delimiter)
                                    else:
                                        total+=number if number <= 1000 else 0
                            else:
                                raise ValueError
                        return total
                    else:
                        total = 0
                        for number in numbers.split(delimiter):
                            number = int(number)
                            if number < 0:
                                raise negativeNum(numbers,delimiter)
                            else:
                                total += number if number <= 1000 else 0
                        return total
                except ValueError as e:
                    return None
                except  negativeNum as e:
                    print(e)
                    return None
            elif type(delimiter) == list:
                stack = numbers.split("\n")[1:] if "\n" in numbers else []
                total = 0
                while len(stack) > 0:
                    string = stack.pop()
                    if not is_digit(string):
                        for D in delimiter:
                            if D in string:
                                stack.extend(string.split(D))
                                break                        
                    else:
                        try:
                            if int(string) > 0:
                                total+= int(string) if int(string) <= 1000 else 0
                            else:
                                raise negativeNum(numbers,delimiter)
                        except negativeNum as e:
                            print(e)
                            return None
                return total
                        
            else:
                if len(numbers) == 1:
                    try:
                        return int(numbers[0])
                    except ValueError:
                        return None
                else:
                    return None
        else:
            return 0    


if __name__ == "__main__":
    input_string = input("Enter String With Comma Seperated Numbers=>")
    input_string = input_string.replace("\\n","\n")
    string_calculator = StringCalcultor()
    print(string_calculator.Add(input_string))  