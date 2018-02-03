import multiprocessing
import urllib.request

url_list = [
  "http://google.com",
  "http://youtube.com",
  "http://github.com"
]

def get_site_contents(url):
  response = urllib.request.urlopen(url)
  return response.read()

process_pool = multiprocessing.Pool(5)
print(process_pool.map(get_site_contents, url_list))
