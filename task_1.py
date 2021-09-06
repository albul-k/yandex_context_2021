import json

data = {}
data_output = []
temp_order_data = {}
last_event_id = {}

with open('data/input_task_1.json', 'r') as f_in:
    data = json.load(f_in)

    for order in data:
    
        if order['order_id'] not in last_event_id:
            last_event_id[order['order_id']] = order['event_id']
        elif order['event_id'] < last_event_id[order['order_id']]:
            continue

        last_event_id[order['order_id']] = order['event_id']

        total = order['count'] - order['return_count']
        if total < 0:
            total = 0
        
        if order['status'] == 'CANCEL' or total == 0:
            if order['order_id'] in temp_order_data:
                for idx, item in enumerate(temp_order_data[order['order_id']]['items']):
                    if item['id'] == order['item_id']:
                        temp_order_data[order['order_id']]['items'].pop(idx)
            continue

        if order['order_id'] not in temp_order_data:
            temp_order_data[order['order_id']] = {
                "id": order['order_id'],
                "items": []
            }

        temp_order_data[order['order_id']]['items'].insert(order['item_id'], {
            "id": order['item_id'],
            "count": total
        })
    
    for itm in temp_order_data.items():
        if len(itm[1]['items']):
            data_output.append(itm[1])

with open('data/output_task_1.json', 'w') as f_out:
    json.dump(data_output, f_out)