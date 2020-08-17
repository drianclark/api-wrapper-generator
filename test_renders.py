from renders.renders import Renders
from renders.Measure import Measure
from renders.SampleOf import SampleOf
from renders.ObservedProperty import ObservedProperty
from renders.Status import Status
from renders.Station import Station
from renders.ObservationType import ObservationType
from renders.ValueStatistic import ValueStatistic
from renders.Reading import Reading


r = Renders()

def testReadings():
    data = r.readings()

    assert all(isinstance(x, Reading) for x in data)
    assert all(x.dateTime() != None for x in data)
    assert all(isinstance(x.dateTime(), str) for x in data)
    assert all(x.date() != None for x in data)
    assert all(isinstance(x.date(), str) for x in data)
    assert all(x.completeness() != None for x in data)
    assert all(isinstance(x.completeness(), str) for x in data)
    assert all(x.quality() != None for x in data)
    assert all(isinstance(x.quality(), str) for x in data)

def testMeasures():
    data = r.measures()

    assert all(isinstance(x, Measure) for x in data)
    assert all(x.label() != None for x in data)
    assert all(isinstance(x.label(), str) for x in data)
    assert all(x.parameter() != None for x in data)
    assert all(isinstance(x.parameter(), str) for x in data)
    assert all(x.parameterName() != None for x in data)
    assert all(isinstance(x.parameterName(), str) for x in data)
    assert all(x.unit() != None for x in data)
    assert all(isinstance(x.unit(), str) for x in data)
    assert all(x.unitName() != None for x in data)
    assert all(isinstance(x.unitName(), str) for x in data)
    assert all(x.notation() != None for x in data)
    assert all(isinstance(x.notation(), str) for x in data)

def testStations():
    data = r.stations()

    assert all(isinstance(x, Station) for x in data)
    assert all(x.type() != None for x in data)
    assert all(x.label() != None for x in data)
    assert all(isinstance(x.label(), str) for x in data)
    assert all(x.notation() != None for x in data)
    assert all(isinstance(x.notation(), str) for x in data)
    assert all(x.easting() != None for x in data)
    assert all(isinstance(x.easting(), str) for x in data)
    assert all(x.northing() != None for x in data)
    assert all(isinstance(x.northing(), str) for x in data)
    assert all(x.lat() != None for x in data)
    assert all(isinstance(x.lat(), str) for x in data)
    assert all(x.long() != None for x in data)
    assert all(isinstance(x.long(), str) for x in data)

 