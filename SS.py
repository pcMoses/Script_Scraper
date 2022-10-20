# here is my attemp at making a scrapper that pulls code from webpages to run in a script.
# using beautiful soup here is the web page i used to build most the basics of the program
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree
#i hope you enjoy my creation or find it useful.

from bs4 import BeautifulSoup
import requests

url = "https://operating-systems.wonderhowto.com/how-to/create-admin-user-account-using-cmd-prompt-windows-0

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
#list_tags = []
#i = {'code', 'kbd', 'pre', 'samp'}

#doesnt work
#for code in doc.find_all('code','kbd','pre','samp'):
#    print(code.string)

#append all tags in website to list_tags
#for tag in doc.find_all(True):
# if tag == i :then print(tag.string) this is just an idea to test.
#    list_tags.append(tag.name)

#loop through list and print out tag.string if matches i
#try doing SoupStrainer, print(BeautifulSoup(html_doc, "html.parser", parse_only_a_tags).prettify())
#if i in list_tags:
#   print(i)
#    if (i == 'code' or 'kbd' or 'pre' or 'samp'):
#        print(i)

# make the variable i become the searched tag and print its document.

#THIS CODE WILL GET THE JOB DONE BUT I WANT TO EXPAND AND GRAB MORE TAGS THAN JUST <code>
#does work for just the code tag
for code in doc.find_all('code'):
    print(code.string)
