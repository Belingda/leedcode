import bs4
import requests
import lxml.html
import html5lib
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}
def SendReq(url):
	r = requests.get(url, headers=headers)
	return r.text.encode(encoding='utf-8')

def Videodownload(SearchUrl):
	try:
		content = SendReq(SearchUrl)
	except:
		print("请求%s失败"%SearchUrl)
		return
	soup = bs4.BeautifulSoup(content, "html5lib")
	items = soup.find_all("div",attrs={"class": "bilibili-player-video"})
	print(len(items))
	if len(items)>0:
		for item in items:
			videourl = item.find("src")
			print(videourl)

Videodownload("https://v.qq.com/x/page/g0308s5jwqw.html")