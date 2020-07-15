import requests

re = requests.post('http://165.227.106.113/post.php', {'username': 'admin', 'password': '71urlkufpsdnlkadsf'})
print(re.content)

