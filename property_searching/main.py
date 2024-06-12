import requests
from bs4 import BeautifulSoup
import scarp

def main():
    page = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
    soup = BeautifulSoup(page.text, "html.parser")

    pricetag_list = soup.select(".PropertyCardWrapper__StyledPriceLine")
    linktag_list = soup.select(".property-card-link")
    links = [tags.attrs["href"] for tags in linktag_list]
    price_list = scarp.prices(pricetag_list=pricetag_list)
    addresses = [tags.text.strip() for tags in soup.find_all("address")]
    
    scarp.openForm()
    for index in range(len(links)):
        scarp.formFiller(
            address=addresses[index],
            price=price_list[index],
            link=links[index]
        )
    scarp.closeForm()

if __name__ == "__main__":
    main()