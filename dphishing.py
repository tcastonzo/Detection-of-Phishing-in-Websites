#rajesh m
import p1
import p2
import p3
import p4
import pandas as pd

website = str(input("Enter website name=> "))
p1.category1(website)
p2.category2(website)
p3.category3(website)
p4.category4(website)


read = pd.read_csv(r'phishing5.txt',header = None,sep = ',')
read = read.iloc[:,:-1].values
dataset = pd.read_csv(r'Training Dataset1.csv')
X = dataset.iloc[:,:-1].values 	
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 1001)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10,criterion = "mse",random_state = 2)
regressor.fit(X_train,y_train)                             

y_pred = regressor.predict(X_test)


from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(estimator = regressor,X=X_train,y=y_train,cv = 5)
accuracy.mean()
accuracy.std()


Detect_phishing_website = regressor.predict(read)

if Detect_phishing_website == 1:
    print("legitimate website")
elif Detect_phishing_website == 0:
    print ('suspicious website')
else:
    print('phishing website')
