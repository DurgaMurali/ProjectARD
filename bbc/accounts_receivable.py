class AccountsReceivable:
   def __init__(self, insured_ar: any, uninsured_ar: any, insured_ar_90_days : any, uninsured_ar_90_days: any) -> None:
        self.insured_ar = insured_ar
        self.uninsured_ar = uninsured_ar
        self.insured_ar_90_days = insured_ar_90_days
        self.uninsured_ar_90_days = uninsured_ar_90_days


class MarginableAR:
    def __init__(self, marginable_AR_90_percent: any, priority_payables: any, Marginable_AR : any, AR_Contra: any, AR_Related_Party: any) -> None:
        self.marginable_AR_90_percent = marginable_AR_90_percent
        self.priority_payables = priority_payables
        self.Marginable_AR = Marginable_AR
        self.AR_Contra = AR_Contra
        self.AR_Related_Party = AR_Related_Party