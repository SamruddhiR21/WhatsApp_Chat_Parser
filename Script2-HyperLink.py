#To Create Hyperlink 
import pandas as pd
import os
import re
import numpy as np

#Reading excel output genereted using 1st script
df = pd.read_excel("G:\\Python\\My\\Axiom\\Whatapp\\output_excel.xlsx")

#Path of Export folder
folder_path = "C:\\Users\\S\\Downloads\\WhatsApp Chat"

#Hyperlink
def create_hyperlink(file_name):
    file_path = os.path.join(folder_path, file_name)
    hyperlink = f'=HYPERLINK("{file_path}", "{file_name}")'
    return hyperlink

#Looping to Iterate
for index, row in df.iterrows():
    message = row["Message"]
    if not pd.isnull(message) and "(file attached)" in message:
        #Extract file name
        file_match = re.search(r'([\w.-]+)\s\(file attached\)', message)
        if file_match:
            file_name = file_match.group(1)
            if os.path.isfile(os.path.join(folder_path, file_name)):
                #found in folder, create hyperlink
                df.at[index, "Message"] = create_hyperlink(file_name)

#Final Output
df.to_excel("Output_Final.xlsx", index=False)
