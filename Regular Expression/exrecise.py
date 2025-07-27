input_strings = ["789", "123", "0041"]
#  1 questn- Check if Strings Have Only Octal Digits

def is_octal(s):
    return all(ch in '01234567' for ch in s)

input_strings = ["789", "123", "0041"]
results = {s: is_octal(s) for s in input_strings}
print(results)

# question 2: extract User ID, Domain Name, and Suffix from Emails

emails = ["purk@facebook.com", "sunder13@google.com"]

for email in emails:
    user_id, rest = email.split('@')
    domain, suffix = rest.split('.')
    print(f"Email: {email}")
    print(f"User ID: {user_id}")
    print(f"Domain: {domain}")
    print(f"Suffix: {suffix}")
    print("------")

#Split Irregular Sentence into Proper Words
import re

sentence = "A, very very; irregular_sentence"
# Replace punctuation with space, then split
cleaned = re.sub(r'[^\w\s]', ' ', sentence)     # Remove punctuation
cleaned = re.sub(r'_', ' ', cleaned)            # Replace underscore with space
words = cleaned.split()
print(' '.join(words))



 #Clean Tweet: Remove URLs, Hashtags, Mentions, RTs, CCs, and Punctuation
import re

tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #rstats"

# Remove RT, CC, mentions, hashtags, URLs, and punctuations
clean = re.sub(r'\b(RT|cc)\b', '', tweet)                           # Remove RT and cc
clean = re.sub(r'@\w+', '', clean)                                 # Remove mentions
clean = re.sub(r'#\w+', '', clean)                                 # Remove hashtags
clean = re.sub(r'http\S+', '', clean)                              # Remove URLs
clean = re.sub(r'[^\w\s]', '', clean)                              # Remove punctuation
clean = re.sub(r'\s+', ' ', clean).strip()                         # Normalize spaces
print(clean)

#Extract All Text Between Tags from HTML
import requests
from bs4 import BeautifulSoup

url = "https://raw.githubusercontent.com/selva66/datasets/master/sample.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
text_list = [tag.get_text(strip=True) for tag in soup.find_all() if tag.get_text(strip=True)]

print(text_list)

#Find Words Starting and Ending with Same Character
words = ["civic", "trust", "widows", "6", 
        "maximum", "museums", "as", "Learning", "Outcomes"]
same_char_words = [w for w in words if w[0].lower() == w[-1].lower()]
print(same_char_words)

