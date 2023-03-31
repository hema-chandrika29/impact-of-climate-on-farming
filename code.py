import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

waterrequirements=input("enter water requirement:")
soilmoisture=input("soil moisture is:")
rainfall=input()
irrigation=waterrequirements-(soilmoisture+rainfall)
print(f"irrigation value is {irrigation}")
 
# Load the CSV file
data = pd.read_csv('weather.csv')

# Separate the features and target variable
X = data.drop('ir1', axis=1)
y = data['ir1']
data.ir1
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose a machine learning algorithm and create an instance of the algorithm
#model = DecisionTreeClassifier()

# Train the model on the training data
#model.fit(X_train, y_train)
if rainfall==0:
     print("irrigate as usual.No probability of rain")
elif rainfall>0:
     print("Stop watering the crops")
else:
    print("------")
# Evaluate the model's performance on the testing data
#y_pred = model.predict(X_test)
#accuracy = accuracy_score(y_test, y_pred)
#print('Accuracy:', accuracy)
