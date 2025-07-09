SELECT
  carrier_name,
  SUM(arr_flights) AS total_flights,
  SUM(arr_del15) AS delayed_flights,
  ROUND(SUM(arr_del15) * 1.0 / SUM(arr_flights), 3) AS delay_rate
FROM flight_delays
GROUP BY carrier_name
ORDER BY delay_rate DESC;

SELECT
  month,
  SUM(arr_flights) AS total_flights,
  SUM(arr_cancelled) AS cancelled_flights,
  ROUND(SUM(arr_cancelled) * 1.0 / SUM(arr_flights), 3) AS cancel_rate
FROM flight_delays
GROUP BY month
ORDER BY month ASC;

SELECT
  airport_name,
  ROUND(AVG(arr_delay), 1) AS avg_arrival_delay
FROM flight_delays
GROUP BY airport_name
ORDER BY avg_arrival_delay DESC
LIMIT 10;

SELECT
  carrier_name,
  ROUND(AVG(carrier_delay), 1) AS carrier_delay,
  ROUND(AVG(weather_delay), 1) AS weather_delay,
  ROUND(AVG(nas_delay), 1) AS nas_delay,
  ROUND(AVG(security_delay), 1) AS security_delay,
  ROUND(AVG(late_aircraft_delay), 1) AS late_aircraft_delay
FROM flight_delays
GROUP BY carrier_name
ORDER BY carrier_name;
