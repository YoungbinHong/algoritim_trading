import openpyxl

f1 = openpyxl.load_workbook('snp500.xlsx')
f2 = openpyxl.load_workbook('nasdaq.xlsx')
s1 = f1.get_sheet_by_name('Sheet1')
s2 = f2.get_sheet_by_name('nasdaq')

snp = []
for cell in s1['C']:
    snp.append(cell.value)
snp = snp[1:]

nasdaq = []
for cell in s2['A']:
    nasdaq.append(cell.value)
nasdaq = nasdaq[1:]

count = 0
intersection = []
for element in nasdaq:
    if element in snp:
        count += 1
        intersection.append(element)

print(count)
print(intersection)
