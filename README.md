# ctlenum
Enumeration of Certificate Transparency Logs

**Requirements:**
  ```pip install requests```
  
 ```pip install argparse```

**API_Key for certspotter:**
  - Register an account with sslmate.com (certspotter)
  
**Grab API Key from:**
  - https://sslmate.com/account/api_credentials

edit 'config.py' and place your API key in the config file

```python ctlenum.py --target targetdomain```

**Arguments:**
 --target sets target domain
 
 -e exclusive subdomain for target domain
 
 -nw no wildcard returned subdomains, example *.google.com

**example:**
   ```python ctlenum.py --target google.com```
   
