from num2words import num2words


class TalkingClock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.minute_word = ""
        self.hour_word = ""
        self.am_or_pm = "am"
        self.separator = ""
        self.output = ""

    def get_time_in_words(self):
        self._get_minutes_and_separator()
        self._get_hour_and_am_pm()
        self._get_output()

    def _get_minutes_and_separator(self):
        if self.minute != 0:
            self.minute_word = num2words(self.minute).replace('-', ' ')

        if self.minute <= 9 and self.minute > 0:
            self.separator = 'oh'

    def _get_hour_and_am_pm(self):
        hour_diff = self.hour - 12
        if hour_diff > 0:
            self.am_or_pm = 'pm'
            self.hour_word = num2words(hour_diff)
        elif hour_diff == -12:
            self.hour_word = num2words(12)
        else:
            self.hour_word = num2words(self.hour)

    def _get_output(self):
        self.output = " ".join(filter(lambda x: x != '', ['It\'s', self.hour_word, self.separator,
                                                          self.minute_word, self.am_or_pm]))


class IO(object):
    for time in ['00:00', '01:30', '12:05', '14:01', '20:29', '21:00']:
        hour = time.split(':')[0]
        minute = time.split(':')[-1]
        tc = TalkingClock(hour=int(hour), minute=int(minute))
        tc.get_time_in_words()
        print(tc.output)
