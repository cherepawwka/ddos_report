import os.path
import requests
from ipwhois import IPWhois
import csv
import pandas as pd
import ipaddress


def location(ip: str):
    response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
    if response.status_code == 404:
        print("Oops")

    ipapi_result = response.json()
    obj = IPWhois(ip)
    whois_result = obj.lookup_whois()
    subnet_cidr = whois_result["nets"][0]["cidr"]
    result_cidr = ""
    if "," in subnet_cidr:
        subnet_cidrs_array = subnet_cidr.split(",")
        addr4 = ipaddress.ip_address(ip)
        for subnet in subnet_cidrs_array:
            net4 = ipaddress.ip_network(subnet.strip())
            if addr4 in net4:
                result_cidr = net4
    # print(result_cidr)
    print("IP-адрес: " + ipapi_result["query"])
    print("Автономная сеть: " + ipapi_result["as"] + "; " + whois_result["asn_cidr"])
    print("Код страны и расшифровка: " + ipapi_result["countryCode"] + "; " + ipapi_result["country"])
    print("Подсеть: " + whois_result["nets"][0]["cidr"] + "; " + whois_result["nets"][0]["range"])

    # ipapi_result["query"] + "," + ipapi_result["as"] + "," + whois_result["asn_cidr"] + "," + ipapi_result[
    #     "countryCode"] + "," + ipapi_result["country"] + "," + whois_result["nets"][0]["cidr"] + "," + \
    # whois_result["nets"][0]["range"]
    result_string = ipapi_result["query"] + "," + ipapi_result["as"] + "," + whois_result["asn_cidr"] + "," + \
                    ipapi_result["countryCode"] + "," + ipapi_result["country"] + "," + str(result_cidr) + "," + \
                    whois_result["nets"][0]["range"]
    print(result_string)
    return result_string


if __name__ == '__main__':
    print("Введите полный путь к файлу в формате .txt: ")
    path_to_file = input()
    print(f"Выбран файл: " + path_to_file)
    if os.path.exists(path_to_file) and path_to_file[-4:] == ".txt":
        file = open(path_to_file, 'r')
        csv_file = open('C:\\Users\\User\\Desktop\\DDoS.csv', 'w', newline='')
        writer = csv.writer(csv_file)
        header = ['Адрес источник', 'Автономная сеть', 'CIDR ASN', 'Код страны', 'Название страны', 'Подсеть',
                  'Пул адресов']
        writer.writerow(header)
        for ip in file:
            clear_ip = ip.replace('\n', '')
            result_to_csv = location(clear_ip)
            print(result_to_csv.split(","))
            writer.writerow(result_to_csv.split(","))
        csv_file.close()

        read_file = pd.read_csv(r'C:\Users\User\Desktop\DDoS.csv', sep=",", encoding="cp1251")
        read_file.to_excel(r'C:\Users\User\Desktop\DDoS.xlsx', index=None, header=True)

    else:
        print("Указанный файл не существует!")
