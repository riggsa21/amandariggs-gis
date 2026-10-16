from pathlib import Path
from datetime import date,timedelta
from random import Random
import csv
folder = Path(__file__).resolve().parent
r = Random(13)
people=['Cedar Bay Supply','Northline Studio','Maple Creek Goods','Bluewater Retail','Pine Hill Services','Riverbend Outfitters']
rows=[]
for i in range(1,41):
    d=date(2026,10,1)+timedelta(days=(i%15))
    ds=[d.strftime('%m/%d/%Y'),d.strftime('%Y-%m-%d'),d.strftime('%m-%d-%Y'),d.strftime('%b %d, %Y')][i%4]
    amount=round(r.uniform(29.5,489.3),2)
    amount_fmt=[f'${amount:,.2f}',f'{amount:.2f}',f' $ {amount:.2f} ',f'${amount:.2f}'][i%4]
    rows.append({'Order ID':f'ORD-{1000+i}', 'Order Date':ds,'Customer':people[i%len(people)], 'Amount':amount_fmt,'Status':['paid','PAID',' Paid ','complete'][i%4]})
# Intentionally imperfect sample data. No real customer records.
for k in [3,8,16,24,32]:
    rows.append(rows[k].copy())
for i in range(3):
    rows.append({'Order ID':f'ORD-{4000+i}','Order Date':'not a date' if i==0 else '10/15/2026','Customer':'Demo Customer','Amount':'N/A' if i==1 else '$80.00','Status':'paid'})
with (folder/'incoming_orders.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['Order ID','Order Date','Customer','Amount','Status']);w.writeheader();w.writerows(rows)
print(f'Created demo input: {len(rows)} fictional orders.')
