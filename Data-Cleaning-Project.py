# Creating project 1 by using python + numpy + pandas + matplotlib
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
# Loading the employee dataset
df = pd.read_csv('sample_employees.csv ')
# Displaying the first few row of the dataset by using head() function



# Check for missing values, duplicates, or incorrect data (introduce some manually if needed).
print(df.isnull().sum())  # Check for missing values
print("==========================================")
print(df.duplicated().sum())  # Check for duplicates
print("==========================================")
print(df.describe())  # Get a statistical summary of the dataset
print("==========================================")
#Handle missing values (fill/replace/drop).
df.fillna(method= 'bfill', inplace=True)  # Forward fill missing values
df.drop_duplicates(inplace=True)  # Remove duplicates
# Display the cleaned dataset
print(df.head())

# Standardize text columns (e.g., make all city names lowercase).
df['City'] = df['City'].str.lower()  # Convert city names to lowercase
# Display the standardized dataset

# Saving the cleaned dataset to a new CSV file.
df.to_csv('cleaned_employees.csv', index=False)
print("Cleaned dataset saved to 'cleaned_employees.csv'.")
# Exploratory Data Analysis (EDA)
# Calculate average, min, max salary.
average_salary = df['Salary'].mean()
min_salary = df['Salary'].min()
max_salary = df['Salary'].max()
print(f"Average Salary: {average_salary}")
print(f"Minimum Salary: {min_salary}")
print(f"Maximum Salary: {max_salary}")

# Find the most common city employees belong to.
most_common_city = df['City'].mode()[0] # if i remove [0] it will return a series or 0 then it will return a string
print(f"Most Common City: {most_common_city}")

# Group data by city and compute the average salary & experience.
city_salary_experience = df.groupby('City').agg({'Salary': 'mean', 'Experience_Years': 'mean'}).reset_index()
print(city_salary_experience)

# Use NumPy to calculate statistical values like mean, median, variance for age/salary.
salary_mean = np.mean(df['Salary'])
salary_median = np.median(df['Salary'])
salary_variance = np.var(df['Salary'])
print("Salary Statistics:")
print(f"Salary Mean: {salary_mean}")
print(f"Salary Median: {salary_median}")
print(f"Salary Variance: {salary_variance}")

# Data Visualization
# Plot a bar chart of average salaries by city.
plt.figure(figsize=(10, 6))
plt.bar(city_salary_experience['City'], city_salary_experience['Salary'], color='skyblue')
plt.title('Average Salary by City')
plt.xlabel('City')
plt.ylabel('Average Salary')
plt.savefig('average_salary_by_city.png')
plt.show()
# Plot a histogram of employee ages.
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Employee Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Employees')
plt.savefig('employee_age_distribution.png')
plt.show()

# Plot a scatter plot of Experience vs Salary to see correlation.
plt.figure(figsize=(10, 6))
plt.scatter(df['Experience_Years'], df['Salary'], color='purple', alpha=0.5)
plt.title('Experience vs Salary')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.savefig('experience_vs_salary.png')
plt.show()

# Advanced Analysis
# Find top 5 highest-paid employees.
top_5_highest_paid = df.nlargest(5, 'Salary')
print("Top 5 Highest Paid Employees:", top_5_highest_paid[['Name', 'Salary']])

# Identify correlation (using df.corr()) between age, salary, and experience.
correlation_matrix = df[['Age', 'Salary', 'Experience_Years']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Create a new column Salary_Level (Low, Medium, High) based on salary ranges.
def categorize_salary(salary):
    if salary < 50000:
        return 'Low'
    elif 50000 <= salary < 100000:
        return 'Medium'
    else:
        return 'High'
df['Salary_Level'] = df['Salary'].apply(categorize_salary)
print("Dataset with Salary Level:", df[['Name', 'Salary', 'Salary_Level']].tail())


    
    