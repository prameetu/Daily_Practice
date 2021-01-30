import pandas as pd

sal = pd.read_csv('Salaries.csv')

print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'])
print(sal.loc[sal['TotalPayBenefits'].argmax()]['EmployeeName'])

print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'])

print(sal.groupby('Year').mean()['BasePay'])

print(sal['JobTitle'].nunique())

print(sal['JobTitle'].value_counts().head())

print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(chief_string)))