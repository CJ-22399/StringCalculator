class StringCalcultor:
    def check_delimiter(self,string):
        lines = string.split("\n")        
        if len(lines) > 1:
            return lines[0][2:] if lines[0].startswith("//") else None
        return None
    def Add(self,numbers):
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
                                total += sum(list(map(int,line.split(delimiter))))
                            else:
                                raise ValueError
                            
                        return total
                    else:
                        return sum(list(map(int,numbers.split(delimiter))))
                except ValueError:
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