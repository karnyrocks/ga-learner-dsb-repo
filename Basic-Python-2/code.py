# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)
#New record

new_record=[50,  9,  4,  1,  0,  0, 40,  0]
data2=np.array([new_record])
print(data2)
census=np.concatenate((data2,data),axis=0)
print(census)
#Code starts here



# --------------
#Code starts here
age=census[0: ,0]
max_age=age.max()
min_age=age.min()
age_mean=np.mean(age)
age_std=age.std()



# --------------
#Code starts here
race_0=census[census[ : ,2]==0]
race_1=census[census[ : ,2]==1]
race_2=census[census[ : ,2]==2]
race_3=census[census[ : ,2]==3]
race_4=census[census[ : ,2]==4]

print(race_0)

len_0=race_0.shape[0]
len_1=race_1.shape[0]
len_2=race_2.shape[0]
len_3=race_3.shape[0]
len_4=race_4.shape[0]
print(len_0,len_1,len_2,len_3)


 
length=np.array([len_0,len_1,len_2,len_3,len_4])
minority_race=length.argmin()
print(minority_race)


# --------------
#Code starts here
senior_citizens=census[census[ : ,0]>60]

workinghours=np.sum(senior_citizens,axis=0)
print(workinghours)
working_hours_sum=workinghours[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[ : ,1]>10]
low=census[census[ : ,1]<=10]
avg_pay_high=high.mean(axis=0)[7]
print(avg_pay_high)
avg_pay_low=low.mean(axis=0)[7]
print(avg_pay_low)
if(avg_pay_high>avg_pay_low):
    print(avg_pay_high)
else:
    print(avg_pay_low)



