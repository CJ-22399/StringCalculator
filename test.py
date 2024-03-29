from main import StringCalcultor
if __name__ == "__main__":
    """
        test Cases Variable contain array of 2 element 
        first Element represent test string
        Second Element Represent result of test ( None or not None) 
        0 : represent None Result of test
        1 : Represent not None Result of test
        """
    test_cases = [
        ["",1],
        ["1",1],
        ["1,2",1],
        ["1_2",0],
        ["_",0],
        ["1_2_3",0],
        ["1b$2",0],
        ["1\n2,3",1],
        ["1,2,3\n1,5,4",1],
        ["1,2,3\n1_5_4",0],
        ["//:\n11:12:13",1],
        ["//*\n11*12*13\n1*2*3",1],
        ["//:\n11,12,13",0],
        ["//:\n11_12_13",0],
        ["1,2,3\n1,-5,4",0],
        ["1,-2,3\n1,-5,-4",0],
        ["1,-2,3\n1,-54_-44",0],
        ["1,-2,3,1,-54,-44",0],
        ["//*\n11*-12*13\n1*-2*3",0],
        ["1000,200,10,2000",1],
        ["1000,2000,1000,2000",1],
        ["//*\n100*1200*100\n100*200*300",1],
        ["//[****]\n1****2****3\n4****5****6",1],
        ["//[!!]\n1!!2!!3\n4!!5!!6",1],
        ["//!!\n1!!2!!3\n4!!5!!6",0],
        ["//[*][!][@]\n1*2@3\n4@5!6",1],
        ["//[***][!!!][@@]\n1***2@@3\n4@@5!!!6\n1***2",1],
        ["//[@@@][!][**]\n1@@@-30!-3**7**8**-9",0]
        
    ]
    string_calculator = StringCalcultor()
    for counter,test in enumerate(test_cases):
        if test[1] == 0:
            assert string_calculator.Add(test[0]) is None , f"Failed Test Case=> {test[0]}"
        elif test[1] == 1:
            assert string_calculator.Add(test[0]) is not None , f"Failed Test Case=> {test[0]}"
    assert len(test_cases) == string_calculator.GetCalledCount() , "Get Called Count Failed"
    print(f"Number of time Add Invoke :{string_calculator.GetCalledCount()}")
    print("All Test Passed.")