import unittest
import ThinkBridge_task

#The TestCases Dictionary, contains input and expected output
Cases={"123456.78":"one lakh twenty three thousand four hundred fifty six Rs seventy eight paise","-98":"Number not in range 0-1000000, Try in valid range","9653.ww":"Number Contains Character, Hence cannot be converted",".67":"sixty seven paise",".6":"sixty  paise","123":"one hundred twenty three Rs","sasfg":"Number Contains Character, Hence cannot be converted","09876.5":"nine thousand eight hundred seventy six Rs fifty  paise"}


class TestDigit2Number(unittest.TestCase):
    
    def test_CheckNumber(self):
        i=1
        for Keys in Cases.keys():
            print("Case: "+str(i))
            print("Input value: "+Keys)
            print("ExpectedResult: "+Cases[Keys])
            #Compare the Values of Output with Expected Result
            self.assertEqual(ThinkBridge_task.Number_2_word(Keys),Cases[Keys])
            i=i+1
            
if __name__=="__main__":
    unittest.main()