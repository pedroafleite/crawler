from bs4 import BeautifulSoup, SoupStrainer
import requests


def main(URL):
	# opening our output file in append mode
	File = open("out.csv", "a")

	# specifying user agent, You can use other user agents
	# available on the internet
	HEADERS = ({
		'User-Agent':
		'Mozilla/5.0 (X11; Linux x86_64) ApleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
		'Accept-Language': 'pt-BR, en;q=0.5'})

	# Making the HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Creating the Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")

	# retrieving product title
	try:
		# Outer Tag Object
		url = soup.find_all("a", href=True)
		
	except AttributeError:
		url = "NA"

	for i in url:
		if i['href'].startswith("/produto"):
			print("url = ", i['href'])
			# saving the title in the file	
			File.write(f"https://www.americanas.com.br{i['href']};")

			nextpage = requests.get(f"https://www.americanas.com.br{i['href']}", headers=HEADERS)
			nextsoup = BeautifulSoup(nextpage.content, 'lxml')

			try:
				gtin = nextsoup.find_all("td", class_='src__Text-sc-70o4ee-7 iHQLKS')[3]
				for tag in gtin:
					print("gtin = ", tag.text)
					File.write(f"{tag.text.strip()};")	
			except Exception:
				File.write("NA;")

			try:
				descricao = nextsoup.find("div", class_='src__Description-sc-13f3i2j-2 bqnMru')
				print("descricao = ", descricao.text)
				File.write(f"{descricao.text};")
			except Exception:
				File.write("NA;")

			try:
				price = nextsoup.find_all(
					"div", class_='src__BestPrice-sc-1jvw02c-5 cBWOIB priceSales')
				for tag in price:
					print("preco = ", tag.text)
					File.write(f"{tag.text};")
			except Exception:
				File.write("NA;")
			
			try:
				foto = nextsoup.find_all("img", src=True)
				print("foto = ", foto[1]['src'])
				File.write(f"{foto[1]['src']};")
			except Exception:
				File.write("NA;")

	File.close()

if __name__ == '__main__':
	file = "https://www.americanas.com.br/categoria/tv-e-home-theater/acessorios-para-tv-e-video?viewMode=list&limit=10&offset=10"
	main(file)
