def isUp(): {
  import urllib3
  healthsite = 'https://api.scratch.mit.edu/health'
  http = urllib3.PoolManager()
  r = http.request('GET', healthsite)
  if '{"connected\":true,\"ready\":true}' in r.text:
    ret = True
  else:
    ret = False
  return(ret)
}
