import requests
import statistics
from bs4 import BeautifulSoup


# baseball_websites = [
# "https://www.mlb.com/news"
# ]

baseball_websites = [
"https://www.mlb.com/news",
"https://www.mlbtraderumors.com",
"https://www.fangraphs.com/blogs/",
"http://www.milb.com/index.jsp",
"https://www.yardbarker.com/mlb",
"https://www.baseballprospectus.com",
"https://news.google.com/?q=baseball&tbm=nws&hl=en-US&gl=US&ceid=US:en", 
"https://www.reddit.com/r/baseball",
"https://blog.justbats.com",
"https://nypost.com/baseball",
"https://razzball.com",
"https://www.minorleagueball.com",
"https://d1baseball.com",
"https://www.royalsreview.com",
"https://sabr.org",
"https://www.brewcrewball.com",
"https://mlbcomblogs.mlblogs.com",
"https://federalbaseball.com",
"https://bluejaysnation.com",
"https://purplerow.com",
"https://beyondtheboxscore.com",
"https://southsidesox.com",
"http://dodgersdigest.com",
"https://www.baseballthinkfactory.org/newsstand",
"https://drivelinebaseball.com/blog",
"https://whatproswear.com",
"https://gaslampball.com",
"https://justbatreviews.com/blog",
"https://baseballfactory.com/news",
"http://joeposnanski.com",
"https://redlegnation.com",
"https://puckettspond.com",
"http://bronxbaseballdaily.com",
"http://jaysfromthecouch.com",
"http://collegebaseballdaily.com",
"http://2018youthbats.com/blog",
"http://insiderbaseball.com/blog",
"http://thebaseballdiamond.com",
"http://thecubreporter.com",
"http://americanassociationbaseball.com",
"http://offthebenchbaseball.com",
"http://birdswatcher.com",
"http://baseballreflections.com",
"http://rayscoloredglasses.com",
"http://mister-baseball.com",
"http://216stitches.org"
]

def ranking(websites):
	link_dic = {}
	for url in websites:
		res = requests.get(url)
		r_soup = BeautifulSoup(res.text, "lxml")
		links = r_soup.find_all("a")
		for key in links:
			if key in link_dic:
				link_dic[key] += 1
			else:
				link_dic[key] = 1
	
	numbers = [link_dic[key] for key in link_dic]
	med = 10
	low = []
	high = []
	for key in link_dic:
		if link_dic[key] <= med:
			low.insert(len(low), key)
		else:
			high.insert(len(high), key)

	return low, high



low, high = ranking(baseball_websites)

def looper(list):
	for link in list:
		print(link)

looper(high)









