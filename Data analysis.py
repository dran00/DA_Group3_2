import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('Visitors.xlsx')
Data = pd.DataFrame(data)
asiasData = Data.iloc[120:360, :16]
asiaData = Data.iloc[120:360, 1:16]
date=asiasData['   '].str.split(' ', n=2, expand=True)
asiaData.index=date[1]
AsiaData=asiaData.groupby(asiaData.index).sum(na=0)
AsiaData=AsiaData.replace(to_replace=r'na', value=0, regex=True)
overallData=AsiaData.sum()
overallData=overallData.sort_values(ascending=False)
china = asiaData[' Indonesia ']
chart1=AsiaData[[' Brunei Darussalam ',' Indonesia ',' Malaysia ',' Philippines ',' Thailand ',' Viet Nam ',
                ' Myanmar ',' Japan ',' Hong Kong ',' China ',' Taiwan ',' Korea, Republic Of ',' India ',' Pakistan ',
                ' Sri Lanka ']].plot(kind='bar',title="Overall",figsize=(10,10),legend=True,fontsize=12)
#chart2=AsiaData[[' Sri Lanka ']].plot(kind='bar',title="Sri Lanka data",figsize=(10,10),legend=True,fontsize=12)
#chart3=overallData.plot.bar(fontsize=5)
chart1.set_ylim(0,2000000)
#chart2.set_ylim(0,2000000)
plt.show()
print(overallData)
print(AsiaData)