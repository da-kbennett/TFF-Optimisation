import os
import pandas as pd

def compare_columns(csv_file1, column1, csv_file2, column2):
    df1 = pd.read_csv(csv_file1)
    df2 = pd.read_csv(csv_file2)
    
    merged_df = df1.merge(df2, left_on=column1, right_on=column2)
    counter = len(merged_df)
    
    if counter > 0:
        # Get the column names of £m in csv_file2 and Position in csv_file2
        column_m = '£m' if '£m' in df2.columns else 'm'  # Handle potential encoding differences
        column_position = 'Position' if 'Position' in df2.columns else 'Position'  # Handle potential encoding differences

        # Update tff_value and sky_pos with the corresponding values from £m and Position columns in csv_file2
        for _, row in merged_df.iterrows():
            tff_id_value = row[column1]
            m_value = row[column_m]
            position_value = row[column_position]
            
            df1.loc[df1[column1] == tff_id_value, 'tff_value'] = m_value
            
            # Check if Position is equal to "STR" in csv_file2
            if position_value == "STR":
                df1.loc[df1[column1] == tff_id_value, 'sky_pos'] = "FOR"
            else:
                df1.loc[df1[column1] == tff_id_value, 'sky_pos'] = position_value
    
        # Save the updated DataFrame back to csv_file1
        df1.to_csv(csv_file1, index=False)
    
    return counter

if __name__ == "__main__":
    data_directory = r"C:\FF\TFF_Optimization-main\data"

    csv_file1 = os.path.join(data_directory, "prior_player_data.csv")
    column1 = "fpl_code"  # Use the correct header name for column L
    
    csv_file2 = os.path.join(data_directory, "TFF_players.csv")
    column2 = "ID"  # Use the correct header name for column B

    result = compare_columns(csv_file1, column1, csv_file2, column2)
    print(f"Number of matching values: {result}")