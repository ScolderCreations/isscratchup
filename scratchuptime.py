def check():
  import urllib3
  healthsite = 'https://api.scratch.mit.edu/health'
  http = urllib3.PoolManager()
  r = http.request('GET', healthsite)
  return(r.json)
