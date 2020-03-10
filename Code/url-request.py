#/usr/bin/python3

import urllib
import re

def Connect2Web():
  aResp = urllib.urlopen("https://uniservices1.uobgroup.com/secure/online_rates/gold_and_silver_prices.jsp")
  web_pg = aResp.read()

  pattern = "<td><b>SILVER PASSBOOK ACCOUNT</b></td>" + "<td>(.*)</td>" * 4
  m = re.search(pattern, web_pg)
  if m:
    print("SILVER PASSBOOK ACCOUNT:")
    print("\tCurrency:", m.group(1))
    print("\tUnit:", m.group(2))
    print("\tBank Sells:", m.group(3))
    print("\tBank Buys:", m.group(4))
  else:
    print("Nothing found")

#Define a main() function that prints a litte greeting
def main():
  Connect2Web()

# This is the standard boilerplate that calls the maun function.
if __name__ == '__main__':
    main()    