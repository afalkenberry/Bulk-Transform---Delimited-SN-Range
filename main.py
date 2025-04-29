import os
import pandas as pd

from google.colab import files
uploaded = files.upload()

os.listdir()

def generate_sn_range(sn_pairs):
    all_sns = []

    for sn1, sn2 in sn_pairs:
        try:
            sn1_str = str(sn1)
            sn2_str = str(sn2)
            sn1_suffix = int(sn1_str[-6:])
            sn2_suffix = int(sn2_str[-6:])
            sn_prefix = sn1_str[:-6]
            
            sn_range = [sn_prefix + str(num).zfill(6) for num in range(sn1_suffix, sn2_suffix + 1)]
        except ValueError:
            # Except skip the pair
            print(f"Non-numeric SN pair skipped: {sn1}, {sn2}")
            continue
        
        all_sns.extend(sn_range)

    return all_sns

# Store excel in dataframe
df = pd.read_excel('CN list2.xlsx')

# Convert to list
sn_pairs = list(zip(df['SN1'], df['SN2']))

sn_pairs = list(zip(df['SN1'], df['SN2']))

# Generate all SNs using function
all_sns = generate_sn_range(sn_pairs)

sn_df = pd.DataFrame(all_sns, columns=['Serial Number'])

# Export the dataframe to an excel file
output_file = os.path.join('INFO_Extracted_Serial_Numbers.xlsx')

sn_df.to_excel(output_file, index=False)

print(f"Serial numbers have been exported to {output_file}")

# Download exported excel file
from google.colab import files
files.download('INFO_Extracted_Serial_Numbers.xlsx')
