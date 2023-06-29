import pandas

from bbc.accounts_receivable import AccountsReceivable, MarginableAR

def read_accounts_receivable(file_name) -> AccountsReceivable:
    # Read insured AR
    file_AR = pandas.read_excel(file_name, sheet_name="Insured AR", skiprows=[0, 1])
    insured_ar_total = file_AR["Balance"].sum()
    AR_Greater_Than_90_Days = file_AR["> 90 day"].sum()

    # Read uninsured AR
    file_uninsured_AR = pandas.read_excel(
        file_name, sheet_name="Uninsured AR", skiprows=[0, 1]
    )
    uninsured_ar_total = file_uninsured_AR["Balance"].sum()
    uninsured_ar_Greater_Than_90_Days = file_uninsured_AR["> 90 day"].sum()

    print("Insured Account Receivable Total = ", insured_ar_total)
    print("Insured AR > 90 days = ", AR_Greater_Than_90_Days)

    print("Uninsured Account Receivable Total = ", uninsured_ar_total)
    print("Uninsured AR > 90 days = ", uninsured_ar_Greater_Than_90_Days)

    return AccountsReceivable(
        insured_ar=insured_ar_total,
        insured_ar_90_days=AR_Greater_Than_90_Days,
        uninsured_ar=uninsured_ar_total,
        uninsured_ar_90_days=uninsured_ar_Greater_Than_90_Days,
    )


# Any calculation?
AR_Insured = 0
AR_Contra = 0
AR_Related_Party = 0


def read_acounts_payabale(file_name) -> int:
    file_AP = pandas.read_excel(file_name, sheet_name="AP", skiprows=[0])
    AP_30_60_table = file_AP["30-60"].where(file_AP["Name"] == "Government")
    AP_60_90_table = file_AP["60-90"].where(file_AP["Name"] == "Government")
    AP_GreaterThan_90_table = file_AP["> 90 day"].where(file_AP["Name"] == "Government")

    AP_30_60_table.fillna(0)
    AP_60_90_table.fillna(0)
    AP_GreaterThan_90_table.fillna(0)
    Priority_Payables = (
        AP_30_60_table.sum() + AP_60_90_table.sum() + AP_GreaterThan_90_table.sum()
    )
    return Priority_Payables


def calculate_marginable_ar(Ar, Priority_Payables) -> MarginableAR:
    Marginable_AR = (
        Ar.insured_ar
        - Ar.insured_ar_90_days
        - AR_Contra
        - AR_Related_Party
        - Priority_Payables
    )
    Marginable_AR_90_percent = Marginable_AR * 0.9
    print("Priority Payables = ", Priority_Payables)
    print("Marginable AR = ", Marginable_AR)
    print("90% of Marginable AR = ", Marginable_AR_90_percent)
    print("Contra AR = ", AR_Contra)
    print("Related party AR = ", AR_Related_Party)
    return MarginableAR(marginable_AR_90_percent=Marginable_AR_90_percent, priority_payables=Priority_Payables,Marginable_AR=Marginable_AR,
                        AR_Contra=AR_Contra,AR_Related_Party=AR_Related_Party)


def main():
    file_name = "Sample_File_1.xlsx"
    ar = read_accounts_receivable(file_name=file_name)
    Priority_Payables = read_acounts_payabale(file_name=file_name)
    calculate_marginable_ar(Ar=ar, Priority_Payables=Priority_Payables)


# if __name__ == "__main__":
#     main()
