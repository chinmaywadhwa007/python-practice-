# import statment
import pandas as pd
import pandas
a = [1, 2, 3, 4, 5]
print(pandas.Series(a))

a = [1, 2, 3, 4, 5]
print(pd.Series(a))

# create label by your own
a = [1, 2, 3, 4, 5]
b = pd.Series(a, index=["a", "b", "c", "d", "e"])
print(b)
print(b["a"])

# note we have notice something in the o/p dtype:int64
# means stands for data type when pandas creates series it stores all the values in a numpy array internally since values are in integers pandas chooses the numpy daya type int64


# key/values
students = {1: "chinmay", 2: "wadhwa", 3: "devloper"}
a = pd.Series(students)
print(a)

# data frames
data = {
    "id": [1, 2, 3, 4, 5, 6],
    "marks": [65, 43, 23, 54, 64, 23]
}
a = pd.DataFrame(data)
print(a)

# locate the rows
data = {
    "id": [1, 2, 3, 4],
    "hoobies": ["cricket", "basketball", "vollyball", "football"]
}
df = pd.DataFrame(data)
# .loc selects rows by their label (index)

print(df.loc[[0]])

stud_data = [

    (1, "chinmay", "24", "male", "jaipur"),
    (2, "chinmay", "24", "male", "jaipur"),
    (3, "chinmay", "24", "male", "jaipur"),
    (4, "chinmay", "24", "male", "jaipur"),
    (5, "chinmay", "24", "male", "jaipur")
]
df = pd.DataFrame(stud_data, columns=[
                  "stud_data", "name", "age", "gender", "lcoation"])
print(df)

df = pd.DataFrame(
    {"names": ["chinmay", "rahul", "unknown gun man"], "marks": [100, 56, 99]})
print(df)

data = {
    'emp_id': [101, 102, 103, 104, 105, 106],
    'emp_name': ["alice", "neha", "john", "rohit", "shyam", "rohan"],
    'emp_dept': ['HR', 'IT', 'IT', 'Sales', 'HR', 'Sales'],
    'Age': [25, 30, 35, None, None, 50],
    'Salary': [50000, 60000, 70000, 52000, 88000, 90000],
    'Experience': [2, 6, 8, 10, 3, 24]
}
df = pd.DataFrame(data)
print(df)

df = pd.read_csv("E:\Destop\phyton\pandas\sample-simple.csv")
print(df)
"/n"
df = pd.read_csv("E:\Destop\phyton\pandas\sample-simple.csv")
print(df.tail())

print(df.describe())
print(df.info())
print(df[["first_name","last_name","email","age","salary","city","joined"]])
print(df.sort_values("salary"))# for salary from decending order
print(df.sort_values("salary",ascending=False)) #for salary from acending order 
print(df.shape)