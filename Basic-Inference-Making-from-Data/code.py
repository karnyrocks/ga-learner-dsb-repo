# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]
data=pd.read_csv(path)


data_sample=data.sample(n=sample_size,random_state=0)
sample_mean=data_sample["installment"].mean()
sample_std=data_sample["installment"].std()


margin_of_error=z_critical*(sample_std/(sample_size**0.5))

confidence_interval=[sample_mean-margin_of_error,sample_mean+margin_of_error]

true_mean=data["installment"].mean()

if(true_mean>=confidence_interval[0] and true_mean<=confidence_interval[1]):
    print("True")
else:
    print("False")






#Code starts here



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1,figsize=(20,10))
axes=[ax_1,ax_2,ax_3]
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        m.append(data["installment"].sample(sample_size[i]).mean())
        j=j+1
    mean_series=pd.Series(m) 
    axes[i] = mean_series.plot.hist(bins=12, alpha=0.5)
    i=i+1   





#Code starts here



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here




data['int.rate'] = data['int.rate'].map(lambda x: x.rstrip('%'))


data["int.rate"]=data["int.rate"].astype(float)/100

print(data.head(100))
x1=data[data['purpose']=='small_business']['int.rate']
value=data["int.rate"].mean()
z_statistic,p_value=ztest(x1,value=data["int.rate"].mean(),alternative='larger')
print(p_value)
if(p_value<0.05):
    print("Reject")
else:
    print('Accept')    



# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic,p_value=ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2=data[data['paid.back.loan']=='Yes']['installment'])

if(p_value<0.05):
    print("Reject")
else:
    print("Accept")    


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes=data[data["paid.back.loan"]=="Yes"]["purpose"].value_counts()
no=data[data["paid.back.loan"]=="No"]["purpose"].value_counts()


observed=pd.concat([yes.transpose(),no.transpose()],axis=1,keys= ['Yes','No'])
print(observed.head())
chi2, p, dof, ex=chi2_contingency(observed)
if(chi2>critical_value):
    print("Reject")
else:
    print("Accept")    


