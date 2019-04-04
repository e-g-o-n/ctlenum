import argparse
import requests
import config

parser = argparse.ArgumentParser()
parser.add_argument('--target', help="target for scan. example: --target google.com", required=True)
parser.add_argument('-nw', action='store_true', help="target for scan. example: --target google.com")

args = parser.parse_args()

target = args.target


class CtlEnum(object):
    def __init__(self, api, domain, nowilds):
        self.api = api
        self.domain = domain
        self.nowilds = nowilds

    def print_target(self):
        print('Target Domain: ', str(self.domain))

    def get_dns(self):
        url = 'https://api.certspotter.com/v1/issuances?domain=' + self.domain + \
              '&include_subdomains=true&match_wildcards=true&expand=dns_names'
        header = {'Authorization': 'Bearer ' + self.api}
        r = requests.get(url, headers=header).json()
        dns_list = list()

        for item in r:
            list_count = len(item['dns_names'])
            if list_count > 1:
                for entry in item['dns_names']:
                    if self.nowilds is True and entry[0][:1] is '*':
                        pass
                    else:
                        dns_list.append(str(entry))
            else:
                str_item = str(item['dns_names'][0])
                if self.nowilds is True and str_item[0][:1] is '*':
                    pass
                else:
                    dns_list.append(str_item)

        return set(dns_list)


scan = CtlEnum(config.api_key, target, args.nw)

for dnsentry in scan.get_dns():
    print(dnsentry)
