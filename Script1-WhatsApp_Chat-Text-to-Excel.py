import re
import pandas as pd

#Regex patterns for extracting timestamp, sender, and message
#pattern = r'(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - (\w+): (.*)'
pattern = r'^(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - ([^:]+): (.*)$'

#Reading chat file
data = []
#Path to whatsapp txt file
with open("C:\\Users\\S\\Downloads\\WhatsApp Chat\\WhatsApp Chat.txt", 'r', encoding='utf-8') as file: 
    for line in file:
        match = re.match(pattern, line)
        if match:
            timestamp, sender, message = match.groups()
            data.append({'Timestamp': timestamp, 'Sender': sender, 'Message': message})

#Creating DataFrame
df = pd.DataFrame(data)

#Output to Excel file
df.to_excel("output_excel.xlsx", index=False)
