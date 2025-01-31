# Weather Application Using CLI

This is a simple Python script that fetches current weather data and a 5-day weather forecast for a user-specified city using the OpenWeatherMap API.

## Features

- Fetches current weather data (temperature, weather condition, and humidity) for a given city.
- Provides a 5-day weather forecast with average temperature, common weather condition, and average humidity for each day.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x** installed on your system.
2. An **API key** from [OpenWeatherMap](https://openweathermap.org/api). Sign up for a free account to get your API key.

## Installation

1. Clone this repository or download the script to your local machine.
2. Install the required Python packages using pip:

   ```bash
   pip install python-dotenv requests
   ```

3. Create a `.env` file in the same directory as the script and add your OpenWeatherMap API key:

   ```env
   MYKEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your actual API key.

## Usage

1. Run the script:

   ```bash
   python weather_app.py
   ```

2. Enter the name of the city when prompted:

   ```
   Enter City: London
   ```

3. The script will display:
   - The current weather conditions for the city.
   - A 5-day weather forecast with average temperature, common weather condition, and average humidity for each day.

## Example Output

```
Enter City: London
Current Weather at London is Clouds, with current temperature of 15.0 Celcius and humidity of 77
The Forecast for next 5 days is:
2023-10-01: 14.5°C, Scattered Clouds, Humidity: 75.0%
2023-10-02: 13.8°C, Light Rain, Humidity: 80.0%
2023-10-03: 12.3°C, Overcast Clouds, Humidity: 85.0%
2023-10-04: 11.7°C, Moderate Rain, Humidity: 90.0%
2023-10-05: 10.2°C, Clear Sky, Humidity: 70.0%
```

## Code Overview

- The script uses the `requests` library to make API calls to OpenWeatherMap.
- The `python-dotenv` library is used to load the API key from a `.env` file.
- The script fetches:
  - Current weather data using the `/weather` endpoint.
  - Forecast data using the `/forecast` endpoint.
- The forecast data is processed to calculate average temperature, common weather condition, and average humidity for each day.

## Acknowledgments

- Thanks to [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.

