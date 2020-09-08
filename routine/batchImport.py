# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 10:46 上午
# @Author  : Ian Leto
# @File    : batchImport.py
# 干啥的    : 批量处理 CMDB
import xlwt
import xlrd
import xlsxwriter


def write_excel():
    # workbook = xlsxwriter.Workbook('/Users/ian/Documents/transferQueryTest.xlsx')
    workbook = xlsxwriter.Workbook('/Users/ian/Documents/bk_cmdb_import_host.xlsx')
    sheet = workbook.add_worksheet('批量导入')
    ip = '20.0.0.0'
    os_type = 1
    port = 1
    sheet.write(3, 0, '20.1.0.1')
    workbook.close()


def read_excel():
    workbook = xlrd.open_workbook('/Users/ian/Documents/bk_nodeman_info.xlsx')

    # 我们只处理一个sheet
    sheet = workbook.sheets()[0]
    print("一共", sheet.nrows, "行")
    print("一共", sheet.ncols, "列")


if __name__ == '__main__':
    # read_excel()
    write_excel()
