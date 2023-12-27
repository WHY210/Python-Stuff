import pandas as pd


def check(from_file, to_file):
    column_name_list = []
    company_name_list = []

    # load data
    # from_df = pd.read_excel(from_file)
    # to_df = pd.read_excel(to_file)
    from_df = pd.read_csv(from_file, encoding="utf-8")
    to_df = pd.read_csv(to_file, encoding="utf-8")

    # collect column names
    from_df_column_name = from_df.columns.tolist()
    to_df_column_name = to_df.columns.tolist()

    for item in from_df_column_name:
        if item not in to_df_column_name:
            print(f"{from_file} 這邊的欄位 在 {to_file} 中未找到匹配列名: {item}")

    for item in to_df_column_name:
        if item not in from_df_column_name:
            print(f"{to_file} 這邊的欄位 在 {from_file} 中未找到匹配列名: {item}")

    # check every companies
    for company_name in from_df["輔助"]:
        if pd.notna(company_name):
            i = 0
            try:
                from_row_index = from_df[from_df["輔助"] == company_name].index[0]
                to_row_index = to_df[to_df["輔助"] == company_name].index[0]
            except IndexError:
                print(f"{from_file} 貼到 {to_file} 這邊在其中一個檔案未找到匹配公司: {company_name}")
                continue

            for column_name in to_df_column_name:
                try:
                    from_data = from_df.iloc[
                        from_row_index, from_df.columns.get_loc(column_name)
                    ]
                    to_data = to_df.iloc[
                        to_row_index, to_df.columns.get_loc(column_name)
                    ]
                except KeyError:
                    # print(f"{to_file} 的  {company_name} 這邊的欄位 在 {from_file} 中未找到匹配列名: {column_name}")
                    continue

                # data preprocessing - start with "0" (delete 0 part)
                from_data_new = from_data
                to_data_new = to_data
                from_data_new = str(from_data_new).lstrip("0")
                to_data_new = str(to_data_new).lstrip("0")
                # data preprocessing - end with".0" (delete .0 part)
                if str(from_data_new).endswith(".0"):
                    from_data_new = str(from_data_new)[:-2]
                if str(to_data_new).endswith(".0"):
                    to_data_new = str(to_data_new)[:-2]

                # start checking
                if from_data_new == to_data_new:
                    # print(company_name,column_name,"：",from_data,"跟",to_data,"一樣")
                    continue
                else:
                    # if pd.isna(from_data_new) and pd.isna(to_data_new):
                    if pd.isna(from_data_new) or from_data_new == "nan":
                        continue
                    elif pd.isna(to_data_new) or to_data_new == "nan":
                        continue
                    elif column_name == "age":
                        continue
                    elif column_name == "Data Date":
                        continue
                    else:
                        i = 1
                        if column_name not in column_name_list:
                            column_name_list.append(column_name)
                        # print(
                        #    f"\n出事Jenny！！！{from_file} 貼到 {to_file} 的 {company_name} 的 {column_name} 這邊 {from_data} 跟 {to_data} 不一樣"
                        # )

            for column_name in from_df_column_name:
                try:
                    from_data = from_df.iloc[
                        from_row_index, from_df.columns.get_loc(column_name)
                    ]
                    to_data = to_df.iloc[
                        to_row_index, to_df.columns.get_loc(column_name)
                    ]
                except KeyError:
                    # print(f"{from_file} 的 {company_name} 這邊的欄位 在 {to_file} 中未找到匹配列名: {column_name}")
                    continue

                # data preprocessing - start with "0" (delete 0 part)
                from_data_new = from_data
                to_data_new = to_data
                from_data_new = str(from_data_new).lstrip("0")
                to_data_new = str(to_data_new).lstrip("0")
                # data preprocessing - end with".0" (delete .0 part)
                if str(from_data_new).endswith(".0"):
                    from_data_new = str(from_data_new)[:-2]
                if str(to_data_new).endswith(".0"):
                    to_data_new = str(to_data_new)[:-2]

                # start checking
                if from_data_new == to_data_new:
                    # print(company_name,column_name,"：",from_data,"跟",to_data,"一樣")
                    continue
                else:
                    # if pd.isna(from_data_new) and pd.isna(to_data_new):
                    if pd.isna(from_data_new) or from_data_new == "nan":
                        continue
                    elif pd.isna(to_data_new) or to_data_new == "nan":
                        continue
                    elif column_name == "age":
                        continue
                    elif column_name == "Data Date":
                        continue
                    else:
                        i = 1
                        if column_name not in column_name_list:
                            column_name_list.append(column_name)
                        if company_name not in company_name_list:
                            company_name_list.append(company_name)
                        # print(
                        #    f"\n出事Jenny！！！{from_file} 貼到 {to_file} 的 {company_name} 的 {column_name} 這邊 {from_data} 跟 {to_data} 不一樣"
                        # )
            # if i == 1:
            #    print(f"\n出事Jenny！！！{from_file} 貼到 {to_file} 的 {company_name} 出事")

    if i == 0:
        print("\n\n", from_file, "貼到", to_file, "檢查完成啦Jenny\n\n")
    else:
        print(
            f"\n\n{from_file}貼到{to_file}檢查完成啦Jenny\n出事啦\n以下company出事{company_name_list}\n以下column出事：\n{column_name_list}",
        )


check(
    "\\Jenny\\管科\\IT_by sample mean.csv",
    "\\Jenny\\管科\\raw_data_2004-2022(12.17)_IT_replace_by_sample_mean_done.csv",
)

"""
check("IT_前後除2.csv", "raw_data_2004-2022(12.17)_IT_divide by 2_done.csv")

check(
    "IT_by focal mean.csv",
    "raw_data_2004-2022(12.17)_IT_replace by focal firm means_done.csv",
)
"""
