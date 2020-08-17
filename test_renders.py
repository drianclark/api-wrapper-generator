from renders.renders import Renders
from renders.SampleOf import SampleOf
from renders.Reading import Reading
from renders.ObservationType import ObservationType
from renders.ObservedProperty import ObservedProperty
from renders.ValueStatistic import ValueStatistic
from renders.Status import Status
from renders.Measure import Measure
from renders.Station import Station


r = Renders()

def testReadings():
    data = r.readings()
    assert all(isinstance(x, Reading) for x in data)
    assert all(x.value() != None for x in data)
    assert all(x.completeness() != None for x in data)
    assert all(x.dateTime() != None for x in data)
    assert all(x.qcode() != None for x in data)
    assert all(x.quality() != None for x in data)
    assert all(x.date() != None for x in data)
    
    
def testMeasures():
    data = r.measures()
    assert all(isinstance(x, Measure) for x in data)
    assert all(x.period() != None for x in data)
    assert all(x.notation() != None for x in data)
    assert all(x.parameterName() != None for x in data)
    assert all(x.unit() != None for x in data)
    assert all(x.parameter() != None for x in data)
    assert all(x.qualifier() != None for x in data)
    assert all(x.label() != None for x in data)
    assert all(x.unitName() != None for x in data)
    assert all(x.datumType() != None for x in data)
    
    
def testStations():
    data = r.stations()
    assert all(isinstance(x, Station) for x in data)
    assert all(x.riverName() != None for x in data)
    assert all(x.type() != None for x in data)
    assert all(x.nrfaStationID() != None for x in data)
    assert all(x.aquifer() != None for x in data)
    assert all(x.notation() != None for x in data)
    assert all(x.datum() != None for x in data)
    assert all(x.boreholeDepth() != None for x in data)
    assert all(x.label() != None for x in data)
    assert all(x.wiskiID() != None for x in data)
    assert all(x.RLOIid() != None for x in data)
    assert all(x.catchmentName() != None for x in data)
    assert all(x.stationReference() != None for x in data)
    assert all(x.long() != None for x in data)
    assert all(x.town() != None for x in data)
    assert all(x.easting() != None for x in data)
    assert all(x.lat() != None for x in data)
    assert all(x.nrfaStationURL() != None for x in data)
    assert all(x.northing() != None for x in data)
    assert all(x.dateOpened() != None for x in data)
    
    
 