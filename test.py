import http.client

conn = http.client.HTTPSConnection("auto-download-all-in-one-big.p.rapidapi.com")

payload = "{\"url\":\"https://www.tiktok.com/@yeuphimzz/video/7237370304337628442\"}"

headers = {
    'x-rapidapi-key': "99bb57d209mshb6ca809dc147a3ep1a51e7jsnf829ae92aef6",
    'x-rapidapi-host': "auto-download-all-in-one-big.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/v1/social/autolink", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))