from renders.renders import Renders

r = Renders()

def testReadings():
    data = r.readings()
    assert all(isinstance(x, Reading) for x in data)
    
def testMeasures():
    data = measures()
    assert all(isinstance(x, Measure) for x in data)
    
def testMeasuresById():
    data = measuresById()
    assert isinstance(data, Measure)
    
def testReadingsByMeasure():
    data = readingsByMeasure()
    assert isinstance(data, Reading)
    
def testStations():
    data = stations()
    assert all(isinstance(x, Station) for x in data)
    
def testStationsById():
    data = stationsById()
    assert isinstance(data, Station)
    
def testMeasuresByStation():
    data = measuresByStation()
    assert isinstance(data, Measure)
    
 