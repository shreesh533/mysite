System Design - Notification service
    Please refer Notification.txt and Notification.jpg


Challenge - URL Shortning
Application name: urlshorter
URLs: 

Create Short URL: 
curl --location 'http://127.0.0.1:8000/urlshorter/shortner?short_url=6440928' \
--header 'Content-Type: application/json' \
--data '{
    "long_url": "https://app.example-random-nxklansclasnccsmcsclsc.com"
}'


Redirect URL:
curl --location --request GET 'http://127.0.0.1:8000/urlshorter/redirect?short_url=6440928' \
--header 'Content-Type: application/json' \
--data '{
    "long_url": "https://app.example-random-nxklansclasnccsmcsclsc.com"
}'


Island Connnectivity Problem Attempt:
island_connectivity.py




