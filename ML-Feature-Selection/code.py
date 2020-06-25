# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here
dataset=pd.read_csv(path)

# read the dataset
print(dataset.loc[ :5, : ])


# look at the first five columns


# Check if there's any column which is not useful and remove it like the column id
dataset=dataset.drop(["Id"],axis=1)

# check the statistical description
print(dataset.info())




# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 
cols=dataset.columns

#number of attributes (exclude target)
size=len(cols)-1

#x-axis has target attribute to distinguish between classes
x=cols[size]
y=cols[0:size]
print(y)
print(x)
#y-axis shows values of an attribute

#Plot violin for all attributes
for i in range (0,size):
    sns.violinplot(data=dataset,x=x,y=y[i])
    plt.show()

  



# --------------
import numpy
upper_threshold = 0.5
lower_threshold = -0.5


# Code Starts Here
subset_train=dataset.iloc[ : ,0:10]

data_corr=subset_train.corr()

sns.heatmap(data_corr)
correlation=data_corr.unstack().sort_values(kind='quicksort')


corr_var_list=correlation[((correlation>upper_threshold) | (correlation<lower_threshold)) & (correlation!=1) ]
print(corr_var_list)


# Code ends here




# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler

# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)

X=dataset.drop(["Cover_Type"],axis=1)
Y=dataset["Cover_Type"]

X_train, X_test, Y_train, Y_test=cross_validation.train_test_split(X,Y,test_size=0.2,random_state=0)

# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.
scaler=StandardScaler()
X_train_temp=scaler.fit_transform(X_train.iloc[:,0:size])
X_test_temp=scaler.transform(X_test)
#Standardized
#Apply transform only for continuous data


#Concatenate scaled continuous data and categorical
X_train1=numpy.concatenate((X_train_temp,X_train),axis=1)
X_test1=numpy.concatenate((X_test_temp,X_test),axis=1)

print(X_train.head())
print("="*50)
print(X_train1)

print(X_train.index)
scaled_features_train_df=pd.DataFrame(data=X_train_temp,index=X_train.index,columns=X_train.columns)

scaled_features_test_df=pd.DataFrame(data=X_test_temp,index=X_test.index,columns=X_test.columns)





# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif


# Write your solution here:

skb=SelectPercentile(score_func=f_classif,percentile=90)
predictors=skb.fit_transform(scaled_features_train_df,Y_train)

scores=skb.scores_
print(scores)
Features=X_train.columns

print(len(Features),len(scores))
d={"Features":Features,"Scores":scores}
dataframe=pd.DataFrame(d)
dataframe=dataframe.sort_values(by=["Scores"],ascending=False)
print(dataframe.head())

top_k_predictors = list(dataframe['Features'][:predictors.shape[1]])

print(top_k_predictors)



# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score


clf=LogisticRegression(multi_class='ovr')
clf1=LogisticRegression(multi_class='ovr')


model_fit_all_features=clf1.fit(X_train,Y_train)

predictions_all_features=model_fit_all_features.predict(X_test)
score_all_features=accuracy_score(Y_test,predictions_all_features)
print(score_all_features)


model_fit_top_features=clf.fit(scaled_features_train_df[top_k_predictors],Y_train)

predictions_top_features=model_fit_top_features.predict(scaled_features_test_df[top_k_predictors])
score_top_features=accuracy_score(Y_test,predictions_top_features)
print(score_top_features)




