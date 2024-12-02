import  pandas as pd
import  pandas

abc = pd.read_csv(r"C:\\Users\\SanjeevaKumarGeejula\\Downloads\\2024_11_04_194436.csv")
# print(str(abc))
# print(abc.to_string())

xyz = pd.read_excel(r'Preparation\\practice\\SeleniumNOV1\\pandas\\42DOTCost.xlsx')
# print(str(xyz))

dataset = {'cars':["BMW","Volvo","maruthy"], 'passings':[3,7,10]}
var = pandas.DataFrame(dataset)
print(var)