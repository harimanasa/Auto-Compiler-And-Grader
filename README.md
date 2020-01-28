# Auto-Compiler-And-Grader
Developed Python scripts to automate grading 60 students’ homework assignments and rubric for the course CMPE 180A: Algorithms and Data Structures. Working under Prof. Juan Gomez.



How to test:

1. mkdir test. Copy Grading_script_HW.py and grader main & Ideal output file in test.

2. mkdir test/submissions. Place your submitted (.h, .cc) files in it.

3. cd test. Run "python3 Grading_script_HW.py"

4. Output file is FinalResults_differences_withIdeal.txt in which the test results are populated.

 
 
Grading criteria:

In FinalResults_differences_withIdeal.txt, it checks the differences between Ideal_output.txt and each program output.

a) If there are no differences, it is graded 100 points.

b) If some differences are found, it is graded as per test cases.

c) If compilation terminated, it is graded 0 marks.
