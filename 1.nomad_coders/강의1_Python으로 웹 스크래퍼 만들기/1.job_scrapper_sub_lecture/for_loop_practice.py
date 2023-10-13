# For Loops 실습

websites = [
    'google.com',
    'apple.com',
    'https://naver.com',
    'daum.net',
    'dhrohsnn.synology.me'
]

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)


