import requests
from bs4 import BeautifulSoup

re = requests.sessions.Session()

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

forum = re.get('https://forum.aspose.com/latest', headers=headers)

if forum.status_code!=200:
  print(forum.status_code)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://forum.aspose.com/latest',
    'X-CSRF-Token': 'undefined',
    'X-Requested-With': 'XMLHttpRequest',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=4',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

csrfc = re.get("https://forum.aspose.com/session/csrf", headers=headers)

if csrfc.status_code==200:
    csrf=csrfc.json()['csrf']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://forum.aspose.com/latest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://forum.aspose.com',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

data = {
    'authenticity_token': csrf
}

ocid = re.post('https://forum.aspose.com/auth/oidc', headers=headers, data=data)

if ocid.status_code==200:
    print(ocid.)