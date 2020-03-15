import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

# Load data for subject "Math".
math = pd.read_csv('student/student-mat.csv', sep=";")
print(math.shape)  # (395, 33)
# add an extra column ['subject] to math DataFrame.
math.insert(1, 'subject', ['math'] * 395)

# Load data for subject "Portuguese".
portuguese = pd.read_csv('student/student-por.csv', sep=";")
print(portuguese.shape)  # (649, 33)
# add an extra column ['subject] to portuguese dataframe.
portuguese.insert(1, 'subject', ['por'] * 649)

# Concatenate both DataFrame vertically
students = pd.concat([math, portuguese])
# Check and make sure the concatenation is correct
assert math.shape[0] + portuguese.shape[0] == students.shape[0], 'merge error'
assert math.shape[1] == portuguese.shape[1] == students.shape[1], 'merge error'

# Sort out the all the column names with data type object
text_columns = []
dataTypeDict = dict(students.dtypes)
for col in dataTypeDict:
    if dataTypeDict[col] == 'O':
        text_columns.append(col)
print(text_columns)
print(students.shape)
print(students.head())
print(students.describe())
# convert all the two-answers categorical features to integers: (Mjob, Fjob, reason, guardian, needs one-hot-encoding method to convert into numerical data)
students['school'] = students['school'].map({'GP':0, "MS":1})
students['subject'] = students['subject'].map({'math':0, "por":1})
students['sex'] = students['sex'].map({'F':0, "M":1})
students['address'] = students['address'].map({'U':0, "R":1})
students['famsize'] = students['famsize'].map({'GT3':0, "LE3":1})
students['Pstatus'] = students['Pstatus'].map({'A':0, "T":1})
students['schoolsup'] = students['schoolsup'].map({'no':0, "yes":1})
students['famsup'] = students['famsup'].map({'no':0, "yes":1})
students['paid'] = students['paid'].map({'no':0, "yes":1})
students['activities'] = students['activities'].map({'no':0, "yes":1})
students['nursery'] = students['nursery'].map({'no':0, "yes":1})
students['higher'] = students['higher'].map({'no':0, "yes":1})
students['internet'] = students['internet'].map({'no':0, "yes":1})
students['romantic'] = students['romantic'].map({'no':0, "yes":1})


print(students.info())






sorted_by_studytime_df = students.sort_values('studytime')
plt.figure(figsize=(12, 8))
sns.set()
sns.lineplot('studytime', 'G3', hue='sex', data=sorted_by_studytime_df)
plt.xlabel('studytime (hours/week)')
plt.ylabel('Grade')
plt.xticks([1,2,3,4], ('less than 2h', '2-5hrs', '5-10hrs', 'more than 10hrs'))
plt.legend(labels=['Female', 'Male'])
plt.title('Studytime on final grade')
plt.show()
plt.close()


#sorted_by_studytime_df = students.sort_values('studytime')
#plt.figure(figsize=(12, 8))
#sns.set()
#sns.lineplot('studytime', 'G3', hue='sex', data=sorted_by_studytime_df)
#plt.xlabel('studytime (hours/week)')
#plt.ylabel('Grade')
#plt.xticks([1,2,3,4], ('less than 2h', '2-5hrs', '5-10hrs', 'more than 10hrs'))
#plt.legend(labels=['Female', 'Male'])
#plt.title('Studytime on final grade')
#plt.show()
#plt.close()
