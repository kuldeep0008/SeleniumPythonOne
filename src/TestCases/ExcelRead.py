import xlrd
class Excelread():
   
    def readExcelData(self):
        workbook = xlrd.open_workbook("C:/Users/kpanwar/Desktop/TestData.xlsx")
        sheet = workbook.sheet_by_name("Sheet1")

        rowcount = sheet.nrows #Get number of rows with data in excel sheet
        colcount = sheet.ncols #Get number of columns with data in each row. Returns highest number

        #print ("row Count", rowcount)
        #print ("col count", colcount)

        result_data =[]
        for curr_row in range(1, rowcount, 1):
            row_data = []

            for curr_col in range(0, colcount, 1):
                data = sheet.cell_value(curr_row, curr_col) # Read the data in the current cell
                #print ( "data", data)
                row_data.append( data )

            result_data.append(row_data)
            
        return result_data


# exlrd = Excelread()
# data1 = exlrd.readExcelData()
# for a in data1:
#     for b in range(len(a)):