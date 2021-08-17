from Exceptions import negativeNum
class StringCalcultor:
    def __init__(self):
        self.count = 0
    def check_delimiter(self,string):
        lines = string.split("\n")        
        if len(lines) > 1:
            return lines[0][2:] if lines[0].startswith("//") else None
        return None
    def GetCalledCount(self):
        return self.count
    def Add(self,numbers):
        self.count += 1
        if len(numbers) > 0:
            delimiter = self.check_delimiter(numbers) if self.check_delimiter(numbers) is not None else ","
            if delimiter in numbers:
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