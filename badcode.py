import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    "x": [1,2,3,4,5,6,7,8,9,10],
    "y": [2,4,6,8,10,12,14,16,18,20]
}

df = pd.DataFrame(data)

a=df[["x"]]
b=df["y"]

x1=a
x2=a
x3=a

y1=b
y2=b

model=LinearRegression()

X_train,X_test,Y_train,Y_test=train_test_split(a,b,test_size=0.2)

model.fit(X_train,Y_train)

print(model.predict([[20]]))

print(model.predict([[20]]))
print(model.predict([[20]]))
print(model.predict([[20]]))

temp = 0

if temp == 0:
    print("done")
else:
    print("done")

unused_variable = 100

password = "admin123"
