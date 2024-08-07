import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#Step 2:Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify())

#Step 3:HTML tree traversal
#Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup) # 3. BeautifulSoup
# 4. Comment
#markup = "<p><!-- this is a comment --></p>"
#soup2 = BeautifulSoup(markup)
#print(type(soup2.p.string))


# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)

#print(anchors)

# Get first element in the html page
print(soup.find('p'))

# Get classes of any element in the html page
print(soup.find('p')['class'])

# Find all the elements with class lead
print(soup.find_all("p",class_="lead"))

# Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
#Get all the links on the page
for link in anchors:
    if (link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)

#.contents - A tag's children are available as a list
#.children - A tag's children are available as a generator
imgpreview2 = soup.find(id='imgpreview2')

#for elem in imgpreview2.contents:
#    print(elem)

#for item in imgpreview2.strings:
 #   print(item)
#for item in imgpreview2.stripped_strings:
 #   print(item)

#print(imgpreview2.parent)
#for item in imgpreview2.parents:
 #   print(item.name)

#print(imgpreview2.previous_sibling.previous_sibling)
#print(imgpreview2.next_sibling.next_sibling)

elem = soup.select('.modal-footer')
print(elem)


