2. write a function that will accept two strings and return Boolean if they are anagram
 str1 = rail safety
 str2= fairy tales


def check_ang(str1, str2):
    A = sorted([x.lower() for x in str1 if x != ' '])
    B = sorted([x.lower() for x in str2 if x != ' '])
    return A == B

Write a SQL Query for the below output
 Input:
 emp_id name salary dept_id 
 ----------- ----------- ------------ -----------
 1 Alice 50000.00 1
 2 Bob 60000.00 2
 3 Charlie 50000.00 2
 4 Charlie 65000.00 2
 5 Eve 45000.00 1
 
 dept_id dept_name 
 ----------- ------------
 1 HR 
 2 Engineering 
 3 Sales 
 
 Output:
 dept_name employee_count highest_salary
 --------------- -------------- --------------
 Engineering 3 65000
 HR 2 50000
 Sales 0 0


SQL problem - 
solve in sql - You want to identify the hierarchy of employees based on the managerid.
employee 
id name managerid 
1 abc null
2 xyz 1
3 jhl 2
4 hfg 2 
if given id = 3 then output should be - 
abc 
xyz
jhl"
