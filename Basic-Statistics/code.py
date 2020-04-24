# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
data["Gender"].replace("-","Agender",inplace=True)
print(data.head())
gender_count=data["Gender"].value_counts()
gender_count.plot.bar()
#Code starts here 




# --------------
#Code starts here
alignment=data["Alignment"].value_counts()
alignment.plot.pie()
plt.title("Character Alignment")


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
print(sc_df.head())
sc_covariance=sc_df.cov().iloc[1,0]


sc_strength=sc_df["Strength"].std()
sc_combat=sc_df['Combat'].std()
sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)


ic_df=data[['Intelligence','Combat']]
print(ic_df.head())
ic_covariance=ic_df.cov().iloc[1,0]


ic_intelligence=ic_df["Intelligence"].std()
ic_combat=ic_df['Combat'].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)

print(ic_pearson)



# --------------
#Code starts here
total_high=data["Total"].quantile(0.99)
print(total_high)


super_best=data[data["Total"]>total_high]
print(super_best.head())

super_best_names=list(super_best["Name"])
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3)
data["Intelligence"].plot.box(ax=ax_1)
data["Speed"].plot.box(ax=ax_2)
data["Power"].plot.box(ax=ax_3)



