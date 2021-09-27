'''Popular python libraries for ML
Numpy--> which provides multidimensional array
Pandas-->which is data analysis library that provides the concepts call dataframe,
        A dataframe is a 2D data structure similar to excel spreadsheet, we can select data in rows and column
MatPlotLib-->which is a 2D plotting library for creating graphs and plots.
Scikit-Learn-->which provides all common algorithm like decision tree, Neural network and so.

Jupyter:
Jupyter is best suitable for the ML, because we frequently need to inspect data, and its very hard in VS code,
and terminal, to install jupyter we use platform called Anaconda
'''

'''
Importing a data set

WE need to download the dataset from the website called 'Kaggle.com'
It's place to load data science projects

'''

# import pandas as pd
#
# df = pd.read_csv("vgsales.csv")
# print(df)


'''
Attributes of pandas: 
shape-->it give shape, Its a 2D array of shape
describe()--> to basics statistics of data inclues min, devation etc
value-->returns a 2D array,  [   []<--indicate inner array   ]<--repr outer array

'''
# print(df.shape)
# print(df.describe())
# print(df.values)


'''Music prediction:
steps: 1. Improt the data
    2. Clean the data-->removing duplicates/irrelavant in data, converting into numerical based value
    3. Split the data into Training/Test Sets-->  
    4. Create a Model-->selecting the algorithm
    5. Train the Model-->
    6. Make predictions-->
    7. Evaluate and Improve--> 
'''

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv("music.csv")
print(music_data)
# split the data input set and output set
x = music_data.drop(columns=['genre'])   # first splitting for training
# print(x)
y = music_data['genre']    # and second for Testing
# print(y)
#
model = DecisionTreeClassifier()
'''fit()--> this method take two data set, input set and outuy set'''
model.fit(x, y)  # here we are training the model
'''finally we ask our model to make prediction'''
predictions = model.predict([[21, 1], [22, 0]])
print(predictions)


'''To measure the accuracy'''

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
#
# music_data = pd.read_csv("music.csv")
# # print(music_data)
#
# x = music_data.drop(columns=['genre'])  # first splitting for training
# # print(x)
# y = music_data['genre']  # and second for Testing
# # print(y)
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8)  # last arg--> allocating the data for 20 percent
#
# model = DecisionTreeClassifier()
# model.fit(x_train, y_train)
# predictions = model.predict(x_test)
#
# score = accuracy_score(y_test, predictions)
# print(score)


'''Persisting Model
joblib--> this object has methods for saving and loading the models
'''
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.externals import joblib
#
# # music_data = pd.read_csv("music.csv")
# # print(music_data)
# # x = music_data.drop(columns=['genre'])   # first splitting for training
# # y = music_data['genre']    # and second for Testing
# #
# # model = DecisionTreeClassifier()
# # model.fit(x, y)
#
# # joblib.dump(model, 'music-recommender.joblib')  # for storing the model its a binary file
#
#
# model = joblib.load('music-recommender.joblib')  # for loading a model
# predictions = model.predict([[21, 1], [22, 0]])
# print(predictions)

'''visualing a tree: How this model make the predictions'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data = pd.read_csv("music.csv")
print(music_data)
x = music_data.drop(columns=['genre'])   # first splitting for training
y = music_data['genre']    # and second for Testing

model = DecisionTreeClassifier()
model.fit(x, y)

tree.export_graphviz(model, out_file='music-recommender.dot',
                     feature_names=['age', 'gender'],
                     class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)
