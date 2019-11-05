import pandas as pd

df = pd.read_csv("Plaza Coffee.csv", sep=";")

name = {"Credit": "assistants", "Cash": "employees"}

for company, group in df.groupby("Company"):
    s = "From %s " % company
    
    for payment, subPaymentGroup in group.groupby("Payment"):
        s += "%d %s have bought " % (len(subPaymentGroup), name[payment])
        subDf = subPaymentGroup.groupby(["Order"])["Quantity"].sum().reset_index()
        
        for i in range(len(subDf)):
            order_type = subDf.loc[i]["Order"]
            quantity = subDf.loc[i]["Quantity"]
            s += " %d servings of %s, " % (quantity, order_type)
            
        s = s[:-2]
        s += " and paid in %s" % payment
        
        s += " and "
        
    s = s[:-5]
    s += "."
    
    print (s)
    print ()