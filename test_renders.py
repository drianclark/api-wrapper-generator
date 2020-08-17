from renders.renders import Renders
from renders.ValueStatistic import ValueStatistic
from renders.SampleOf import SampleOf
from renders.Status import Status
from renders.ObservationType import ObservationType
from renders.Reading import Reading
from renders.Measure import Measure
from renders.Station import Station
from renders.ObservedProperty import ObservedProperty


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

    
    try:
        dataWithvalue = r.readings(exists=['value'], limit=1)[0]
        assert (dataWithvalue.value() != None)
        assert isinstance(dataWithvalue.value(), (int, float))
    except IndexError:
        print('No data found with prop value')
    
    try:
        dataWithqcode = r.readings(exists=['qcode'], limit=1)[0]
        assert (dataWithqcode.qcode() != None)
        assert isinstance(dataWithqcode.qcode(), str)
    except IndexError:
        print('No data found with prop qcode')
    

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
    # assert all(isinstance(x.unit(), str) for x in data)
    assert all(x.unitName() != None for x in data)
    assert all(isinstance(x.unitName(), str) for x in data)
    assert all(x.notation() != None for x in data)
    assert all(isinstance(x.notation(), str) for x in data)

    
    try:
        dataWithqualifier = r.measures(exists=['qualifier'], limit=1)[0]
        assert (dataWithqualifier.qualifier() != None)
        assert isinstance(dataWithqualifier.qualifier(), str)
    except IndexError:
        print('No data found with prop qualifier')
    
    try:
        dataWithperiod = r.measures(exists=['period'], limit=1)[0]
        assert (dataWithperiod.period() != None)
        assert isinstance(dataWithperiod.period(), (int, float))
    except IndexError:
        print('No data found with prop period')
    
    try:
        dataWithdatumType = r.measures(exists=['datumType'], limit=1)[0]
        assert (dataWithdatumType.datumType() != None)
        assert isinstance(dataWithdatumType.datumType(), str)
    except IndexError:
        print('No data found with prop datumType')
    

def testStations():
    data = r.stations()

    assert all(isinstance(x, Station) for x in data)
    assert all(x.type() != None for x in data)
    assert all(x.label() != None for x in data)
    assert all(isinstance(x.label(), str) for x in data)
    assert all(x.notation() != None for x in data)
    assert all(isinstance(x.notation(), str) for x in data)
    # assert all(x.easting() != None for x in data)
    # assert all(isinstance(x.easting(), str) for x in data)
    # assert all(x.northing() != None for x in data)
    # assert all(isinstance(x.northing(), str) for x in data)
    # assert all(x.lat() != None for x in data)
    # assert all(isinstance(x.lat(), str) for x in data)
    # assert all(x.long() != None for x in data)
    # assert all(isinstance(x.long(), str) for x in data)

    
    try:
        dataWithcatchmentName = r.stations(exists=['catchmentName'], limit=1)[0]
        assert (dataWithcatchmentName.catchmentName() != None)
        assert isinstance(dataWithcatchmentName.catchmentName(), str)
    except IndexError:
        print('No data found with prop catchmentName')
    
    try:
        dataWithriverName = r.stations(exists=['riverName'], limit=1)[0]
        assert (dataWithriverName.riverName() != None)
        assert isinstance(dataWithriverName.riverName(), str)
    except IndexError:
        print('No data found with prop riverName')
    
    try:
        dataWithtown = r.stations(exists=['town'], limit=1)[0]
        assert (dataWithtown.town() != None)
        assert isinstance(dataWithtown.town(), str)
    except IndexError:
        print('No data found with prop town')
    
    try:
        dataWithstationReference = r.stations(exists=['stationReference'], limit=1)[0]
        assert (dataWithstationReference.stationReference() != None)
        assert isinstance(dataWithstationReference.stationReference(), str)
    except IndexError:
        print('No data found with prop stationReference')
    
    try:
        dataWithwiskiID = r.stations(exists=['wiskiID'], limit=1)[0]
        assert (dataWithwiskiID.wiskiID() != None)
        assert isinstance(dataWithwiskiID.wiskiID(), str)
    except IndexError:
        print('No data found with prop wiskiID')
    
    try:
        dataWithRLOIid = r.stations(exists=['RLOIid'], limit=1)[0]
        assert (dataWithRLOIid.RLOIid() != None)
        assert isinstance(dataWithRLOIid.RLOIid(), str)
    except IndexError:
        print('No data found with prop RLOIid')
    
    try:
        dataWithdateOpened = r.stations(exists=['dateOpened'], limit=1)[0]
        assert (dataWithdateOpened.dateOpened() != None)
        assert isinstance(dataWithdateOpened.dateOpened(), str)
    except IndexError:
        print('No data found with prop dateOpened')
    
    try:
        dataWithnrfaStationID = r.stations(exists=['nrfaStationID'], limit=1)[0]
        assert (dataWithnrfaStationID.nrfaStationID() != None)
        assert isinstance(dataWithnrfaStationID.nrfaStationID(), str)
    except IndexError:
        print('No data found with prop nrfaStationID')
    
    try:
        dataWithnrfaStationURL = r.stations(exists=['nrfaStationURL'], limit=1)[0]
        assert (dataWithnrfaStationURL.nrfaStationURL() != None)
        assert isinstance(dataWithnrfaStationURL.nrfaStationURL(), str)
    except IndexError:
        print('No data found with prop nrfaStationURL')
    
    # try:
    #     dataWithdatum = r.stations(exists=['datum'], limit=1)[0]
    #     assert (dataWithdatum.datum() != None)
    #     assert isinstance(dataWithdatum.datum(), (int, float))
    # except IndexError:
    #     print('No data found with prop datum')
    
    try:
        dataWithboreholeDepth = r.stations(exists=['boreholeDepth'], limit=1)[0]
        assert (dataWithboreholeDepth.boreholeDepth() != None)
        assert isinstance(dataWithboreholeDepth.boreholeDepth(), (int, float))
    except IndexError:
        print('No data found with prop boreholeDepth')
    
    try:
        dataWithaquifer = r.stations(exists=['aquifer'], limit=1)[0]
        assert (dataWithaquifer.aquifer() != None)
        assert isinstance(dataWithaquifer.aquifer(), str)
    except IndexError:
        print('No data found with prop aquifer')
    

 