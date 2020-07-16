class Reading:

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, "_" + k, v)

        keys = list(dict.keys())

        try: 
            self._id = dict["@id"]
        except:
            pass
        
    def measure(self):
        try:
            value = self._measure["@id"]
        except AttributeError:
            value = None

        return value
            
        
    def dateTime(self):
        try:
            value = self._dateTime
        except AttributeError:
            value = None

        return value
        
        
    def date(self):
        try:
            value = self._date
        except AttributeError:
            value = None

        return value
        
        
    def value(self):
        try:
            value = self._value
        except AttributeError:
            value = None

        return value
        
        
    def completeness(self):
        try:
            value = self._completeness
        except AttributeError:
            value = None

        return value
        
        
    def quality(self):
        try:
            value = self._quality
        except AttributeError:
            value = None

        return value
        
        
    def qcode(self):
        try:
            value = self._qcode
        except AttributeError:
            value = None

        return value
        
        
    def valid(self):
        try:
            value = self._valid
        except AttributeError:
            value = None

        return value
        
        
    def invalid(self):
        try:
            value = self._invalid
        except AttributeError:
            value = None

        return value
        
        
    def missing(self):
        try:
            value = self._missing
        except AttributeError:
            value = None

        return value
        
        