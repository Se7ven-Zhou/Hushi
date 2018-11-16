# coding:utf-8

class Package_message:

    def __init__(self):

        pass

    def Get_ErrorMessage(self,result_code,right_code,result):
        error_info = "<AssertionError> " + result_code + "≠" + right_code + " <Response:\t" + result + ">"
        return error_info