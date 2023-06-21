import csv

# Define the input and output file paths
input_file = "forParsing_task.xls"
output_file = "basic_cleaned_example.csv"

# Read the input file
with open(input_file, "r") as file:
    reader = csv.reader(file, delimiter="\t")
    rows = list(reader)

# Clean the data
cleaned_rows = []
headers = []

for row in rows:
    if row and "|" in row[0] and "--------" not in row[0]:
        values = [value.strip() for value in row[0].split("|")][1:-1]

        # Check if the row contains the headers
        if "Stat" in values:
            if not headers:
                headers = values
        else:
            # Clean the LC amnt column by removing commas and handling negative values
            float_value = values[5].replace(',', '')
            if values[5].endswith("-"):
                float_value = "-" + float_value.strip()[:-1]
            values[5] = float(float_value)

            # Append the cleaned row to the list
            cleaned_rows.append(values)

# Write the cleaned data to the output file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(cleaned_rows)

# Print a message indicating the completion of data cleaning
print("Data cleaning completed. The cleaned data is saved in", output_file)
