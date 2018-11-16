# coding:utf-8

from openpyxl import load_workbook
from openpyxl import Workbook
from urllib import request
from prettytable import PrettyTable

file = load_workbook("C:/Users/Administrator/PycharmProjects/pythonStudy/venv/HuShi/Reports/2018-10-24.xlsx")
sheet = file.get_sheet_by_name("result")

data_list =[]
for i in range(2,sheet.max_column+1):
        data1=[]
        data_dict = {}
        data_dict["1"] = sheet.cell(row=2,column=item).value

    for j in range(2,sheet.max_column+1):



print(data_list)


# data["1"] = sheet.cell(row=item, column=1).value

# text = ""
# # for i in range(0,len(data_list)):
# for i in range(0,len(data_list)):
#     text += "\n"
#     for j in data_list[0].keys():
#         text += str(data_list[i][j]) + "\t\t\t\t"
# print(text)

list1 = ["小明",200, 199, 198]
list2 = ["大明白",197, 196, 195]
#
# x = PrettyTable(["名字", "数学成绩", "语文成绩", "计算机成绩"])
# x.add_row(list1)
# x.add_row(list2)
# print(x)

