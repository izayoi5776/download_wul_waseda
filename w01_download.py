import urllib.request, urllib.error, urllib.parse
import os
import sys
import time
from bs4 import BeautifulSoup

# eg https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E5%AE%9D%E5%B7%BB&szlmt=30
def get1url(url):
  with urllib.request.urlopen(url) as res:
    html = res.read()
    soup = BeautifulSoup(html, "html5lib")
    #print(soup)
    for i in soup.select("a>img"):
      #print(i.parent["href"])
      getlvl2url(urllib.parse.urljoin(url, i.parent["href"]))
      

# eg https://www.wul.waseda.ac.jp/kotenseki/html/bunko19/bunko19_f0399_0011/index.html
def getlvl2url(url):
  #print("url=" + url, end="")
  try:
    with urllib.request.urlopen(url) as res:
      html = res.read()
      soup = BeautifulSoup(html, "html5lib")
      for i in soup.select("a>img"):
        #print("   result=" + i.parent["href"])
        getlvl3url(urllib.parse.urljoin(url, i.parent["href"]))
  except Exception as e:
    #print("... SKIP")
    print("ERROR SKIP url=" + url)
    print(e)

# eg https://archive.wul.waseda.ac.jp/kosho/bunko19/bunko19_f0399/bunko19_f0399_0035/bunko19_f0399_0035_0004/
def getlvl3url(url):
  #print("url=" + url, end="")
  try:
    with urllib.request.urlopen(url) as res:
      html = res.read()
      soup = BeautifulSoup(html, "html5lib")
      for i in soup.select("a"):
        if(i["href"].endswith("pdf")):
          print(urllib.parse.urljoin(url, i["href"]))
  except Exception as e:
    print("ERROR SKIP url=" + url)
    print(e)


# --- MAIN ----
urls = (
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E5%AE%9D%E5%B7%BB&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E5%BC%BE%E8%A9%9E&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E5%A4%A7%E9%BC%93%E6%9B%B8&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E5%AD%90%E5%BC%9F%E6%9B%B8&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E6%9C%A8%E9%AD%9A%E6%9B%B8&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E7%89%8C%E5%AD%90%E6%9B%B2&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E7%9F%B3%E6%B4%BE%E6%9B%B8&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E5%B2%94%E6%9B%B2&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E6%99%82%E8%AA%BF%E5%B0%8F%E6%9B%B2&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E8%AC%8E%E8%AA%9E&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E8%93%AE%E8%8A%B1%E8%90%BD&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E7%9B%B8%E8%81%B2&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E9%9B%99%E7%B0%A7&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E4%B8%AD%E5%9B%BD%E5%B9%B4%E7%94%BB&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E7%B4%99%E9%8C%A2&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E8%B7%AF%E5%BC%95&szlmt=9999",
"https://www.wul.waseda.ac.jp/kotenseki/search.php?cndbn=%E7%9A%AE%E5%BD%B1%E6%88%AF&szlmt=9999",
"https://www.wul.waseda.ac.jp/kosho/ni16/ni16_2272/taiwan_list.html",
"https://www.wul.waseda.ac.jp/kosho/ni16/ni16_2272/manshu_list.html",
)
for url in urls:
  get1url(url)

