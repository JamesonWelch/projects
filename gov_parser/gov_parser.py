from site_downloader import download
import re

site = download("https://www.ca.gov/")


def header():
    """Get all header achor text and urls"""
    print("----- head anchor text -----")
    anchor_text = list(site.header.nav.find_all("span", {"class": "link-title"}))
    for text in anchor_text:
        print(text.text)

    print("----- header links -----")

    header_links = list(site.header.nav.find_all("a", {"class": "first-level-link"}))
    for link in header_links:
        print(link.get("href"))


def footer():
    """ Get all footer anchor text & urls """
    print("----- footer anchor text -----")
    footer = list(site.footer.find("ul", {"class": "footer-links"}))
    for text in footer:
        print(text.text)

    print("----- footer links -----")
    footer_links = list(site.footer.ul.find_all("a"))
    for link in footer_links:
        print(link.get("href"))


def heading():
    """Get all heeadings"""
    headings = site.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    for heading in headings:
        print(heading.text)


def para_text():
    """Print all text from paragraphs"""
    texts = site.find_all("p")
    for text in texts:
        print(text.text)


def img_link():
    """All image links"""
    img_links = site.find_all("img")
    for img in img_links:
        print(img.get("src"))


def social_link():
    """All social media links"""
    social_links = []
    social_links_header = site.header.find("div", {"class": "social-media-links"})
    for link in social_links_header("a", href=True):
        social_links.append(link["href"])

    social_links_footer = site.footer.find("ul", {"class": "socialsharer-container"})
    for link in social_links_footer("a", href=True):
        social_links.append(link["href"])
    social_links.pop(0)
    for i in range(len(social_links)):
        print(social_links[i])


def social_embeds():
    """ Get all embeded social posts on site """
    tweets = site.body.iframe.find_all("#document")
    print(tweets)


social_embeds()
social_link()
img_link()
para_text()
heading()
footer()
head()
