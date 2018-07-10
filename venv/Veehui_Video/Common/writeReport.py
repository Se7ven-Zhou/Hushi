# coding:utf-8

import os,time
from openpyxl import Workbook
from openpyxl import load_workbook
from Veehui_Video.Common.readData import Read_Data

class WriteReport:

    def __init__(self):

        self.address = self.address = os.path.split(os.path.dirname(__file__))[0] + "\TestDatas"
        self.report_name = "test_result.xlsx"
        self.report_path = os.path.join(self.address,self.report_name)

    def Write_Report(self,x,name,api,params,code,response,result = "False"):

        file = load_workbook(self.report_path)
        sheet = file.get_sheet_by_name("result")

        sheet.cell(row=x, column=1).value = name
        sheet.cell(row=x, column=2).value = api
        sheet.cell(row=x, column=3).value = params
        sheet.cell(row=x, column=4).value = code
        sheet.cell(row=x, column=5).value = response
        sheet.cell(row=x, column=6).value = result

        file.save(self.report_path)

if __name__ == "__main__":
    name = 11
    api = 22
    params =33
    code =44
    response =55
    WriteReport().Write_Report(name,api,params,code,response)
