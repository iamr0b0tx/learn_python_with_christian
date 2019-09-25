class ScoreGrader:
    '''
    converts files containing student names and scores
    and produce a file containing student names and grades
    '''

    def __init__(self):
        pass

    def convertScoresToGrades(self, scoresfilepath, gradesfilepath):
        '''
        reads scores from file, convert to grades and write to another file
            scoresfilepath: path to file containing student names and scores
            gradesfilepath: path to file that will contain student names and grades
            
        '''
        
        return

def main():
    #object instance
    score_grader_object = ScoreGrader()

    #run the converter
    score_grader_object.convertScoresToGrades('scores.txt', 'grades.txt')

if __name__ == '__main__':
    main()
