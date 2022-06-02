# Copyright (c) 2022, rangsutra_app and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    price_list = frappe.db.sql_list("select price_list_name from `tabPrice List`")

    i=0
    price_dict = {}
    for pp in price_list:
        price_dict.update({'price' + str(i):pp})
        i+=1

    columns = get_columns(price_dict)
    data = get_data(filters, price_dict)

    return columns, data

def get_columns(price_list):
    columns = [
        _("Item Name") + ":Link.Item:200",
    ]

    for k,v in price_list.items():
        print(k,v)
        columns.append ({
            "label": _(v), "fieldname": k, "width": 160
        })

    return columns

def get_data(filters, price_list):

    item_query = f"""select distinct(item_name) as name, item_code as code from `tabItem Price`"""
    item_data=frappe.db.sql(item_query, as_dict=True)

    data = []

    for items in item_data:
        op = f"""select distinct(ip.item_code) as name, ip.price_list_rate as rate, pl.price_list_name as pname, ip.item_name as iname from `tabItem Price` ip 
                inner join `tabPrice List` as pl on ip.price_list = pl.price_list_name where ip.item_code = "{items.code}" order by ip.item_code desc"""
        price_data=frappe.db.sql(op, as_dict=True)

        dictt = {'item_name': items.name}
        for k,v in price_list.items():
            for each in price_data:
                if each.pname == v:
                    dictt.update({k: each.rate})

        data.append(dictt)

    return data

