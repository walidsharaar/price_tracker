import requests

# address of the product I want to track
PRODUCT_URL ="https://www.amazon.de/s?k=iphone+12+pro+max&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3IA9HGLKVZ1VH&sprefix=iphone%2Caps%2C253&ref=nb_sb_ss_ts-doa-p_2_6"
# I have to find the HTTP header from http://myhttpheader.com/
HEADER = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
    "Accept_Language":"en-US,en;q=0.9"
}

# request to html page
response = requests.get(PRODUCT_URL,headers=HEADER)

