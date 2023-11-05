import requests
from extractors.school_code import get_school_code
import folium

def get_location(school_name):

    schools = get_school_code(school_name)
    print(schools)
    
    results = []
    
    for school in schools:
        address1 = school['address_1']
        address2 = school['address_2']
        
        params = {
            "service": "address",
            "request": "getcoord",
            "crs": "epsg:4326",
            "address": address1 + " " + address2,
            "format": "json",
            "type": "road",
            "key": "67FF3424-0D60-352C-9E61-5251766215FE"
        }
        base_url = "https://api.vworld.kr/req/address"
        response = requests.get(base_url, params=params)
        json_data = None             

        if response.status_code != 200:
            print("Can't access the information")
        else:
            json_data = response.json()
            x = json_data['response']['result']['point']['x'] # 경도
            y = json_data['response']['result']['point']['y'] # 위도
            location = {
                "school_name": school['school_name'],
                "longitude": x,
                "latitude": y}
            results.append(location)

            map = folium.Map(location=[y, x], zoom_start= 10)
            marker = folium.Marker(location=[y, x], popup=school['school_name'], icon=folium.Icon(color='red'))
            marker.add_to(map)
            map.save(f'{school['school_name']}.html')
    return results