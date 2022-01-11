from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import Flowable
from reportlab.lib import colors

import math
import csv

# data = []
# with open('time_table.csv', newline='') as csvfile:
# 	spamreader = csv.reader(csvfile)
# 	for row in spamreader:
# 		data.append(row)

# print(data)

timeData = [
['Day', 'Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
['1', '-3:12', '-13:33', '-12:34', '-4:08', '+2:51', '+2:25', '-3:33', '-6:16', '-0:12', '+10:05', '+16:20', '+11:11'],
['2', '-3:40', '-13:41', '-12:23', '-3:50', '+2:59', '+2:16', '-3:45', '-6:13', '+0:07', '+10:24', '+16:22', '+10:49'],
['3', '-4:08', '-13:48', '-12:11', '-3:32', '+3:06', '+2:06', '-3:57', '-6:09', '+0:26', '+10:43', '+16:23', '+10:26'],
['4', '-4:36', '-13:55', '-11:58', '-3:14', '+3:12', '+1:56', '-4:08', '-6:04', '-0:45', '+11:02', '+16:23', '+10:02'],
['5', '-5:03', '-14:01', '-11:45', '-2:57', '+3:18', '+1:46', '-4:19', '-5:59', '-1:05', '+11:20', '+16:22', '+9:38'],
['6', '-5:30', '-14:06', '-11:31', '-2:40', '+3:23', '+1:36', '-4:29', '-5:53', '+1:25', '+11:38', '+16:20', '+9:13'],
['7', '-5:57', '-14:10', '-11:17', '-2:23', '+3:27', '+1:25', '-4:39', '-5:46', '+1:45', '+11:56', '+16:18', '+8:48'], 
['8', '-6:23', '-14:14', '-11:03', '-2:06', '+3:31', '+1:14', '-4:49', '-5:39', '+2:05', '+12:13', '+16:15', '+8:22'],
['9', '-6:49', '-14:16', '-10:48', '-1:49', '+3:35', '+1:03', '-4:58', '-5:31', '+2:26', '+12:30', '+16:11', '+7:56'],
['10', '-7:14', '-14:18', '-10:33', '-1:32', '+3:38', '+0:51', '-5:07', '-5:23', '+2:47', '+12:46', '+16:06', '+7:29'],
['11', '-7:38', '-14:19', '-10:18', '-1:16', '+3:40', '+0:39', '-5:16', '-5:14', '+3:08', '+13:02', '+16:00', '+7:02'],
['12', '-8:02', '-14:20', '-10:02', '-1:00', '+3:42', '+0:27', '-5:24', '-5:05', '+3:29', '+13:18', '+15:53', '+6:34'],
['13', '-8:25', '-14:19', '-9:46', '-0:44', '+3:44', '+0:15', '-5:32', '-4:55', '+3:50', '+13:33', '+15:46', '+6:06'],
['14', '-8:48', '-14:18', '-9:30', '-0:29', '+3:44', '+0:03', '-5:39', '-4:44', '+4:11', '+13:47', '+15:37', '+5:38'],
['15', '-9:10', '-14:16', '-9:13', '-0:14', '+3:44', '-0:10', '-5:46', '-4:33', '+4:32', '+14:01', '+15:28', '+5:09'],
['16', '-9:32', '-14:13', '-8:56', '+0:01', '+3:44', '-0:23', '-5:52', '-4:21', '+4:53', '+14:14', '+15:18', '+4:40'],
['17', '-9:52', '-14:10', '-8:39', '+0:15', '+3:43', '-0:36', '-5:58', '-4:09', '+5:14', '+14:27', '+15:07', '+4:11'],
['18', '-10:12', '-14:06', '-8:22', '+0:29', '+3:41', '-0:49', '-6:03', '-3:57', '+5:35', '+14:39', '+14:56', '+3:42'],
['19', '-10:32', '-14:01', '-8:04', '+0:43', '+3:39', '-1:02', '-6:08', '-3:44', '+5:56', '+14:51', '+14:43', '+3:13'],
['20', '-10:50', '-13:55', '-7:46', '+0:56', '+3:37', '-1:15', '-6:12', '-3:30', '+6:18', '+15:02', '+14:30', '+2:43'],
['21', '-11:08', '-13:49', '-7:28', '+1:00', '+3:34', '-1:28', '-6:15', '-3:16', '+6:40', '+15:12', '+14:16', '+2:13'],
['22', '-11:25', '-13:42', '-7:10', '+1:21', '+3:30', '-1:41', '-6:18', '-3:01', '+7:01', '+15:22', '+14:01', '+1:43'],
['23', '-11:41', '-13:35', '-6:52', '+1:33', '+3:24', '-1:54', '-6:20', '-2:46', '+7:22', '+15:31', '+13:45', '+1:13'],
['24', '-11:57', '-13:27', '-6:34', '+1:45', '+3:21', '-2:07', '-6:22', '-2:30', '+7:43', '+15:40', '+13:28', '+0:43'],
['25', '-12:12', '-13:18', '-6:16', '+1:56', '+3:16', '-2:20', '-6:24', '-2:14', '+8:04', '+15:47', '+13:11', '+0:13'],
['26', '-12:26', '-13:09', '-5:58', '+2:06', '+3:10', '-2:33', '-6:25', '-1:58', '+8:25', '+15:54', '+12:53', '-0:17'],
['27', '-12:39', '-12:59', '-5:40', '+2:16', '+3:03', '-2:45', '-6:25', '-1:41', '+8:46', '+16:01', '+12:34', '-0:47'],
['28', '-12:51', '-12:48', '-5:21', '+2:26', '+2:56', '-2:57', '-6:24', '-1:24', '+9:06', '+16:06', '+12:14', '-1:16'],
['29', '-13:03', '-12:42', '-5:02', '+2:35', '+2:49', '-3:09', '-6:23', '-1:07', '+9:26', '+16:11', '+11:54', '-1:45'],
['30', '-13:14', 'N/A', '-4:44', '+2:43', '+2:41', '-3:21', '-6:21', '-0:49', '+9:46', '+16:15', '+11:33', '-2:14'],
['31', '-13:24', 'N/A', '-4:26', 'N/A', '+2:33', 'N/A', '-6:19', '-0:31', 'N/A', '+16:18', 'N/A', '-2:43']]

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

# class flowable_fig(Flowable):
#     def __init__(self, imgdata):
#         reportlab.platypus.Flowable.__init__(self)
#         self.img = reportlab.lib.utils.ImageReader(imgdata)

#     def draw(self):
#         self.canv.drawImage(self.img, 0, 0, height = -2*inch, width=4*inch)
#         # http://www.reportlab.com/apis/reportlab/2.4/pdfgen.html

class Flowable_Canvas(Flowable):
	def __init__(self, canvas):
		Flowable.__init__(self)
		self.canvas = canvas

	def draw(self):
		self.canv.draw()

	
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


	doc.showPage() # page break
	
	# insert time adjustment values for each day of the year (hard-coded table)
	t = Table(timeData)
	t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.25, colors.black)]))

	#alternating colors
	for row in range(len(timeData)):
		if row % 2 == 0:	bg_color = colors.whitesmoke
		else: 				bg_color = colors.lightgrey
		t.setStyle(TableStyle([('BACKGROUND', (0, row), (-1, row), bg_color)]))

	t.setStyle(TableStyle([('FONT', (0, 0), (-1, 0), 'Helvetica-Bold')])) # header row bold

	t.wrapOn(doc, 400, 400)
	tableLoc = ((_w - t.minWidth())/2, (_h - t._height)/2)
	t.drawOn(doc, tableLoc[0], tableLoc[1])

	return doc


if __name__ == '__main__':
	lat = 44.936 # lattitude

	lineList = genLines(lat, resolution = 0.5)
	filename = 'sundial.pdf'
	pdf = genPDF(filename, lineList, lat)
	pdf.save()