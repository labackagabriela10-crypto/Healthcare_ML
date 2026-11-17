
#Import
print("Pandas is working!")
import pandas as pd


#1 first partc (CHECKING DATA)
# Load the healthcare dataset
df = pd.read_csv("healthcare_dataset.csv")

# Display the first 5 rows
print(df.head())

# Display the number of rows and columns
print(df.shape)

# Display the column names
print(df.columns.tolist())

# Check the dataset structure
print("\n--- DATASET INFORMATION ---")
df.info()

# Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Check duplicate rows
print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

#2 Duble checking, deeper understanding the dataset
# Display the first 10 rows
print("\n--- FIRST 10 ROWS ---")
print(df.head(10))

# Count the different blood types
print("\n--- BLOOD TYPE COUNTS ---")
print(df["Blood Type"].value_counts())

# Count the different medical conditions
print("\n--- MEDICAL CONDITION COUNTS ---")
print(df["Medical Condition"].value_counts())

#I need to check if there is conncection between blood and illness
# Compare blood types and medical conditions
print("\n--- BLOOD TYPE AND MEDICAL CONDITION ---")

comparison = pd.crosstab(
    df["Blood Type"],
    df["Medical Condition"]
)

print(comparison)

from scipy.stats import chi2_contingency


# Perform the Chi-square test
chi2, p_value, dof, expected = chi2_contingency(comparison)

print("\n--- CHI-SQUARE TEST ---")
print("Chi-square statistic:", chi2)
print("P-value:", p_value)

# Interpret the result
if p_value < 0.05:
    print("There is a statistically significant association.")
else:
    print("There is no statistically significant association.")

