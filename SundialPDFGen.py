from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
import math
import os


def genLines(lattitude, resolution = 1, hoursToCalc = 7, decimalPlaces = 3):

	# All info on calcs obtained here: https://files.eric.ed.gov/fulltext/EJ802706.pdf

	# resolution = resolution, in hours, of the sundial

	# hoursToCals = the earliest and latest hour line to calculate
	# 7 -> from 5 am to 7 pm

	# 6am, 6pm have the same angle
	# 6:15am, 5:45pm have the same angle
	# ... etc ...
	# 12:00 noon has angle = 0

	angleIncrement = 15 * resolution

	timeLines = []
	# (hrs away from 12:00 noon, angle on sundial)

	timeLines.append((0, 0))
	for i in range(int(hoursToCalc / resolution)):
		# T = angle of this line if all lines on dial were uniformly spaced
		T = math.radians((i+1) * angleIncrement)
		
		# H = angle of this line projected onto our actual (elliptical) dial
		H = math.atan(math.tan(T) * math.sin(math.radians(lattitude)))
		H = (math.degrees(H) + 180) % 180 # account for negative numbers you get past 9pm

		# formatting for printing
		totalHours = (i+1) * resolution
		hoursOnly = math.floor(totalHours)
		minutesOnly = int((totalHours - hoursOnly) * 60)
		timeStr = str(hoursOnly).zfill(2) + ':' + str(minutesOnly).zfill(2)

		newTimeLine = (totalHours, round(H, decimalPlaces))
		timeLines.append(newTimeLine)
	return timeLines


def hrTo12HrStr(hr, includeMin = True, includeSec = False):
	am_pm = 'AM' if hr < 12 else 'PM'
	min = (hr - int(hr)) * 60
	sec = (min - int(min)) * 60

	hr_12 = int(hr) % 12
	hr_12 = 12 if hr_12 == 0 else hr_12

	min = str(int(min)).zfill(2)
	sec = str(int(sec)).zfill(2)

	if includeSec:
		timeStr = f"{hr_12}:{min}:{sec} {am_pm}"
	elif includeMin:
		timeStr = f"{hr_12}:{min} {am_pm}"
	else:
		timeStr = f"{hr_12} {am_pm}"

	return timeStr

	
def genPDF(
			path, 
			lineList, 
			lattitude, 
			lineLen = 325, 
			textOffset = 25,
			originOffset = (0, 0),
			fontSize = 8,
			gnomonScale = 1):

	doc = canvas.Canvas(path, pagesize=landscape(letter))
	doc.setLineWidth(.3)
	doc.setFont('Helvetica', fontSize)

	_w = doc._pagesize[0]
	_h = doc._pagesize[1]
	center = (_w/2, _h/2)
	origin = (center[0] + originOffset[0], 200 + originOffset[1])
	fontYRotatedOffset = -doc._fontsize / 3

	for (timeDiff, angle) in lineList:
		time_low = hrTo12HrStr(12 - timeDiff)
		time_high = hrTo12HrStr(12 + timeDiff)
		
		angle_low = 90 + angle
		angle_high = 90 - angle
		
		x_low = lineLen * math.cos(math.radians(angle_low))
		y_low = lineLen * math.sin(math.radians(angle_low))

		x_high = lineLen * math.cos(math.radians(angle_high))
		y_high = lineLen * math.sin(math.radians(angle_high))

		lineEnd_low = (origin[0] + x_low, origin[1] + y_low)
		lineEnd_high = (origin[0] + x_high, origin[1] + y_high)

		x_low = textOffset * math.cos(math.radians(angle_low))
		y_low = textOffset * math.sin(math.radians(angle_low))

		x_high = textOffset * math.cos(math.radians(angle_high))
		y_high = textOffset * math.sin(math.radians(angle_high))

		textLoc_low = (lineEnd_low[0] + x_low, lineEnd_low[1] + y_low)
		textLoc_high = (lineEnd_high[0] + x_high, lineEnd_high[1] + y_high)

		doc.line(origin[0], origin[1], lineEnd_low[0], lineEnd_low[1]) # low line

		doc.saveState()
		doc.translate(textLoc_low[0], textLoc_low[1])
		doc.rotate(angle_low + 180)
		doc.drawCentredString(0, fontYRotatedOffset, time_low)
		doc.restoreState()

		if angle_low != angle_high:
			doc.line(origin[0], origin[1], lineEnd_high[0], lineEnd_high[1]) # high line
			doc.saveState()
			doc.translate(textLoc_high[0], textLoc_high[1])
			doc.rotate(angle_high)
			doc.drawCentredString(0, fontYRotatedOffset, time_high)
			doc.restoreState()


	doc.showPage() # page break

	# now draw a triangle for the gnomon

	x = lineLen * gnomonScale
	y = lineLen * gnomonScale * math.tan(math.radians(lattitude))

	doc.setFont('Helvetica', fontSize)
	gOrigin = (100, 100)
	doc.line(gOrigin[0], gOrigin[1], gOrigin[0] + x, gOrigin[1])
	doc.line(gOrigin[0], gOrigin[1], gOrigin[0] + x, gOrigin[1] + y)
	doc.line(gOrigin[0] + x, gOrigin[1], gOrigin[0] + x, gOrigin[1] + y)

	doc.drawString(gOrigin[0] + 10, gOrigin[1] - 15, "←  Place point at center.  This edge on surface of dial")
	return doc


if __name__ == '__main__':
	lat = 44.936 # lattitude

	lineList = genLines(lat, resolution = 0.25)
	filename = 'sundial.pdf'
	pdf = genPDF(filename, lineList, lat)
	pdf.save()