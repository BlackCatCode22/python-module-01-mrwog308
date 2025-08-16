######################################
#   ex031.py gross pay calc w/1.5x   #
# ####################################

#print('py4e')
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    if float(hours) > 40:
        regular_pay = 40 * float(rate)
        overtime_pay = (float(hours) - 40) * float(rate) * 1.5
        pay = regular_pay + overtime_pay
    pay = float(hours) * float(rate)
    # pay = hours * rate
    print('Pay:',pay)
    print('Straight Time hours:', hours)
    print('Overtime hours:', float(hours) - 40 if float(hours) > 40 else 0)
except:
    print('A common mistake when attempting to design a foolproof program' \
    ' is to underestimate the inguenuity of complete fools. Please enter numeric values for hours and rate.')
    # exit(1)