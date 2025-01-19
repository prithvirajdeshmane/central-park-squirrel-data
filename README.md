# Central Park Squirrel Census Data Analysis

This Python program analyzes squirrel data from the **2018 Central Park Squirrel Census** dataset and generates a summary CSV file that counts squirrels based on their fur color. 

## Features
- Counts squirrels of different fur colors: **Gray**, **Cinnamon**, and **Black**.
- Outputs a new CSV file (`squirrel_count_by_color.csv`) containing the counts for each fur color.
- Uses the pandas library for efficient data manipulation and analysis.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/squirrel-census-analysis.git
   cd squirrel-census-analysis
2. **Install dependencies:** Ensure you have Python installed. Then install the required library:
    ```bash
    pip install pandas
3. **Add the dataset:** Place the 2018 Central Park Squirrel Census dataset in the same directory as the script. The dataset should be named
    `2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250106.csv`

## Usage
Run the script to generate the fur color counts and the CSV output:
    ```python squirrel_analysis.py```

## Expected Output
1. Counts of squirrels by fur color printed in the terminal
2. A new CSV file, squirrel_count_by_color.csv, with the following structure:
    ```csv
    Fur color,Count
    Gray,1234
    Cinnamon,678
    Black,456
    ```

## Example Terminal Output
```mathematica
Gray       1234
Cinnamon    678
Black       456
Name: Primary Fur Color, dtype: int64

   Unnamed: 0 Fur color  Count
0           0      Gray   1234
1           1  Cinnamon    678
2           2     Black    456
```
## Requirements
- Python 3.7 or later
- pandas library

## File Overview
- ```squirrel_analysis.py```: Main program script.
- ```2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250106.csv```: Dataset containing squirrel census data (not included in the repository).
- ```squirrel_count_by_color.csv```: Output file containing counts of squirrels by fur color.

## Dataset
The dataset is from the 2018 Central Park Squirrel Census and should be downloaded from [this](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data) source or provided manually.

## Affiliation
This program is part of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu and AppBrewery.
## License
This project is licensed under the [GNU General Public Use v3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).
