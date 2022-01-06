import math

# goes from 6am to 6pm
# 6am, 6pm have the same angle
# 6:15am, 5:45pm have the same angle
# ... etc ...
# 12:00 noon has angle = 0

resolution = 72
tanIncrement = 90/resolution
decimalPlaces = 3

# first increment will be:
# (12:00 noon) +/- ((6 hrs)/resolution)
# resolution = 24 -> 15 minute increments
# resolution = 72 -> 5 minute increments

lat_deg = 44.9366 # your degrees of latitude
sinLat = math.sin(math.radians(lat_deg))

Angles = []
# (hrs away from 12:00 noon, angle on sundial)
Angles.append((0, 0))

for i in range(resolution):
	t = math.tan(math.radians((i+1) * tanIncrement))
	shadowAngle_deg = math.degrees(math.atan(t * sinLat))
	newPair = (
		round((6/resolution) * (i+1), decimalPlaces), 
		round(shadowAngle_deg, decimalPlaces)
	)
	Angles.append(newPair)

for pair in Angles:
	print(pair)