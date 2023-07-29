import pandas as pd

def find_player_data(stadium_name, player_name, dataset):
    filtered_data = dataset[
        (dataset['Stadium_Name'] == stadium_name) &
        (dataset['Player_Name'] == player_name) &
        (dataset.apply(lambda row: all(cell != 'NA' for cell in row), axis=1))
    ]
    return filtered_data

# Read the CSV file into a pandas DataFrame
dataset = pd.read_csv(r'c:\Users\twadd\OneDrive\Desktop\IBM PROJECT\project\Player vs Stadium Dataset.csv')

# Input values for stadium_name and player_name
input_stadium_name = input("Enter the stadium name: ")
input_player_name = input("Enter the player name: ")

# Finding and displaying the data
filtered_data = find_player_data(input_stadium_name, input_player_name, dataset)

if not filtered_data.empty:
    print("Player data for", input_player_name, "in", input_stadium_name)
    for _, row in filtered_data.iterrows():
        print("Stadium_Name:", row['Stadium_Name'])
        # print("Stadium_ID:", row['Stadium_ID'])
        print("Player_Name:", row['Player_Name'])
        # print("Player_ID:", row['Player_ID'])
        print("Role:", row['Role'])
        print("Country:", row['Country'])
        if not pd.isna(row['Highest_Runs']):
            print("Highest_Runs:", row['Highest_Runs'])
        if not pd.isna(row['Average_Runs']):
            print("Average_Runs:", row['Average_Runs'])
        if not pd.isna(row['Strike_Rate']):
            print("Strike_Rate:", row['Strike_Rate'])
        if not pd.isna(row['Total_Wickets']):
            print("Total_Wickets:", row['Total_Wickets'])
        if not pd.isna(row['Economy']):
            print("Economy:", row['Economy'])
        if not pd.isna(row['Dots']):
            print("Dots:", row['Dots'])
        
        print("-------------------------")
else:
    print("No data found for the given stadium and player.")
