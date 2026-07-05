import pandas as pd

# ============================
# Load the CSV file
# ============================

df = pd.read_csv("Messy_Employee_dataset.csv")

print("Original Shape:", df.shape)

# ============================
# Remove duplicate rows
# ============================

df.drop_duplicates(inplace=True)

# ============================
# Remove leading and trailing spaces
# ============================

for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# ============================
# Standardize text columns
# ============================

text_columns = [
    "First_Name",
    "Last_Name",
    "Department_Region",
    "Status",
    "Performance_Score"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].str.title()

# ============================
# Convert Join_Date to datetime
# ============================

df["Join_Date"] = pd.to_datetime(
    df["Join_Date"],
    errors="coerce"
)

# ============================
# Handle missing values
# ============================

# Age
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

# Salary
if "Salary" in df.columns:
    df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Department
if "Department_Region" in df.columns:
    df["Department_Region"] = df["Department_Region"].fillna("Unknown")

# Performance Score
if "Performance_Score" in df.columns:
    df["Performance_Score"] = df["Performance_Score"].fillna("Not Available")

# ============================
# Remove rows with missing Employee ID
# ============================

df.dropna(subset=["Employee_ID"], inplace=True)

# ============================
# Clean Email
# ============================

if "Email" in df.columns:
    df["Email"] = df["Email"].str.lower()

# ============================
# Convert Phone to string
# ============================

if "Phone" in df.columns:
   df["Phone"] = df["Phone"].astype(str)

# ============================
# Remove impossible ages
# ============================

if "Age" in df.columns:
    df = df[(df["Age"] >= 18) & (df["Age"] <= 65)]
    # Convert Age to integer
    df["Age"] = df["Age"].astype(int)

    # Round Salary to 2 decimal places
    df["Salary"] = df["Salary"].round(2)

# ============================
# Remove negative salaries
# ============================

if "Salary" in df.columns:
    df = df[df["Salary"] >= 0]

# ============================
# Reset Index
# ============================

df.reset_index(drop=True, inplace=True)

# ============================
# Save Cleaned File
# ============================

df.to_csv("Employee_dataset_cleaned.csv", index=False)
print("\nCleaning Completed Successfully!")
print("Cleaned Shape:", df.shape)
print("\nCleaned file saved as:")
print("Employee_dataset_cleaned.csv")