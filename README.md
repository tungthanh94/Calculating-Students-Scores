# General
This is a program used for calculating students' scores.

## File Input
The students' answers of the class are stored in txt file in the `Data Files` folder.  
Each file line contains the student's ID and his/her answers, with below format:
`N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D`
or
`N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D,`
- The first value is student's ID, which begin with an 'N' and follow by 8 digits.
- The following values are 25 anwers, which can be A, B, C or D, seperated by comma (','). If the student doesn't give the answer for a question, then it will be blank. 
File should not has any header or footer, just students scores.
The name of the file should be _name_of_class.txt_. For example, 'class1.txt'.
## File Output
The final score for each class will be stored in the `Output` folder.
Each line contains the student's ID and his/her score.
The file name will be depend on the input. For example, if the input file name is 'class1.txt', the output file will be 'class1_grades.txt'

# How to run
Just put the input file in the `Data Files` folder, run the program file, then enter class name.
