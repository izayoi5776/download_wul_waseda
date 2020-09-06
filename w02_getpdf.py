import urllib.request, urllib.error, urllib.parse
import os

with open("urls.txt") as f:
  for url in f.read().split("\n"):
    print(url, end="")
    filename = os.path.basename(url)
    if os.path.exists(filename):
      print("... SKIP")
    else:
      urllib.request.urlretrieve(url, filename=filename)
      print("... DONE")

