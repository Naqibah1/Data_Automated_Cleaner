import csv
import pandas as pd
# bbox = {
#     "SELANGOR": {
#         "minlng": 100.8204699762929,
#         "maxlng": 101.86691768552187,
#         "minlat": 2.595688902360501,
#         "maxlat": 3.8790109805578754,
#     },
#     "KL": {
#         "minlat": 3,
#         "maxlat": 6,
#     }
# }

with open('sales-sample.csv', 'r', newline='') as csvfile:
    r = csv.reader(csvfile)
    next(r, None)  # skip the headers
    daerah = {}
    for row in r:
        # print(", ".join(row))
        addr = row[0].split("\n")
        if len(addr) > 2:
            d = addr[-2]
            # cleaning by trim d
            if d in daerah:
                daerah[d] = daerah[d] + 1
            else:
                daerah[d] = 1
        else:
            print("XXX", addr)

#
