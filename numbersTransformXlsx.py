# 文档链接：https://products.aspose.com/cells/zh/python-java/conversion/numbers-to-xlsx/
numbers_file = "./numFile/Rester.numbers"
xlsx_file = "./xlsx/Register1.xlsx"

import  jpype
import  asposecells
jpype.startJVM()
from asposecells.api import Workbook
workbook = Workbook(numbers_file)
workbook.save(xlsx_file)
jpype.shutdownJVM()