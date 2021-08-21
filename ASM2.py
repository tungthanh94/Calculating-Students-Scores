import numpy as np
import pandas as pd

file = None
while file is None:
    try:
        
        n = input('Enter a class to grade (i.e. class1 for class1.txt): ')
              
        file = open(f'Data Files/{n}.txt', 'r')
        
        print(f'Successfully opened {n}.txt\n')
        print('**** ANALYZING ****\n')
    except:
        print('File cannot be found.\nPlease try again!')

invalid = 0
valid_line =[]
for i in file:
    line = i.strip().split(',')
    
    if len(line) != 26:
        print('Invalid line of data: does not contain exactly 26 values:')
        print(i, '\n')
        invalid += 1
        
    elif len(line[0]) != 9 or not line[0].startswith('N') or not line[0][1:].isnumeric():
        print('Invalid line of data: N# is invalid')
        print(i, '\n')
        invalid += 1
    else:
        
        valid_line.append(line)
        

if invalid == 0:
    print('No errors found!\n')
    
print('**** REPORT ****\n')
print('Total valid lines of data:', len(valid_line))
print('Total invalid lines of data:', invalid, '\n')


all_student = pd.DataFrame(valid_line)
all_student.set_index(0, inplace = True)
all_student.index.name = None
all_student.columns = list(range(0,25))

answer_key = pd.Series("B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(','))
all_student.replace('', 0, inplace = True)
all_student[all_student == answer_key] = 4
all_student[~all_student.isin([0,4])] = -1
all_student = all_student.astype(int)
score = all_student.sum(axis = 1)


score.to_csv(f'Output/{n}_grades.txt', header = False)
print('Mean (average) score: {:.2f}'.format(score.mean()))
print('Highest score:', score.max())
print('Lowest score:', score.min())
print('Range of scores:', score.max() - score.min())
print('Median score:', score.median(), '\n')