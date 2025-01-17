#!/usr/bin/env python

"""Tests for `xls2xlsx` feature of ignoring workbook corruption error"""
"""This feature are depended on xlrd(>=2.0.0)"""
"""Highly recommend setting `ignore_workbook_corruption=True` """
from xls2xlsx import XLS2XLSX

# By using of `XLS2XLSX` default set of `ignore_workbook_corruption`
# It will try to replace the old XLS2XLSX object by a new that are set `ignore_workbook_corruption=True`
# if raise `xlrd.compdoc.CompDocError: Workbook corruption: seen[2] == 4`
def test_ignore_workbook_corruption():
    bad_file_path = 'inputs/workbook_corruption.xls'
    excel = XLS2XLSX(f=bad_file_path)
    excel.to_xlsx('outputs/workbook_corruption.xlsx')


# Manually set `ignore_workbook_corruption=True`
# It will ignore `xlrd.compdoc.CompDocError: Workbook corruption: seen[2] == 4` if raise
def test_ignore_workbook_corruption_with_set():
    bad_file_path = 'inputs/workbook_corruption.xls'
    excel = XLS2XLSX(f=bad_file_path,ignore_workbook_corruption=True)
    excel.to_xlsx('outputs/workbook_corruption_manualy.xlsx')