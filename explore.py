import pandas as pd

def stat_function():
  print("Type 1 for minimum value of each column \nType 2 for maximum of each column \nType 3 for mean of each column \nType 4 for standard deviation of each column")
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  df = pd.read_csv('iris.csv')

  try:
    input_value = int(input("Enter number to select: "))
    if input_value == 1:
        print("You have selected minimum value.")
        col1 = round(df.iloc[:,0].min(),2)
        col2 = round(df.iloc[:,1].min(),2)
        col3 = round(df.iloc[:,2].min(),2)
        col4 = round(df.iloc[:,3].min(),2)
        print("Minimum value of sepal length is {0},sepal width is {1},petal length is {2},petal width is {3}.".format(col1,col2,col3,col4))

    elif input_value == 2:
        print("You have selected maximum value.")
        col1 = round(df.iloc[:,0].max(),2)
        col2 = round(df.iloc[:,1].max(),2)
        col3 = round(df.iloc[:,2].max(),2)
        col4 = round(df.iloc[:,3].max(),2)
        print("Maximum value of sepal length is {0},sepal width is {1},petal length is {2},petal width is {3}.".format(col1,col2,col3,col4))

    elif input_value == 3:
        print("You have selected mean value.")
        col1 = round(df.iloc[:,0].mean(),2)
        col2 = round(df.iloc[:,1].mean(),2)
        col3 = round(df.iloc[:,2].mean(),2)
        col4 = round(df.iloc[:,3].mean(),2)
        print("Mean of sepal length is {0},sepal width is {1},petal length is {2},petal width is {3}.".format(col1,col2,col3,col4))    

    elif input_value == 4:
        print("You have selected standard deviation value.")
        col1 = round(df.iloc[:,0].std(),2)
        col2 = round(df.iloc[:,1].std(),2)
        col3 = round(df.iloc[:,2].std(),2)
        col4 = round(df.iloc[:,3].std(),2)
        print("Standard deviation of sepal length is {0},sepal width is {1},petal length is {2},petal width is {3}.".format(col1,col2,col3,col4))    
  
  except Exception as e:
    print("Exception",e)


stat_function()