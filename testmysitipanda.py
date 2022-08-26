# importing pandas package
import pandas as pd

df = pd.read_csv("forcleaning2.csv")
# assign dataset
csvData = pd.read_csv("forcleaning2.csv")

# sort data frame
csvData.sort_values(["CREDIT LIMIT"],
                    axis=0,
                    ascending=[True],
                    inplace=True)

# csvData.to_csv("forcleaning.csv", index=False)
# print(csvData)


def trim(csvData):
    def trim(x): return x.strip() if type(x) is str else x
    return csvData.applymap(trim)



# df = pd.csvData(
#     {"line4": [1, 2]},
# )
# df.rename({'JOHOR DARUL TAKZIM': 'KEDAH DARUL AMAN', 'JOHOR': 'KEDAH'})


# For printing negeri sahaja
# print(csvData['negeri'])

csvData.sort_values(['daerah', 'negeri'], ascending=True)

#print(csvData['negeri', 'daerah'])

# print(csvData)
csvData.to_csv("miniproject1.csv", index=False)

