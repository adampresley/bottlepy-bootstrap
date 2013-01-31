from model.Service import Service

from datetime import tzinfo, timedelta, datetime
from dateutil import tz

class DateHelper(Service):
	utc = tz.gettz("UTC")

	pyToJsFormatMapping = {
		"%m/%d/%Y": "MM/dd/yyyy",
		"%d/%m/%Y": "dd/MM/yyyy",
		"%Y-%m-%d": "yyyy-MM-dd"
	}

	def __init__(self, db, timezone = "UTC", dateFormat = "%m/%d/%Y", timeFormat = "%I:%M %p"):
		self.db = db
		self._timezone = timezone
		self._dateFormat = dateFormat
		self._timeFormat = timeFormat

	def addDays(self, d, numDays = 1, format = "%Y-%m-%d"):
		if not self.isDateType(d):
			d = datetime.strptime(d, format)
		
		newDate = d + timedelta(days = numDays)
		return newDate

	def dateFormat(self, d):
		return self.utcToTimezone(d, self._timezone).strftime(self._dateFormat)

	def dateTimeFormat(self, d):
		return self.utcToTimezone(d, self._timezone).strftime("%s %s" % (self._dateFormat, self._timeFormat))

	def isDateType(self, d):
		result = True

		try:
			d.today()
		except AttributeError as e:
			result = False

		return result

	def localNow(self):
		return self.utcToTimezone(datetime.now(self.utc), self._timezone)

	def now(self):
		return datetime.now(self.utc)

	def pyToJsDateFormat(self, pyDateFormat):
		return self.pyToJsFormatMapping[pyDateFormat]

	def restDateFormat(self, d):
		return d.strftime("%Y-%m-%d")
		
	def restDateTime(self, d):
		return d.strftime("%Y-%m-%d %H:%M")

	def timeFormat(self, d):
		return self.utcToTimezone(d, self._timezone).strftime(self._timeFormat)

	def utcToTimezone(self, d, timezone):
		targetTZ = tz.gettz(timezone)
		d = d.replace(tzinfo = self.utc)
		return d.astimezone(targetTZ)

	def validateDateRange(self, start, end, format = "%Y-%m-%d"):
		#
		# Basically if the range between start and end is greater than 91
		# days kick it back with today's date as default.
		#
		parsedStart = datetime.strptime(start, format)
		parsedEnd = datetime.strptime(end, format)

		delta = parsedEnd - parsedStart

		newStart = start
		newEnd = end

		if delta.days > 91:
			newStart = self.restDateFormat(self.localNow())
			newEnd = self.restDateFormat(self.localNow())

		return (newStart, newEnd)
		