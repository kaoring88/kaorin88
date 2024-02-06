import openpyxl as excel

wb = excel.load_workbook('C:/Users/かおりん/Desktop/poker/card.xlsx')
ws = wb.worksheets[0]

ws.title = 'card'
wb.save("card.xlsx")
