# Project Title

This project demonstrates how to load a CSV file using the pandas library and perform basic data analysis.

## Loading a CSV file with pandas

To load a CSV file using pandas, you need to install the pandas library first. You can install it using pip:

```bash
pip install pandas
```

Once you have pandas installed, you can use the following code to load a CSV file:

```python
import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df
```

## Example of loading a CSV file and performing basic analysis

Here is an example of how to load a CSV file and perform basic analysis using pandas:

```python
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
```
