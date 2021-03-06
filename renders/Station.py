class Station:

    def __init__(self, dict):
        from renders.SampleOf import SampleOf
        from renders.Status import Status
        from renders.Measure import Measure
        

        for k, v in dict.items():
            setattr(self, "_" + k, v)

        keys = list(dict.keys())

        try: 
            self._id = dict["@id"]
        except:
            pass
        
        if "sampleOf" in keys:
            try: 
                self._sampleOf = SampleOf(dict["sampleOf"])
            except AttributeError:
                self._sampleOf = [SampleOf(x) for x in dict["sampleOf"]]
        
        if "status" in keys:
            try: 
                self._status = Status(dict["status"])
            except AttributeError:
                self._status = [Status(x) for x in dict["status"]]
        
        if "measures" in keys:
            try: 
                self._measures = Measure(dict["measures"])
            except AttributeError:
                self._measures = [Measure(x) for x in dict["measures"]]
        
    def type(self):
        try:
            value = self._type
        except AttributeError:
            value = None

        return value
        
        
    def label(self):
        try:
            value = self._label
        except AttributeError:
            value = None

        return value
        
        
    def notation(self):
        try:
            value = self._notation
        except AttributeError:
            value = None

        return value
        
        
    def easting(self):
        try:
            value = self._easting
        except AttributeError:
            value = None

        return value
        
        
    def northing(self):
        try:
            value = self._northing
        except AttributeError:
            value = None

        return value
        
        
    def lat(self):
        try:
            value = self._lat
        except AttributeError:
            value = None

        return value
        
        
    def long(self):
        try:
            value = self._long
        except AttributeError:
            value = None

        return value
        
        
    def catchmentName(self):
        try:
            value = self._catchmentName
        except AttributeError:
            value = None

        return value
        
        
    def riverName(self):
        try:
            value = self._riverName
        except AttributeError:
            value = None

        return value
        
        
    def town(self):
        try:
            value = self._town
        except AttributeError:
            value = None

        return value
        
        
    def stationReference(self):
        try:
            value = self._stationReference
        except AttributeError:
            value = None

        return value
        
        
    def wiskiID(self):
        try:
            value = self._wiskiID
        except AttributeError:
            value = None

        return value
        
        
    def RLOIid(self):
        try:
            value = self._RLOIid
        except AttributeError:
            value = None

        return value
        
        
    def dateOpened(self):
        try:
            value = self._dateOpened
        except AttributeError:
            value = None

        return value
        
        
    def nrfaStationID(self):
        try:
            value = self._nrfaStationID
        except AttributeError:
            value = None

        return value
        
        
    def nrfaStationURL(self):
        try:
            value = self._nrfaStationURL
        except AttributeError:
            value = None

        return value
        
        
    def datum(self):
        try:
            value = self._datum
        except AttributeError:
            value = None

        return value
        
        
    def boreholeDepth(self):
        try:
            value = self._boreholeDepth
        except AttributeError:
            value = None

        return value
        
        
    def aquifer(self):
        try:
            value = self._aquifer
        except AttributeError:
            value = None

        return value
        
        
    def status(self):
        try:
            value = self._status
        except AttributeError:
            value = None

        return value
        
        
    def measures(self):
        try:
            value = self._measures
        except AttributeError:
            value = None

        return value
        
        
    def sampleOf(self):
        try:
            value = self._sampleOf
        except AttributeError:
            value = None

        return value
        
        
    def label(self):
        try:
            value = self._label
        except AttributeError:
            value = None

        return value
        
        
    def wiskiID(self):
        try:
            value = self._wiskiID
        except AttributeError:
            value = None

        return value
        
        
    def stationReference(self):
        try:
            value = self._stationReference
        except AttributeError:
            value = None

        return value
        
        
    def RLOIid(self):
        try:
            value = self._RLOIid
        except AttributeError:
            value = None

        return value
        
        