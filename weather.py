import requests
import sys

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle: Light",
    53: "Drizzle: Moderate",
    55: "Drizzle: Dense intensity",
    56: "Freezing Drizzle: Light",
    57: "Freezing Drizzle: Dense intensity",
    61: "Rain: Slight",
    63: "Rain: Moderate",
    65: "Rain: Heavy intensity",
    66: "Freezing Rain: Light",
    67: "Freezing Rain: Heavy intensity",
    71: "Snow fall: Slight",
    73: "Snow fall: Moderate",
    75: "Snow fall: Heavy intensity",
    77: "Snow grains",
    80: "Rain showers: Slight",
    81: "Rain showers: Moderate",
    82: "Rain showers: Violent",
    85: "Snow showers slight",
    86: "Snow showers heavy",
    95: "Thunderstorm: Slight or moderate",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        return None
    place = results[0]
    return place["latitude"], place["longitude"], place["name"], place.get("country", "")

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
    
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()["current"]

def main():
    print("Weather App - type 'exit' to quit\n")
    while True:
        city = input("Enter a city name: ").strip()
        if city.lower() == "exit":
            sys.exit(0)
        if not city:
            continue

        try:
            coords = get_coordinates(city)
            if coords is None:
                print(f"Sorry, could not find '{city}'.\n")
                continue
            lat, lon, name, country = coords
            weather = get_weather(lat, lon)
            description = WEATHER_CODES.get(weather['weather_code'], "Unknown weather condition")


            print(f"\nWeather in {name}, {country}:")
            print(f"Weather Condition: {description}")
            print(f"Temperature: {weather['temperature_2m']}°C")
            print(f"Humidity: {weather['relative_humidity_2m']}%")
            print(f"Wind Speed: {weather['wind_speed_10m']} km/h\n")

        except requests.RequestException as e:
            print(f"Network error: {e}\n")


if __name__ == "__main__":
    main()