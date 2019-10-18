"""
Page Visits Funnel

Cool T-Shirts Inc. has asked you to analyze data on visits to their website. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.

In this case, our funnel is going to describe the following process:

    A user visits CoolTShirts.com
    A user adds a t-shirt to their cart
    A user clicks “checkout”
    A user actually purchases a t-shirt

"""

data=visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')

print(all_data.head())

nulls2=len(all_data[all_data.checkout_time.notnull()&all_data.purchase_time.isnull()])
rows2=len(all_data[all_data.checkout_time.notnull()])

print((float(nulls2)/rows2)*100)

print('Visit time')
print((float(len(all_data[all_data.visit_time.isnull()]))/len(all_data)))*100

print('Cart time')
print((float(len(all_data[all_data.cart_time.isnull()]))/len(all_data)))*100

print('Checkout time')
print((float(len(all_data[all_data.checkout_time.isnull()]))/len(all_data)))*100

print('Purchase time')
print((float(len(all_data[all_data.purchase_time.isnull()]))/len(all_data)))*100

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase)


print(all_data.time_to_purchase.mean())

