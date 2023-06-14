# DDoS report script
Script helping to automate imformation gathering about IPs from DDoS sources list

---
To use this script, you need to install some requirements:
```bash
pip install openpyxl
pip install pandas
pip install ipwhois
pip install requests
```
---

A script created to facilitate the creation of a summary of the set IP address list in .txt format.
Actions required to create a file supplied to the script as input:
1) Download the session report from PT SIEM or PT NAD;
2) Analyze the original .csv/.xlsx;
3) Select the list of source addresses, write them to the .txt file;
4) Save the file in a convenient location and copy its full name and path.

Before running the script, you need to make sure that all libraries are installed.
The pip package name and the libraries it installed under my venv:
- openpyxl (et-xmlfile-1.1.0 openpyxl-3.1.2);
- pandas (numpy-1.24.3 pandas-2.0.2 python-dateutil-2.8.2 pytz-2023.3 six-1.16.0 tzdata-2023.3);
- ipwhois (dnspython-2.0.0 ipwhois-1.2.0);
- requests (certifi-2023.5.7 charset-normalizer-3.1.0 idna-3.4 requests-2.31.0 urllib3-2.0.2);

After running the script, it enters the full path to the .txt file we used earlier.
After entering the file name, the script will output information about each IP address from the list to the console.
The result of the work: the assembly of two files (in case of use on my desktop):
- DDoS.csv (comma separated)
- DDoS.xlsx (Excel table with header)
