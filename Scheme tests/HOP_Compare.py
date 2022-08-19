from datetime import date, datetime
from HOP_functions import *
import os
import difflib

print('-' * 120)
url = input('\n\033[1mPaste scheme website you want to test (you can paste link here by using right click):\n\033[0m')
scheme_name = input("\n\033[1mPlease enter scheme name: \n\033[0m")

print('-' * 120)
print("\n\033[1mFirst let's scrape the demo page!\033[0m\n")

# line below is recalling function that is written in HOP_functions file
scrape_demo()

print("\n\033[1mDemo page scraping script was executed successfully\n\033[0m")
print('-' * 120)

print(f"\n\033[1mNow lets scrape {scheme_name} page!\033[0m\n")

# line below is recalling function that is written in HOP_functions file
scrape_scheme(url, scheme_name)

print(f"\n\033[1m{scheme_name} page has been scraped!\033[0m\n")
print('-' * 120)
print("\n\033[1mNow let's compare the two!\033[0m\n")

# the code below is opening correct evidence file and loads it to the variable "scheme_wording"

with open(f"Scheme tests\Generated Evidence\HOP_{scheme_name}_Evidence.txt", encoding='utf8') as scheme_page_evidence:
    scheme_wording = scheme_page_evidence.read()

# code below is opening evidence file of demo website and loads it to the variable "demo_wording"

with open("Scheme tests\Generated Evidence\HOP_Corvidae_Evidence.txt", encoding='utf8') as demo_page_evidence:
    demo_wording = demo_page_evidence.read()

# here evidence file that will be generated from this script is prepared with date and time

filename = "Scheme tests\Demo vs Scheme - evidence\HOP_{scheme_name}_compared_to_demo.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

evidence_file_diff = open(f"Scheme tests\Demo vs Scheme - evidence\HOP_{scheme_name}_compared_to_demo.txt","w")
evidence_file_diff.close()
evidence_file_diff = open(f"Scheme tests\Demo vs Scheme - evidence\HOP_{scheme_name}_compared_to_demo.txt","a", encoding="utf-8")
now = datetime.now()
today = str(date.today())
current_time = now.strftime("%H:%M:%S")
evidence_file_diff.write(f"{today}\n{current_time}\n")
evidence_file_diff.close()

#below is the part where wording from both pages will be compared and saved into evidence file

evidence_file_diff = open(f"Scheme tests\Demo vs Scheme - evidence\HOP_{scheme_name}_compared_to_demo.txt","a", encoding="utf-8")
evidence_file_diff.write(f"Lines starting with - are from {scheme_name} scheme\nLines starting with + are from demo\n\n")
scheme_wording_list = scheme_wording.split("\n")
demo_wording_list = demo_wording.split("\n")
d = difflib.Differ()
diff = d.compare(scheme_wording_list, demo_wording_list)
evidence_file_diff.write('\n'.join(diff))
evidence_file_diff.close()

print("\n\033[1mEvidence file was successfully generated! You can find it in folder named 'Demo vs Scheme - evidence'\033[0m\n")
print('-' * 120)
