table_1 = {}

# files = input().split()
files = ['data/market_2.csv', 'data/billing_2.csv']

with open(files[0], 'r') as tbl_1:
    with open(files[1], 'r') as tbl_2:
        with open('data/output_task_3.txt', 'w') as f_out:

            # order_id,shop_name,shop_id,cost
            f_out.write(f"order_id,shop_name,shop_id,cost\n")
            
            for line_num, line in enumerate(tbl_2):
                if line_num == 0:
                    continue
                
                # order_id,shop_id,cost
                data = line.rstrip().split(',')
                order_id, shop_id, cost = data[0], data[1], data[2]

                shop_id_, shop_name_ = None, None
                for line_num_, line_ in enumerate(tbl_1):
                    if line_num_ == 0:
                        continue

                    # shop_id,shop_name
                    data_ = line_.rstrip().split(',')
                    shop_id_, shop_name_ = data_[0], data_[1]
                    if shop_id == shop_id_:
                        break
                
                if shop_name_ is not None:
                    f_out.write(f"{order_id},{shop_name_},{shop_id},{cost}\n")
