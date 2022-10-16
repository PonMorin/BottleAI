import pandas as pd

excel_data_df = pd.read_excel('1.xlsx')
print(type(str(excel_data_df['User'][0])))
