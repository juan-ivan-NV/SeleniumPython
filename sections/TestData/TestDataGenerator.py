import faker
import xlwt

data = faker.Faker()
wk = xlwt.Workbook()
ws = wk.add_sheet("Sheet1")

for i in range(0, 10000):
    ws.write(i,0, data.name())
    ws.write(i,1, data.address())
    ws.write(i,2, data.email())

wk.save("Result.xls")