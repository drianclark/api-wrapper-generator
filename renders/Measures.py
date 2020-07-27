from ObservedProperty import ObservedProperty
from ObservationType import ObservationType
from ValueStatistic import ValueStatistic

class Measures:

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, "_" + k, v)

        keys = list(dict.keys())

        try: 
            self._id = dict["@id"]
        except:
            pass
        
        if "observedProperty" in keys:
            self._observedProperty = ObservedProperty(dict["observedProperty"])
        
        if "observationType" in keys:
            self._observationType = ObservationType(dict["observationType"])
        
        if "valueStatistic" in keys:
            self._valueStatistic = ValueStatistic(dict["valueStatistic"])
        
    def label(self):
        try:
            value = self._label
        except AttributeError:
            value = None

        return value
        
        
    def observedProperty(self):
        try:
            value = self._observedProperty
        except AttributeError:
            value = None

        return value
        
        
    def qualifier(self):
        try:
            value = self._qualifier
        except AttributeError:
            value = None

        return value
        
        
    def unitName(self):
        try:
            value = self._unitName
        except AttributeError:
            value = None

        return value
        
        
    def notation(self):
        try:
            value = self._notation
        except AttributeError:
            value = None

        return value
        
        
    def period(self):
        try:
            value = self._period
        except AttributeError:
            value = None

        return value
        
        
    def valueStatistic(self):
        try:
            value = self._valueStatistic
        except AttributeError:
            value = None

        return value
        
        
    def observationType(self):
        try:
            value = self._observationType
        except AttributeError:
            value = None

        return value
        
        