"""
Petal Power Inventory

You’re the lead data analyst for a chain of gardening stores called Petal Power. Help them analyze their inventory!
"""

import codecademylib
import pandas as pd

inventory=pd.read_csv('inventory.csv')
inventory.head(10)
staten_island=inventory[inventory.location=='Staten Island']

product_request=staten_island['product_description']

seed_request=inventory[(inventory.location=='Brooklyn')&(inventory.product_type=='seed_request')]

mylambda = lambda x: True \
	if x >0 \
  else False
inventory['in_stock']=inventory.quantity.apply(mylambda)
inventory['total_value']=inventory.price*inventory.quantity

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description']=inventory.apply(combine_lambda, axis = 1)
