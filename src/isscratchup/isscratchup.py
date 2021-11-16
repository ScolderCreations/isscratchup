import urllib3
import json
def isUp():
  healthsite = 'https://api.scratch.mit.edu/health'
  http = urllib3.PoolManager()
  r = http.request('GET', healthsite)
  if '{"connected\":true,\"ready\":true}' in r.text:
    ret = True
  else:
    ret = False
  return(ret)

def apiHealth():
  healthsite = 'https://api.scratch.mit.edu/health'
  http = urllib3.PoolManager()
  r = http.request('GET', healthsite)
  return(json.load(r.text))
