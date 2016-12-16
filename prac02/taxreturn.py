__author__ = 'jc450453'
def tax_return(income):
    if income>=16000:
        print((income-16000)*.3)
        return (income-16000)*.3

    else:
        print("no need to pay tax")
        return 0

tax_return(12)