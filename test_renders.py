from renders.renders import Renders
from renders.Station import Station
from renders.Measure import Measure
from renders.Reading import Reading

r = Renders()

def testReadings():
    data = r.readings()
    assert all(isinstance(x, Reading) for x in data)
    
def testMeasures():
    data = r.measures()
    assert all(isinstance(x, Measure) for x in data)
    
def testMeasuresById():
    data = r.measuresById()
    assert isinstance(data, Measure)
    
def testReadingsByMeasure():
    data = r.readingsByMeasure()
    assert isinstance(data, Reading)
    
def testStations():
    data = r.stations()
    assert all(isinstance(x, Station) for x in data)
    
def testStationsById():
    data = r.stationsById()
    assert isinstance(data, Station)
    
def testMeasuresByStation():
    data = r.measuresByStation()
    assert isinstance(data, Measure)
    
 