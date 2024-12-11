import pandas as pd

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def analyze_data(df):
    print("DataFrame Head:")
    print(df.head())
    print("\nDataFrame Description:")
    print(df.describe())

if __name__ == "__main__":
    file_path = "your_file.csv"
    df = load_csv(file_path)
    if df is not None:
        analyze_data(df)
