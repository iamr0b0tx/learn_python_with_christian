'''
Collect an Input of a user score
and check which Grade he/she has

0  - 39  F
40 - 44  E
45 - 49  D
50 - 59  C
60 - 69  B
70 - 100 A
'''

def validateInput(score_input, verbose=False):
    try:
        score_input = int(score_input)

        if 0 <= score_input <= 100:
            return score_input

        if verbose:
            print('Score should be between 1 and 100!\n')
    
    except:
        if verbose:
            print('Invalid Score Input!\n')
        
        
def getInput():
    while True:
        score_input = input('Please type in the score: ')
        score_input = validateInput(score_input)

        if score_input is not None:
            return score_input
        
def gradeScore(score_arg):
    if 0 <= score_arg <= 39:
        return 'F'

    elif score_arg in range(40, 45):
        return 'E'

    elif score_arg >= 44 and score_arg <50:
        return 'D'

    elif 45 <= score_arg <= 49:
        return 'C'

    elif 50 <= score_arg <= 59:
        return 'B'

    elif 60 <= score_arg <= 69:
        return 'B'

    elif 70 <= score_arg <= 100:
        return 'A'

def readScores(filepath):
    '''
    creates another file that contaains the student names and their grades
    '''

    student_scores_file_object = open(filepath, 'r')
    
    for line in student_scores_file_object:
        name, score = line.split()

        score = validateInput(score, True)
        if score is None:
            grade = 'Invalid Score'

        else:
            grade = gradeScore(score)
        print(f'name = {name}, score = {score}, grade = {grade}')
##
##    open('student_grades.txt', 'w')

    student_scores_file_object.close()
    return


def scoreByInput():
    score = getInput()
    gradeScore(score, True)

def scoreByFile():
    filepath = 'student_scores.txt'
    readScores(filepath)

scoreByFile()






