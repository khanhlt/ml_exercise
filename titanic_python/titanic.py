import pandas as pd

test = pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

# plot relation between survived-died and age ranges
import matplotlib.pyplot as plt

survived = train[train["Survived"] == 1]
died = train[train["Survived"] == 0]
survived["Age"].plot.hist(alpha=0.5,color='red',bins=50)
died["Age"].plot.hist(alpha=0.5,color='blue',bins=50)
plt.legend(['Survived','Died'])
plt.show()

# process age
cut_points = [-1,0,5,12,18,35,60,100]
label_names = ['Missing', 'Infant', 'Child', 'Teenager', 'Young Adult', 'Adult', 'Senior']
def process_age(df,cut_points,label_names):
    df["Age"] = df["Age"].fillna(-0.5)
    df["Age_categories"] = pd.cut(df["Age"],cut_points,labels=label_names)
    return df

train = process_age(train, cut_points, label_names)
test = process_age(test, cut_points, label_names)

pivot = train.pivot_table(index='Age_categories',values='Survived')
pivot.plot.bar()
plt.show()

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

# create dummies
def create_dummies(df,column_name):
    dummies = pd.get_dummies(df[column_name],prefix=column_name)
    df = pd.concat([df,dummies],axis=1)
    return df

for column in ["Pclass", "Sex", "Age_categories"]:
    train = create_dummies(train, column)
    test = create_dummies(test, column)
# creating logistic regression model

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train[columns], train['Survived'])

# split data => to evaluate the accuracy of model
from sklearn.model_selection import train_test_split
all_X = train[columns]
all_y = train['Survived']

train_X, test_X, train_y, test_y = train_test_split(all_X, all_y, test_size=0.2, random_state=0)

# prediction's accuracy
from sklearn.metrics import accuracy_score
lr = LogisticRegression()
lr.fit(train_X, train_y)
predictions = lr.predict(test_X)
accuracy = accuracy_score(test_y,predictions)
print(accuracy)

# cross validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(lr, all_X, all_y, cv=10)
accuracy = scores.mean()
print(accuracy)

# prediction on unseen data
lr.fit(all_X, all_y)
test_predictions = lr.predict(test[columns])

# make submission file
test_ids = test["PassengerId"]
submission_df = {"PassengerId": test_ids, "Survived": test_predictions}
submission = pd.DataFrame(submission_df)
submission.to_csv("submission.csv", index=False)