# importing libraries
from bs4 import BeautifulSoup
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
		title = soup.find_all("span",
						class_="src__Text-sc-154pg0p-0 product-name__Name-sc-n8j4w0-0 fcRttM product-info__ProductNameUI-sc-94t9sv-2 hswIUF")

			
	except AttributeError:
		title = "NA"
	for tag in title:
		print("product Title = ", tag.text.strip())

	# saving the title in the file
	File.write(f"{title},")

	# retrieving price
	try:
		price = soup.find_all(
			"span", attrs={'class': 'src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-1i4tohf-1 hjtXiU'})
		
		# we are omitting unnecessary spaces
		# and commas form our string
	except AttributeError:
		price = "NA"
	for tag in price:
		print("product Price = ", tag.text.strip())

	# saving
	File.write(f"{price},")

	# closing the file
	File.close()

if __name__ == '__main__':
# opening our url file to access URLs
	file = open("url.txt", "r")

	# iterating over the urls
	for links in file.readlines():
		main(links)