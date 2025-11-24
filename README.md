# unit-conversion-microservice
Local microservice using ZMQ to convert units.
Send a string to the listening server: f"{quantity} {unit}" to recieve back the converted unit as a string.

The following are the allowed conversions:
centimeters <-> inches
kilograms <-> pounds
celsius <-> fahrenheit
liters <-> gallons
miles <-> kilometers
feet <-> meters
mph <-> kph
