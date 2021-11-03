import csv
import pandas


df = pandas.read_csv('text.csv')
print(df)

with open ('text.csv') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')
    line_count=0
    f= open("sqlfile.txt","a")
    for row in csv_reader:
        if line_count==0:
            f.write(f'INSERT INTO mytable({",".join(row)}) VALUES  \n')
            line_count+=1
        else:
            f.write(f'(\'{row[0]}\',\'{row[1]}\',\'{row[2]}\',\'{row[3]}\'),\n')
            line_count+=1
print
