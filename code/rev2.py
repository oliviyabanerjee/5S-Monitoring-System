import os
import pandas as pd
import re


def check_folders(list_folders_files):
    list_folders = [_ for _ in list_folders_files if '.' not in _]
    if len(list_folders) > 0:
        return (True, list_folders)
    else:
        return (False, None)


if __name__ == '__main__':
    df = pd.DataFrame(columns=['year', 'zone', 'folder', 'sub_folder', 'sub_sub_folder', 'count_files'])
    main_path = r'C:\\Users\\BanerjeeA\\OneDrive - thyssenkrupp\\Desktop\\Projects\\5SImplementation\\5S'
    year_folder_list = os.listdir(main_path)
    for year_folder in year_folder_list:
        zone_path = main_path + '\\' + year_folder
        zone_folder_list = os.listdir(zone_path)
        for zone_folder in zone_folder_list:
            folder_path = zone_path + '\\' + zone_folder
            folder_list = os.listdir(folder_path)
            # print(folder_list)
            for folder in folder_list:
                sub_folder_path = folder_path + '\\' + folder
                sub_folder_list = os.listdir(sub_folder_path)
                # print(check_folders(sub_folder_list))
                if check_folders(sub_folder_list)[0] == True:
                    for sub_folder in check_folders(sub_folder_list)[1]:
                        sub_sub_folder_path = sub_folder_path + '\\' + sub_folder
                        sub_sub_folder_list = os.listdir(sub_sub_folder_path)
                        if check_folders(sub_sub_folder_list)[0] == True:
                            for sub_sub_folder in check_folders(sub_sub_folder_list)[1]:
                                sub_sub_sub_folder_path = sub_sub_folder_path + '\\' + sub_sub_folder
                                sub_sub_sub_folder_list = os.listdir(sub_sub_sub_folder_path)
                                count_files = len(sub_sub_sub_folder_list)
                                var = sub_sub_sub_folder_path.split('\\')
                                l = [var[-5], var[-4], var[-3], var[-2], var[-1], count_files]
                                df.loc[len(df)] = l
                                # print(sub_sub_sub_folder_path)
                        else:
                            count_files = len(sub_sub_folder_list)
                            var = sub_sub_folder_path.split('\\')
                            l = [var[-4], var[-3], var[-2], var[-1], None, count_files]
                            df.loc[len(df)] = l

                            # print(var)
                            # print(sub_sub_folder_path)
                else:
                    count_files = len(sub_folder_list)
                    var = sub_folder_path.split('\\')
                    l = [var[-3], var[-2], var[-1], None, None, count_files]
                    df.loc[len(df)] = l
                    # print(var[-1], var[-2], var[-3])
                    # print(sub_folder_path)
    df.to_excel('test1.xlsx')
