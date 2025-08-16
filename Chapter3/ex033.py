###########################
#   ex033.py Grade calc   #
# #########################

#print('py4e')
score = input('Enter Score: ')
try:
    score = float(score)
    if score < 0.0 or score > 1.0:
        raise ValueError("Score must be between 0.0 and 1.0")
    
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
    print('Invalid input. Please enter a numeric value between 0.0 and 1.0 for the score.')
    # exit(1)