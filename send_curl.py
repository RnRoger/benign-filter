import requests
import sys

def main():
    """Send a cURL request to the API"""
    url = "http://localhost:8080"
    
    payload = f"{{\n\t\"filename\": \"{sys.argv[1]}\",\n\t\"chr\": \"{sys.argv[2]}\"\n}}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "905a33d4-00fa-47a1-a685-5d28a3b915e8,25066761-0331-4104-bff6-03e57f626170",
        'Host': "localhost:8080",
        'accept-encoding': "gzip, deflate",
        'content-length': "71",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    print(f"\n{response.text}\n")


if __name__ == "__main__":
    main()