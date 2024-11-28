import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def analyze_data(df):
    print("DataFrame Head:")
    print(df.head())
    print("\nDataFrame Description:")
    print(df.describe())

if __name__ == "__main__":
    file_path = "your_file.csv"
    df = load_csv(file_path)
    analyze_data(df)
