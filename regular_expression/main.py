import re

text = "The quick brown fox jumps over the lazy dog."
# Search for a pattern
match = re.search("brown", text)
if match:
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())

# Find all occurrences of a pattern
matches = re.findall("the", text, re.IGNORECASE) # Case-insensitive search
print("Matches:", matches)

# Replace all occurrences of a pattern
new_text = re.sub("fox", "cat", text)
print("New text:", new_text)
# Compile a regex for efficiency (if used multiple times)

pattern = re.compile(r"\b\w+\b") # Matches whole words
words = pattern.findall(text)
print("Words:", words)


# Example of using regex to validate an email address
email = "Contact us at support@example.com"
pattern = re.compile(r"[\w\.-]+@[\w\.-]+")
match = pattern.search(email)
if match:
    print("Valid email found:", match.group())  


# Example of using regex to extract URLs from a string
text_with_urls = "Visit our site at https://example.com or http://example.org for more info."
url_pattern = re.compile(r"https?://[\w\.-]+")
urls = url_pattern.findall(text_with_urls)
print("Extracted URLs:", urls)  

# Example of using regex to split a string by multiple delimiters
text_to_split = "apple, banana; orange|grape"
split_pattern = re.compile(r"[;,|]")
split_text = split_pattern.split(text_to_split)
print("Split text:", split_text)   


# Example of using regex to validate a phone number
phone_number = "Call us at +1-800-555-1234"
phone_pattern = re.compile(r"\+?\d{1,3}-\d{3}-\d{3}-\d{4}")
if phone_pattern.search(phone_number):
    print("Valid phone number found:", phone_number)

# Example of using regex to match a date in the format YYYY-MM-DD
date_string = "Today's date is 2023-10-01."
date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
date_match = date_pattern.search(date_string)
if date_match:
    print("Valid date found:", date_match.group())

# Example of using regex to validate a password
password = "P@ssw0rd123"
password_pattern = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
if password_pattern.match(password):
    print("Valid password")
else:
    print("Invalid password")

# Example of using regex to extract hashtags from a string
text_with_hashtags = "Check out #Python and #Regex for more info!"
hashtag_pattern = re.compile(r"#\w+")
hashtags = hashtag_pattern.findall(text_with_hashtags)
print("Extracted hashtags:", hashtags)

# Example of using regex to validate a URL
url = "https://www.example.com/path/to/resource?query=param#fragment"
url_pattern = re.compile(r"^(https?://)?([\w.-]+)(:[0-9]+)?(/[\w./?%&=-]*)?$")
if url_pattern.match(url):
    print("Valid URL:", url)

