# import s
# import getpathinfo  # 自己定义的内部类，该类返回项目的绝对路径
# # 调用读Excel的第三方库xlrd
# from xlrd import open_workbook
#
# # 拿到该项目所在的绝对路径
# path = getpathinfo.get_Path()
#
# class readExcel():
#     def get_xls(self, xlsx_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
#         cls = []
#         # 获取用例文件路径
#         xlsPath = os.path.join(path,'testCase',xlsx_name)
#         file = open_workbook(xlsPath)  # 打开用例Excel
#         sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
#         # 获取这个sheet内容行数
#         nrows = sheet.nrows
#         for i in range(nrows):  # 根据行数做循环
#             if sheet.row_values(i)[0] != u'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
#                 cls.append(sheet.row_values(i))
#         return cls
#
#
# if __name__ == '__main__':  # 我们执行该文件测试一下是否可以正确获取Excel中的值
#     print(readExcel().get_xls('login.xlsx', 'Sheet1'))
#     print(readExcel().get_xls('login.xlsx', 'Sheet1')[0][1])
#     print(readExcel().get_xls('login.xlsx', 'Sheet1')[1][2])

import json
import requests
# data = {"phone":18701890657,
#         "smsCode":"171204",
#         "channel":"IPAD"
#         }
# print(type(data))
# json1=json.dumps(data)
# pprint.pprint(json1)
'''
print("git add xxx  # 添加文件到仓库" )
print("git status  # 查看提交状态" )
print("git commit -m 'mesage ' # 提交状态以及提交记录message" )
git log 查看Git日志
git diff XXX  查看修改记录
git reset --hard HEAD^ 回退上一个版本
git reset --hard XXX  commi id 重新将HEAD指针指到XXX的版本
git reflog 查看命令历史
'''
