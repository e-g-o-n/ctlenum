# ctlenum
Enumeration of Certificate Transparency Logs

**Requirements:**
  - ```pip install requests```
  - ```pip install argparse```
  - API Key for sslmate's certspotter:
    - Register an account with sslmate.com (certspotter)
    - Grab API Key from: https://sslmate.com/account/api_credentials

**Before using:**
  - edit 'config.py' and place your API key in the config file
  - example: ```API_KEY = "legitimate_key"```

**Basic Use:**

```python ctlenum.py --target targetdomain```

**Arguments:**

 --target sets target domain
 
 -a include ALL non-target domains in output
 
 -w include wildcard subdomains in output. Example: \*.example.com

**Example w/ Arguments:**

   ```python ctlenum.py -a -w --target example.com```
   
