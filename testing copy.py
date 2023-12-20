import requests

def find_place_id(api_key, query):
    endpoint_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        'input': query,
        'inputtype': 'textquery',
        'fields': 'place_id',
        'key': api_key
    }
    response = requests.get(endpoint_url, params=params)
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'OK':
            place_id =  result['candidates'][0]['place_id']
        # Assuming you have a valid place_id from the previous step
            google_maps_url = construct_google_maps_url(place_id)
            return google_maps_url
    return None
def construct_google_maps_url(place_id):
    base_url = "https://www.google.com/maps/place/?q=place_id:"
    return base_url + place_id

# Example usage
api_key = 'AIzaSyBKFYUc0NQnSTGjnXCAvyYVAqvRjfqkHhM'
query = 'AVUKAT SALIH DOĞAN'
place_url = find_place_id(api_key, query)
print(place_url)

