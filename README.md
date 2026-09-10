# synent-task6-weatherapp-otsileLekabe

Weather App (API Integration) — Task 6, Intermediate Level
Synent Technologies Python Development Internship

## Objective
Fetch and display real-time weather data for a city entered by the user.

## Features
- User inputs a city name
- Displays current temperature, humidity, wind speed, and general weather condition
- Translates numeric weather codes into readable descriptions (e.g. "Slight rain")
- Handles invalid city names and network errors gracefully
- Runs as an interactive command-line loop (enter multiple cities, or `exit` to quit)

## Tech Stack
- Python 3
- [`requests`](https://pypi.org/project/requests/) library
- [Open-Meteo API](https://open-meteo.com/) (free, no API key required) for geocoding and current weather

## Setup
```bash
pip install requests
python weather.py
```

## Usage
```
Weather App - type 'exit' to quit
Enter a city name: Pretoria

Weather in Pretoria, South Africa
Condition: Mainly clear
Temperature: 22.5°C
Humidity: 40%
Wind: 12.3 km/h
```

## How It Works
1. `get_coordinates(city_name)` — calls Open-Meteo's geocoding API to turn a city name into latitude/longitude
2. `get_weather(latitude, longitude)` — calls Open-Meteo's forecast API with those coordinates to get current conditions
3. Weather codes returned by the API are mapped to human-readable descriptions via a lookup dictionary
4. All network calls are wrapped in error handling for invalid cities and connection issues

## Project Structure
```
synent-task6-weatherapp-otsile/
├── weather.py      # Main application
├── README.md
└── .gitignore
```

## Author
Otsile — Synent Technologies Python Internship
