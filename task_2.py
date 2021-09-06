import re
from datetime import datetime

date_start = None
output = -1
counter = 0

with open('data/input_task_2.txt', 'r') as f_in:
    for line_num, line in enumerate(f_in):
        if line_num == 0:
            _ = line.split()
            t, e = int(_[0]), int(_[1])
            continue
            
        date_orig = re.findall(r'\[(.+)\]', line)[0]
        date = datetime.strptime(date_orig, "%Y-%m-%d %H:%M:%S")
        
        if date_start is None:
            date_start = date

        is_error = line.find('] ERROR ') > -1
        if is_error:
            K = (date - date_start).seconds
            if K < t:
                counter += 1
            else:
                counter = 1
                date_start = date
        
        if counter >= e:
            output = date_orig
            break

with open('data/output_task_2.txt', 'w') as f_out:
    f_out.write(str(output))