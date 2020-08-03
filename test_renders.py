from renders.renders import Renders
from renders.Status import Status
from renders.SampleOf import SampleOf
from renders.ObservationType import ObservationType
from renders.Reading import Reading
from renders.Station import Station
from renders.ObservedProperty import ObservedProperty
from renders.ValueStatistic import ValueStatistic
from renders.Measure import Measure


r = Renders()

def testReadings():
    data = r.readings()
    assert all(isinstance(x, Reading) for x in data)
    
def testMeasures():
    data = r.measures()
    assert all(isinstance(x, Measure) for x in data)
    
def testStations():
    data = r.stations()
    assert all(isinstance(x, Station) for x in data)
    
 