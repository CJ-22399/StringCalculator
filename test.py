from main import StringCalcultor


if __name__ == "__main__":
    string1 = ""
    string2 = "1"
    string3 = "1,2"
    string4 = "1_2"
    string5 = "_"
    string6 = "1_2_3"
    string7 = "1b$2"
    string_calculator = StringCalcultor()
    assert string_calculator.Add(string1) is not None , "empty String"
    assert string_calculator.Add(string2) is not None , f"str = {string2}"
    assert string_calculator.Add(string3) is not None , f"str = {string3}"
    assert string_calculator.Add(string4) is  None , f"str = {string4}"
    assert string_calculator.Add(string5) is  None , f"str = {string5}"
    assert string_calculator.Add(string6) is  None , f"str = {string6}"
    assert string_calculator.Add(string7) is  None , f"str = {string7}"
    print("All Test Passed.")
    