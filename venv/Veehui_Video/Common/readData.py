# coding:utf-8

import os
from openpyxl import load_workbook
from openpyxl import Workbook
from HuShi.Common.logger import Logging


class Read_Data:

    def __init__(self,filename,address = os.path.split(os.path.dirname(__file__))[0]+"\TestDatas"):

        self.address = address
        self.filename = filename

        self.path = os.path.join(self.address, self.filename)
        try:
            self.file = load_workbook(self.path)
        except Exception as error:
            Logging().Error(error)
            raise error

        self.sheet = self.file.get_sheet_by_name("meeting_info")

    def Get_Params(self):

        params_list = []
        for item in range(2,self.sheet.max_row + 1):
            params = self.sheet.cell(row = item, column = 2).value
            params_list.append(params)
        self.file.close()
        return params_list

    def Get_API(self):

        api_list = []
        for item in range(2,self.sheet.max_row + 1):
            api = self.sheet.cell(row = item,column = 1).value
            api_list.append(api)
        self.file.close()
        return api_list

    def Get_Code(self):

        code_list = []
        for item in range(2,self.sheet.max_row + 1):
            code = self.sheet.cell(row = item,column = 3).value
            code_list.append(code)
            self.file.close()
        return code_list

    def Get_name(self):

        name_list = []
        for item in range(2,self.sheet.max_row + 1):
            name = self.sheet.cell(row = item,column = 4).value
            name_list.append(name)
            self.file.close()
        return name_list

    def Get_MaxRow(self):

        MaxRow = self.sheet.max_row

        return MaxRow

if __name__ == "__main__":

    xx = Read_Data("test_data.xlsx").Get_Params()
    yy = Read_Data("test_data.xlsx").Get_API()
    zz = Read_Data("test_data.xlsx").Get_Code()
    tt = Read_Data("test_data.xlsx").Get_MaxRow()
    print(xx,yy,zz,tt)


