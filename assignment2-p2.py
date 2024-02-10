import pandas as pd 

# Q1: Read Salaries.csv as a dataframe called sal
sal = pd.read_csv('Salaries.csv')
print(sal.head())

# Q2: Check the head of the DataFrame.
print("Head of the DataFrame:")
print(sal.head())

# Q3: Use the .info() method to find out how many entries there are.
print("\nInformation about the DataFrame:")
print(sal.info())

# Q4: What is the average BasePay?
average_base_pay = sal['BasePay'].mean()
print("\nAverage BasePay:", average_base_pay)

# Q5: What is the highest amount of OvertimePay in the dataset?
highest_overtime_pay = sal['OvertimePay'].max()
print("\nHighest OvertimePay:", highest_overtime_pay)

# Q6: What is the job title of JOSEPH DRISCOLL? Note: Use all caps, there is also a lowercase Joseph Driscoll.
joseph_driscoll_job_title = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].iloc[0]
print("\nJob title of JOSEPH DRISCOLL:", joseph_driscoll_job_title)

# Q7: How much does JOSEPH DRISCOLL make (including benefits)?
joseph_driscoll_total_pay_benefits = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'].iloc[0]
print("\nTotal pay including benefits for JOSEPH DRISCOLL:", joseph_driscoll_total_pay_benefits)

# Q8: What is the name of the highest paid person (including benefits)?
highest_paid_person = sal.loc[sal['TotalPayBenefits'].idxmax()]['EmployeeName']
print("\nName of highest paid person (including benefits):", highest_paid_person)

# Q9: What is the name of the lowest paid person (including benefits)?
lowest_paid_person = sal.loc[sal['TotalPayBenefits'].idxmin()]['EmployeeName']
print("\nName of lowest paid person (including benefits):", lowest_paid_person)

# Q10: What was the average (mean) BasePay of all employees per year? (2011-2014)?
average_base_pay_per_year = sal.groupby('Year')['BasePay'].mean()
print("\nAverage BasePay of all employees per year:")
print(average_base_pay_per_year)

# Q11: How many unique job titles are there?
unique_job_titles_count = sal['JobTitle'].nunique()
print("\nNumber of unique job titles:", unique_job_titles_count)

# Q12: What are the top 5 most common jobs?
top_5_common_jobs = sal['JobTitle'].value_counts().head()
print("\nTop 5 most common jobs:")
print(top_5_common_jobs)

# Q13: How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurrence in 2013?)
job_titles_2013_count = sal[sal['Year'] == 2013]['JobTitle'].value_counts()
unique_job_titles_2013_count = sum(job_titles_2013_count == 1)
print("\nNumber of Job Titles represented by only one person in 2013:", unique_job_titles_2013_count)

# Q14: How many people have the word Chief in their job title?
chief_count = sal[sal['JobTitle'].str.contains('Chief', case=False)]['JobTitle'].count()
print("\nNumber of people with the word Chief in their job title:", chief_count)

# Q15: Is there a correlation between the length of the Job Title string and Salary?
sal['TitleLength'] = sal['JobTitle'].apply(len)
correlation = sal[['TitleLength', 'TotalPayBenefits']].corr().iloc[0, 1]
print("\nCorrelation between length of Job Title string and Salary:", correlation)