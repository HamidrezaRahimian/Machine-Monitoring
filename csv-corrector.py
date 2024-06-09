import csv

input_file = 'machines_data.csv'
output_file = 'machines_data_corrected.csv'

with open(input_file, mode='r', newline='', encoding='utf-8-sig') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header
    header = next(reader)
    writer.writerow(header)

    header_length = len(header)

    for i, row in enumerate(reader, start=2):
        if len(row) != header_length:
            print(f"Error in line {i}: {row} - Adjusting to match header length")
            while len(row) < header_length:
                row.append('')  # Add empty fields to match header length
            while len(row) > header_length:
                row.pop()  # Remove extra fields to match header length

        writer.writerow(row)

print(f"Corrected CSV saved to {output_file}")
