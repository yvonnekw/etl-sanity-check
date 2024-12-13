import pandas as pd
source = pd.read_csv("employee_sal.csv")
print("Test Case 1: Following are the column names in the source file : \n")
print(source.columns)
print("\n")
print("Test Case 2: Rows X columns in the source file \n")
print(source.shape)
print("\n")
print("Test Case 3: No. of rows under each columns \n")
print(source.count())
print("\n")

print("Test Case 4: Duplicate records in the source \n")
print(source.duplicated().sum())
print("\n")

print("Test Case 5: Duplicate records saved in the file below \n")
dupes = source[source.duplicated()].to_csv("employee_dupli2.csv")
print("\n")

print("Test Case 6: Check if NULL value exist in dept_name column \n")
print(source[source['dept_name'].isnull()])
print("\n")

print("Test Case 6a: Check if NULL value exist in salary column \n")
print(source[source['salary'].isnull()])
print("\n")

print("Test Case 7: Unique value of Eno column in the source \n")
print(source['Eno'].unique())
print("\n")

print("Test Case 8: Unique value of emp_name column in the source \n")
print(source['emp_name'].unique())
print("\n")

print("Test Case 9: Unique value of dept_name column in the source \n")
print(source['dept_name'].unique())
print("\n")

print("Test Case 10: Unique value of salary column in the source \n")
print(source['salary'].unique())
print("\n")

print("Test Case 11: Sample (top 5) records from source file \n")
print(source.head())
print("\n")

print("Test Case 12: Sample (bottom 5) records from source file \n")
print(source.tail())
print("Test Completed...... \n")