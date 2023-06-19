import pandas

skip_cols = [0]
keep_cols = [i for i in range(8) if i not in skip_cols]
file_AR = pandas.read_excel('Sample_File_1.xlsx', sheet_name='AR', skiprows=[0,1], nrows=13, usecols=keep_cols)
AR_Total = file_AR['Balance'].sum()
AR_Greater_Than_90_Days = file_AR['> 90 day'].sum()

# Any calculation?
AR_Insured = 0
AR_Contra = 0
AR_Related_Party = 0

file_AP = pandas.read_excel('Sample_File_1.xlsx', sheet_name='AP', skiprows=[0])
AP_30_60_table = file_AP['30-60'].where(file_AP['Name'] == "Government")
AP_60_90_table = file_AP['60-90'].where(file_AP['Name'] == "Government")
AP_GreaterThan_90_table = file_AP['> 90 day'].where(file_AP['Name'] == "Government")

AP_30_60_table.fillna(0)
AP_60_90_table.fillna(0)
AP_GreaterThan_90_table.fillna(0)
Priority_Payables = AP_30_60_table.sum() + AP_60_90_table.sum() + AP_GreaterThan_90_table.sum()

Marginable_AR = AR_Total - AR_Greater_Than_90_Days - AR_Contra - AR_Related_Party - Priority_Payables
Marinable_AR_90_percent = Marginable_AR*0.9

print("Account Receivable Total = ", AR_Total)
print("AR > 90 days = ", AR_Greater_Than_90_Days)
print("Contra AR = ", AR_Contra)
print("Related party AR = ", AR_Related_Party)
print("Priority Payables = ", Priority_Payables)
print("Marginable AR = ", Marginable_AR)
print("90% of Marginable AR = ", Marinable_AR_90_percent)
