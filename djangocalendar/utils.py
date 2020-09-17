from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from test.models import Data

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += f'<div style="padding:3px;margin-bottom:3px;background-color:#F3A712;border-radius:15px;border:1px solid purple"> {event.get_html_url}</div>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True,user=None):
		accepted_forms = []

		all_data = Data.objects.filter(user=user,status='ACCEPTED')
		for a_data in all_data:
			accepted_forms.append(a_data)

		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month,user=user)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal