# Matthew J Carr, Alison K Wright, Lalantha Leelarantha, Hood Thabit, Nicola Milne, Naresh Kanumilli, Darren M Ashcroft, Martin K Rutter, 2024.

import sys, csv, re

codes = [{"code":"3982440000000000.0","system":"gprdproduct"},{"code":"1.17814e+16","system":"gprdproduct"},{"code":"5997040000000000.0","system":"gprdproduct"},{"code":"3982340000000000.0","system":"gprdproduct"},{"code":"1.17813e+16","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('metformin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["metformin-solution---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["metformin-solution---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["metformin-solution---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
