Words=[["","one","two","three","four","five","six","seven","eight","nine"],["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"],["ten","eleven","tweleve","thirteen","forteen","fifteen","sixteen","seventeen","eighteen","nineteen"]]

def valid_number(Input_Number):
    try:
        Value=float(Input_Number)
    except:
        return False,"Number Contains Character, Hence cannot be converted"
    if Value>0 and Value<1000000:
        if "." in Input_Number:
            Input_Number=Input_Number.split(".")
            if len(Input_Number[1])>2:
                return False,"Decimal Value cannot exceed 2 Decimal Places"
            else:
                return True,""
        else:
            return True,""
    else:
        return False,"Number not in range 0-1000000, Try in valid range"


def two_digit_conversion(Number):
    if Number>9 and Number<20:
        Value=Words[2][Number%10]
    if Number>19:
        Value=Words[1][(Number//10)-2]+" "+Words[0][Number%10]
    if Number<10:
        Value=Words[0][Number]
    return Value


def Convert(Number):
    Value=""
    if Number//100000 !=0:
        Value= Value+Words[0][(Number//100000)]+" lakh "
        Number=Number%100000
    if Number//1000!=0:
        Value=Value+ two_digit_conversion(Number//1000) + " thousand "
        Number=Number%1000
    if Number//100!=0:
        Value=Value+Words[0][(Number//100)]+" hundred "
        Number=Number%100
    if Number!=0:
        Value= Value+ two_digit_conversion(Number)
    return Value
    
    


def Number_2_word(Input_Number):
    proceed,Output=valid_number(Input_Number)
    if proceed:
        if "." in Input_Number:
            Input_Number=Input_Number.split(".")
            if Input_Number[0]!="":
                if Input_Number[1]!="":
                    if len(Input_Number[1])==1:
                        Conversionnumber=int(Input_Number[1])*10
                    else:
                        Conversionnumber=int(Input_Number[1])
                    Output=Convert(int(Input_Number[0]))+" Rs "+Convert(Conversionnumber)+ " paise"
                else:      
                    Output=Convert(int(Input_Number[0]))+" Rs"
            else:
                if len(Input_Number[1])==1:
                    Conversionnumber=int(Input_Number[1])*10
                else:
                    Conversionnumber=int(Input_Number[1])
                Output=Convert(Conversionnumber)+" paise"
        else:
            Output=Convert(int(Input_Number))+" Rs"
    return Output
    
if __name__=="__main__":
    Input_Number=input("Enter the number to be converted:")
    print(Number_2_word(Input_Number))