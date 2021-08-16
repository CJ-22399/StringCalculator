class StringCalcultor:
    def Add(self,numbers):
        if len(numbers) > 0:
            if "," in numbers:
                try:
                    return sum(list(map(int,numbers.split(","))))
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
    string_calculator = StringCalcultor()
    print(string_calculator.Add(input_string))  