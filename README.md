# Bulk-Transform---Delimited-SN-Range
Extract individual SN values from a range delimited by "-"

Excel transformation steps - 
1. Data -> text to columns. Separate with "," delimination between SN ranges.
2. Power Query, unpivot columns so there is 1 SN range (ex SN1-SN50) per row
3. Data -> text to columns. Separate into two columns the range with deliminator "-". This will give you beginning and ending SN.
4. 3rd column for diff in value. SN2-SN1 = range of SN.

Import file into google colab and run python script to extract all SN within the ranges into one column. Program tested with 500k+ SN values.
