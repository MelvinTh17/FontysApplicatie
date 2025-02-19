import dns.resolver
from tabulate import tabulate
import time
from os import system

def check_domein(domein):
    datalijst = []
    records = [
        'NONE',
        'A',
        'NS',
        'MD',
        'MF',
        'CNAME',
        'SOA',
        'MB',
        'MG',
        'MR',
        'NULL',
        'WKS',
        'PTR',
        'HINFO',
        'MINFO',
        'MX',
        'TXT',
        #COPYRIGHT MELVIN 2024
        'RP',
        'AFSDB',
        'X25',
        'ISDN',
        'RT',
        'NSAP',
        'NSAP-PTR',
        'SIG',
        'KEY',
        'PX',
        'GPOS',
        'AAAA',
        'LOC',
        'NXT',
        'SRV',
        'NAPTR',
        'KX',
        'CERT',
        'A6',
        'DNAME',
        'OPT',
        'APL',
        'DS',
        'SSHFP',
        'IPSECKEY',
        'RRSIG',
        'NSEC',
        'DNSKEY',
        'DHCID',
        'NSEC3',
        'NSEC3PARAM',
        'TLSA',
        'HIP',
        'CDS',
        'CDNSKEY',
        'CSYNC',
        'SPF',
        'UNSPEC',
        'EUI48',
        'EUI64',
        'TKEY',
        'TSIG',
        'IXFR',
        'AXFR',
        'MAILB',
        'MAILA',
        'ANY',
        'URI',
        'CAA',
        'TA',
        'DLV',
    ]
    clear()
    for rec in records:
        try:
            antwoord = dns.resolver.resolve(domein, rec)
            for rdata in antwoord:
                datalijst.append([rec, rdata.to_text()])
                
        except:
            quit


    print(tabulate(datalijst, headers=['Type', 'Data'], tablefmt="grid"))

if __name__ == '__main__':
    clear = lambda: system('clear') 
    clear()
    print("Hoi! Welkom bij de DNS resolver. Het programma is even aan het opstarten")
    time.sleep(5)
    print("\n \n \n")
    domein = input("Welk domein wil je checken?: ")
    check_domein(domein)