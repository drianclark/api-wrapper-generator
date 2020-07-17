from renders.ObservedProperty import ObservedProperty
from renders.ValueStatistic import ValueStatistic
from renders.Station import Station
from renders.ObservationType import ObservationType

class TimeSeries:

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
        
        if "valueStatistic" in keys:
            self._valueStatistic = ValueStatistic(dict["valueStatistic"])
        
        if "station" in keys:
            self._station = Station(dict["station"])
        
        if "observationType" in keys:
            self._observationType = ObservationType(dict["observationType"])
        
    def label(self):
        try:
            value = self._label
        except AttributeError:
            value = None

        return value
        
        
    def parameter(self):
        try:
            value = self._parameter
        except AttributeError:
            value = None

        return value
        
        
    def parameterName(self):
        try:
            value = self._parameterName
        except AttributeError:
            value = None

        return value
        
        
    def qualifier(self):
        try:
            value = self._qualifier
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
        
        
    def datumType(self):
        try:
            value = self._datumType
        except AttributeError:
            value = None

        return value
        
        
    def observationType(self):
        try:
            value = self._observationType
        except AttributeError:
            value = None

        return value
        
        
    def observedProperty(self):
        try:
            value = self._observedProperty
        except AttributeError:
            value = None

        return value
        
        
    def station(self):
        try:
            value = self._station
        except AttributeError:
            value = None

        return value
        
        
    def unit(self):
        try:
            value = self._unit
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
        
        