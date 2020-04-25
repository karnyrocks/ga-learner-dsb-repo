# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)

p_a=len(df[df["fico"]>700])/len(df["fico"])

df1=df[df["purpose"]=="debt_consolidation"]
p_b=len(df1)/len(df["purpose"])


p_a_b=len(df1[df1["fico"]>700])/len(df[df["fico"]>700])

result=p_a_b==p_a
print(result)
# code ends here


# --------------
# code starts here
prob_lp=len(df[df["paid.back.loan"]=="Yes"])/len(df)
print(prob_lp)
prob_cs=len(df[df["credit.policy"]=="Yes"])/len(df)
print(prob_cs)

new_df=df[df["paid.back.loan"]=="Yes"]

prob_pd_cs=len(new_df[new_df["credit.policy"]=="Yes"])/len(new_df)
print(prob_pd_cs)

bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
fig, (ax_1, ax_2) = plt.subplots(1,2, figsize=(20,10))

var1=df["purpose"].value_counts()

var1.plot(kind="bar",ax=ax_1)
df1=df[df["paid.back.loan"]=="No"]

df1["purpose"].value_counts().plot.bar(ax=ax_2)
# code ends here


# --------------
# code starts here
fig, (ax_1, ax_2) = plt.subplots(1,2, figsize=(20,10))

inst_median=df["installment"].median()

inst_mean=df["installment"].mean()

df["installment"].plot.hist(ax=ax_1)
df["log.annual.inc"].plot.hist(ax=ax_2)
plt.legend()
# code ends here


