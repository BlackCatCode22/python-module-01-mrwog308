###########################
#   ex033.py Grade calc   #
# #########################

#print('py4e')
score = input('Enter Score: ')
try:
    score = float(score)
    if score < 0.0 or score > 1.0:
        raise ValueError('Bad Score')
    
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    
    print('Grade:', grade)
except:
    print('Bad Score')
    # exit(1)