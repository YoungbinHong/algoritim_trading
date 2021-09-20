import pandas_datareader.data as dr

snp500 = dr.YahooDailyReader(symbols='^GSPC', start='8/12/1982', end='9/14/2021')
print(snp500._read_lines('1.csv'))