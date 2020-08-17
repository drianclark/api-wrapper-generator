class Measure:

    def __init__(self, dict):
        from renders.Station import Station
        from renders.ObservationType import ObservationType
        from renders.ValueStatistic import ValueStatistic
        from renders.ObservedProperty import ObservedProperty
        

        for k, v in dict.items():
            setattr(self, "_" + k, v)

        keys = list(dict.keys())

        try: 
            self._id = dict["@id"]
        except:
            pass
        
        if "station" in keys:
            try: 
                self._station = Station(dict["station"])
            except AttributeError:
                self._station = [Station(x) for x in dict["station"]]
        
        if "observationType" in keys:
            try: 
                self._observationType = ObservationType(dict["observationType"])
            except AttributeError:
                self._observationType = [ObservationType(x) for x in dict["observationType"]]
        
        if "valueStatistic" in keys:
            try: 
                self._valueStatistic = ValueStatistic(dict["valueStatistic"])
            except AttributeError:
                self._valueStatistic = [ValueStatistic(x) for x in dict["valueStatistic"]]
        
        if "observedProperty" in keys:
            try: 
                self._observedProperty = ObservedProperty(dict["observedProperty"])
            except AttributeError:
                self._observedProperty = [ObservedProperty(x) for x in dict["observedProperty"]]
        
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
        
        