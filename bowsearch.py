# BowSearch
# Coded by BowFun

# Import the main search function (webbrowser) and a wait function (time).
import webbrowser
import time

# Introduction to the program.
print("BowSearch v1")
print("Written by BowFun")
time.sleep(1)
print("Welcome to BowSearch! This will search the web across many search engines.")

# Search
print("Please type your search:")
search = input()

#Google function
googleurl = "https://www.google.com/search?q=" + search
print("Opening Google")
webbrowser.open(googleurl)

#DuckDuckGo function
ddgurl = "https://duckduckgo.com/?q=" + search
print("Opening DuckDuckGo")
webbrowser.open(ddgurl)

#Bing function
bingurl = "https://www.bing.com/search?q=" + search
print("Opening Bing")
webbrowser.open(bingurl)

#Disabled Search Engines
#If you want to enable one, uncomment it.
#If there are two hashtags (##), only remove one.

##Whoogle
##A privacy-respecting alternative to Google.
#whoogleurl = "https://whoogle.privacydev.net/search?q=" + search
#print("Opening Whoogle (Manually Enabled)")
#webbrowser.open(whoogleurl)

##Brave Search
##Also a privacy-respecting search engine.
#braveurl = "https://search.brave.com/search?q=" + search
#print("Opening Brave Search (Manually Enabled)")
#webbrowser.open(braveurl)

##Search Encrypt
##Encrypts your searches locally.
#seurl = "https://www.searchencrypt.com/search?q=" + search
#print("Opening Search Encrypt (Manually Enabled)")
#webbrowser.open(seurl)