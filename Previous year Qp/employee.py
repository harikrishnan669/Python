import pandas as pd

data = {
    'name': [
        'Alice Johnson', 'Bob Smith', 'Charlie Davis', 'Diana Adams', 'Ethan Brown',
        'Fiona Lee', 'George White', 'Hannah Green', 'Ian Black', 'Julia Stone'
    ],
    'gender': [
        'Female', 'Male', 'Male', 'Female', 'Male',
        'Female', 'Male', 'Female', 'Male', 'Female'
    ],
    'start_date': [
        '2018-03-15', '2017-06-22', '2019-01-10', '2020-09-05', '2016-11-30',
        '2021-07-19', '2015-05-14', '2018-08-01', '2022-02-20', '2019-12-11'
    ],
    'salary': [
        75000, 68000, 82000, 91000, 99000,
        60000, 105000, 72000, 63000, 78000
    ],
    'team': [
        'Engineering', 'Marketing', 'Sales', 'Engineering', 'Finance',
        'Marketing', 'Management', 'Sales', 'Finance', 'Engineering'
    ]
}
df = pd.DataFrame(data)
df.to_csv('employee.csv', index=False)
df = pd.read_csv('employee.csv')

print("First 7 records:")
print(df.head(7))

print("Employee names in alphabetical order:")
print(df['name'].sort_values())

highest_salary_employee = df.loc[df['salary'].idxmax(), 'name']
print("Employee with the highest salary:")
print(highest_salary_employee)

print("Male employees:")
print(df[df['gender'].str.lower() == 'male']['name'])

print("Teams employees belong to:")
print(df['team'].unique())
