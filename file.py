# with open("try.txt",'r') as File1:
#     file=File1.readlines()
#     for content in file:
#      print(content)
#     # for line in File1:
#     #     print(line)
#     # file=File1.read(2)
#     # print(file)
#     File1.close()
    
# with open("try.txt",'r') as file1:
#     with open("write.txt",'w') as file2:
#         for line in file1:
#             file2.write(line)
#             print(line)

''' loading data with pandas'''
import pandas
file="data.xlsx"
df=pandas.read_excel(file)
unique=df['Name'].unique()
print(unique)

