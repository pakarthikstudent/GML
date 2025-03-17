import time
'''This is trading app'''
class vendor:
    '''vendor enrollment'''
    def __init__(self,vName,vGST):
        self.vName = vName
        self.vGST = vGST
        print(f'Vendor:{self.vName} registration is done!')
    def billing(self,pName,pCost=0.0,pQty=0):
        '''This is non-constructor - billing details'''
        self.pName = pName
        self.pCost = pCost
        self.pQty = pQty
        self.tax = 0.18
        self.total = self.pQty * self.pCost
        self.gs = self.total + self.tax
        s1=f'VendorName:{self.vName}\tVendorGST:{self.vGST}\tProductName:{self.pName}\t'
        s2=f'Cost:{self.pCost}\tTax:{self.tax}\tTotal:{self.total}\tGS:{self.gs}\t'
        s3=f'Billing date/time:{time.ctime()}\n'
        with open('billing_info.log','a') as wobj:
            wobj.write(s1+s2+s3+'\n')

