# test1.py
#import the library
import streamlit as st
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix, recall_score,classification_report
from sklearn.model_selection import train_test_split
import altair as alt
import streamlit.components.v1 as components
import datetime
import streamlit as stl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 




# add title
st.title('CEI 523 Assignment 2021 📈')
st.info('Case study for our given data for predictive maintenance')
st.text("")
st.markdown("### Given data")
st.markdown("---")
st.text("")

dataset = pd.read_csv('https://github.com/itsheleng/test2/blob/3f6d2c0cfbdbeebbf2f6fb07fbdbee577004479c/data.csv', error_bad_lines=False )

st.sidebar.text("")
st.sidebar.text("")



data=pd.read_csv("data.csv")

st.write(data)
st.text("")
st.markdown("We decided to use *LinearSVC* algorithm. Following this decision we found out this:")
st.markdown("### LinearSVC")

st.markdown("---")



X = data[['Air_temperature', 'Process_temperature', 'Rotational_speed', 'Torque','Tool_wear']]
y = data.Machine_failure

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


st.text(" Checking if the column Product ID is unique!") 
data['Product_ID'].is_unique
st.text("Replace zero with mean")


data["Tool_wear"]=data["Tool_wear"].astype("int32")
m=data["Tool_wear"].mean()
data["Tool_wear"]=data["Tool_wear"].replace(0,m)

data



model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=1e5)
model.fit(X_train, y_train)

gnb = GaussianNB()
yGNB_pred = gnb.fit(X_train, y_train).predict(X_test)


predictions = model.predict(X_test)

ySVC_pred = model.fit(X_train, y_train).predict(X_test)


st.write(
    "Number of mislabeled points out of a total %d points : %d"
    % (X_test.shape[0], (y_test != ySVC_pred).sum())
)

st.markdown("Taking under consideration these results we thought that trying the Naive Bayes algorithm could be helpful in our case. Turned out that we were right, since it is visible from our results.")
st.markdown("### Gaussian Naive Bayes")
st.markdown("---")

predictions1 = gnb.predict(X_test)
st.markdown("Confusion Matrix:")
st.write(confusion_matrix(y_test, predictions1))
st.markdown("Accuracy Score:")
st.write(accuracy_score(y_test, predictions1))
st.markdown("F1 score:")
st.write(f1_score(y_test, predictions1))
st.markdown("Recall:")
st.write(recall_score(y_test, predictions1))

st.write(
    "Number of mislabeled points out of a total %d points : %d"
    % (X_test.shape[0], (y_test != yGNB_pred).sum())
)



plt.scatter(y_test, predictions1,  color='gray')
plt.plot(y_test,predictions1, color='red', linewidth=2)
plt.show()



st.sidebar.text("")
st.sidebar.text("")
st.sidebar.title("🔗 Sources")
st.sidebar.info('[Given Data](https://drive.google.com/file/d/1cEMvten1WEJTae9xRw0JNezHrZZhhT9o/view?usp=sharing)'+'\r')

st.sidebar.title("🛈 About")
st.sidebar.info('Created and maintained by:'+'\r'+'[Eleni Giakoumi](eg.giakoumi@edu.cut.ac.cy)'+'[ Andreas Othonos](am.othonos@edu.cut.ac.cy)'+'[ Andriani Petrou](ae.petrou@edu.cut.ac.cy)')
