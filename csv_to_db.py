import csv
import sqlite3

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = 'data/zip_code_database.csv'
# This will be the name of your SQLite database
db_name = 'data/zip_code_database.db'

def create_table_from_csv(cursor, csv_file_path, table_name):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        
        # Creating a table with column names based on CSV headers
        column_definitions = ', '.join([f"{header} TEXT" for header in headers])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})")
        
        # Inserting data into the table
        for row in reader:
            placeholders = ', '.join('?' * len(row))
            cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", row)

def add_entry_to_table(cursor, table_name, entry_data):
    placeholders = ', '.join('?' * len(entry_data))
    cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", entry_data)

# Main process
if __name__ == '__main__':
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    
    # Convert CSV to SQLite table
    create_table_from_csv(cur, csv_file_path, 'zip_codes')
    
    # Commit changes and close the connection
    conn.commit()
    
    # Example of adding a new row entry; modify 'entry_data' as per your table structure
    # entry_data = ('value1', 'value2', ...)  # Must match the structure of your CSV/table
    # add_entry_to_table(cur, 'my_table', entry_data)
    # conn.commit()
    
    conn.close()

    print("CSV data has been imported to the SQLite database.")
