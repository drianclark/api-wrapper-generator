from renders.renders import Renders
from renders.ObservationType import ObservationType
from renders.Measure import Measure
from renders.Reading import Reading
from renders.SampleOf import SampleOf
from renders.ObservedProperty import ObservedProperty
from renders.ValueStatistic import ValueStatistic
from renders.Status import Status
from renders.Station import Station


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

    except ValueError:
        print('Invalid http request for prop value')
    try:
        dataWithqcode = r.readings(exists=['qcode'], limit=1)[0]
        assert (dataWithqcode.qcode() != None)
        assert isinstance(dataWithqcode.qcode(), str)

    except IndexError:
        print('No data found with prop qcode')

    except ValueError:
        print('Invalid http request for prop qcode')
        

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
    try:
        assert all(isinstance(x.unit(), Unit) for x in data)
    except NameError:
        assert all(isinstance(x.unit(), dict) for x in data)
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

    except ValueError:
        print('Invalid http request for prop qualifier')
    try:
        dataWithperiod = r.measures(exists=['period'], limit=1)[0]
        assert (dataWithperiod.period() != None)
        assert isinstance(dataWithperiod.period(), (int, float))

    except IndexError:
        print('No data found with prop period')

    except ValueError:
        print('Invalid http request for prop period')
    try:
        dataWithdatumType = r.measures(exists=['datumType'], limit=1)[0]
        assert (dataWithdatumType.datumType() != None)
        assert isinstance(dataWithdatumType.datumType(), str)

    except IndexError:
        print('No data found with prop datumType')

    except ValueError:
        print('Invalid http request for prop datumType')
    try:
        dataWithvalueStatisticlabel = r.measures(limit=1)[0]
        assert (dataWithvalueStatisticlabel.valueStatistic().label() != None)
        assert isinstance(dataWithvalueStatisticlabel.valueStatistic().label(), str)
        
    except IndexError:
        print('No data found with prop valueStatisticlabel')
    try:
        dataWithobservationTypelabel = r.measures(limit=1)[0]
        assert (dataWithobservationTypelabel.observationType().label() != None)
        assert isinstance(dataWithobservationTypelabel.observationType().label(), str)
        
    except IndexError:
        print('No data found with prop observationTypelabel')
    try:
        dataWithobservedPropertylabel = r.measures(limit=1)[0]
        assert (dataWithobservedPropertylabel.observedProperty().label() != None)
        assert isinstance(dataWithobservedPropertylabel.observedProperty().label(), str)
        
    except IndexError:
        print('No data found with prop observedPropertylabel')
    try:
        dataWithstationlabel = r.measures(limit=1)[0]
        assert (dataWithstationlabel.station().label() != None)
        assert isinstance(dataWithstationlabel.station().label(), str)
        
    except IndexError:
        print('No data found with prop stationlabel')
    try:
        dataWithstationwiskiID = r.measures(exists=['stationwiskiID'], limit=1)[0]
        assert (dataWithstationwiskiID.station().wiskiID() != None)
        assert isinstance(dataWithstationwiskiID.station().wiskiID(), str)
    except IndexError:
        print('No data found with prop stationwiskiID')

    except ValueError:
        print('Invalid http request for prop stationwiskiID')
    
    try:
        dataWithstationstationReference = r.measures(exists=['stationstationReference'], limit=1)[0]
        assert (dataWithstationstationReference.station().stationReference() != None)
        assert isinstance(dataWithstationstationReference.station().stationReference(), str)
    except IndexError:
        print('No data found with prop stationstationReference')

    except ValueError:
        print('Invalid http request for prop stationstationReference')
    
    try:
        dataWithstationRLOIid = r.measures(exists=['stationRLOIid'], limit=1)[0]
        assert (dataWithstationRLOIid.station().RLOIid() != None)
        assert isinstance(dataWithstationRLOIid.station().RLOIid(), str)
    except IndexError:
        print('No data found with prop stationRLOIid')

    except ValueError:
        print('Invalid http request for prop stationRLOIid')
    
        

def testStations():
    data = r.stations()

    assert all(isinstance(x, Station) for x in data)
    assert all(x.type() != None for x in data)
    assert all(x.label() != None for x in data)
    assert all(isinstance(x.label(), str) for x in data)
    assert all(x.notation() != None for x in data)
    assert all(isinstance(x.notation(), str) for x in data)
    assert all(x.easting() != None for x in data)
    assert all(isinstance(x.easting(), (int, float)) for x in data)
    assert all(x.northing() != None for x in data)
    assert all(isinstance(x.northing(), (int, float)) for x in data)
    assert all(x.lat() != None for x in data)
    assert all(isinstance(x.lat(), (int, float)) for x in data)
    assert all(x.long() != None for x in data)
    assert all(isinstance(x.long(), (int, float)) for x in data)

    
    try:
        dataWithcatchmentName = r.stations(exists=['catchmentName'], limit=1)[0]
        assert (dataWithcatchmentName.catchmentName() != None)
        assert isinstance(dataWithcatchmentName.catchmentName(), str)

    except IndexError:
        print('No data found with prop catchmentName')

    except ValueError:
        print('Invalid http request for prop catchmentName')
    try:
        dataWithriverName = r.stations(exists=['riverName'], limit=1)[0]
        assert (dataWithriverName.riverName() != None)
        assert isinstance(dataWithriverName.riverName(), str)

    except IndexError:
        print('No data found with prop riverName')

    except ValueError:
        print('Invalid http request for prop riverName')
    try:
        dataWithtown = r.stations(exists=['town'], limit=1)[0]
        assert (dataWithtown.town() != None)
        assert isinstance(dataWithtown.town(), str)

    except IndexError:
        print('No data found with prop town')

    except ValueError:
        print('Invalid http request for prop town')
    try:
        dataWithstationReference = r.stations(exists=['stationReference'], limit=1)[0]
        assert (dataWithstationReference.stationReference() != None)
        assert isinstance(dataWithstationReference.stationReference(), str)

    except IndexError:
        print('No data found with prop stationReference')

    except ValueError:
        print('Invalid http request for prop stationReference')
    try:
        dataWithwiskiID = r.stations(exists=['wiskiID'], limit=1)[0]
        assert (dataWithwiskiID.wiskiID() != None)
        assert isinstance(dataWithwiskiID.wiskiID(), str)

    except IndexError:
        print('No data found with prop wiskiID')

    except ValueError:
        print('Invalid http request for prop wiskiID')
    try:
        dataWithRLOIid = r.stations(exists=['RLOIid'], limit=1)[0]
        assert (dataWithRLOIid.RLOIid() != None)
        assert isinstance(dataWithRLOIid.RLOIid(), str)

    except IndexError:
        print('No data found with prop RLOIid')

    except ValueError:
        print('Invalid http request for prop RLOIid')
    try:
        dataWithdateOpened = r.stations(exists=['dateOpened'], limit=1)[0]
        assert (dataWithdateOpened.dateOpened() != None)
        assert isinstance(dataWithdateOpened.dateOpened(), str)

    except IndexError:
        print('No data found with prop dateOpened')

    except ValueError:
        print('Invalid http request for prop dateOpened')
    try:
        dataWithnrfaStationID = r.stations(exists=['nrfaStationID'], limit=1)[0]
        assert (dataWithnrfaStationID.nrfaStationID() != None)
        assert isinstance(dataWithnrfaStationID.nrfaStationID(), str)

    except IndexError:
        print('No data found with prop nrfaStationID')

    except ValueError:
        print('Invalid http request for prop nrfaStationID')
    try:
        dataWithnrfaStationURL = r.stations(exists=['nrfaStationURL'], limit=1)[0]
        assert (dataWithnrfaStationURL.nrfaStationURL() != None)
        assert isinstance(dataWithnrfaStationURL.nrfaStationURL(), str)

    except IndexError:
        print('No data found with prop nrfaStationURL')

    except ValueError:
        print('Invalid http request for prop nrfaStationURL')
    try:
        dataWithdatum = r.stations(exists=['datum'], limit=1)[0]
        assert (dataWithdatum.datum() != None)
        assert isinstance(dataWithdatum.datum(), (int, float))

    except IndexError:
        print('No data found with prop datum')

    except ValueError:
        print('Invalid http request for prop datum')
    try:
        dataWithboreholeDepth = r.stations(exists=['boreholeDepth'], limit=1)[0]
        assert (dataWithboreholeDepth.boreholeDepth() != None)
        assert isinstance(dataWithboreholeDepth.boreholeDepth(), (int, float))

    except IndexError:
        print('No data found with prop boreholeDepth')

    except ValueError:
        print('Invalid http request for prop boreholeDepth')
    try:
        dataWithaquifer = r.stations(exists=['aquifer'], limit=1)[0]
        assert (dataWithaquifer.aquifer() != None)
        assert isinstance(dataWithaquifer.aquifer(), str)

    except IndexError:
        print('No data found with prop aquifer')

    except ValueError:
        print('Invalid http request for prop aquifer')
    try:
        dataWithmeasureslabel = r.stations(limit=1)[0]
        assert (dataWithmeasureslabel.measures().label() != None)
        assert isinstance(dataWithmeasureslabel.measures().label(), str)
        
    except IndexError:
        print('No data found with prop measureslabel')
    try:
        dataWithmeasuresobservedPropertylabel = r.stations(limit=1)[0]
        assert (dataWithmeasuresobservedPropertylabel.measures().observedProperty().label() != None)
        assert isinstance(dataWithmeasuresobservedPropertylabel.measures().observedProperty().label(), str)
        
    except IndexError:
        print('No data found with prop measuresobservedPropertylabel')
    try:
        dataWithmeasuresunitName = r.stations(limit=1)[0]
        assert (dataWithmeasuresunitName.measures().unitName() != None)
        assert isinstance(dataWithmeasuresunitName.measures().unitName(), str)
        
    except IndexError:
        print('No data found with prop measuresunitName')
    try:
        dataWithmeasuresnotation = r.stations(limit=1)[0]
        assert (dataWithmeasuresnotation.measures().notation() != None)
        assert isinstance(dataWithmeasuresnotation.measures().notation(), str)
        
    except IndexError:
        print('No data found with prop measuresnotation')
    try:
        dataWithmeasuresvalueStatisticlabel = r.stations(limit=1)[0]
        assert (dataWithmeasuresvalueStatisticlabel.measures().valueStatistic().label() != None)
        assert isinstance(dataWithmeasuresvalueStatisticlabel.measures().valueStatistic().label(), str)
        
    except IndexError:
        print('No data found with prop measuresvalueStatisticlabel')
    try:
        dataWithmeasuresobservationTypelabel = r.stations(limit=1)[0]
        assert (dataWithmeasuresobservationTypelabel.measures().observationType().label() != None)
        assert isinstance(dataWithmeasuresobservationTypelabel.measures().observationType().label(), str)
        
    except IndexError:
        print('No data found with prop measuresobservationTypelabel')
    try:
        dataWithsampleOflabel = r.stations(limit=1)[0]
        assert (dataWithsampleOflabel.sampleOf().label() != None)
        assert isinstance(dataWithsampleOflabel.sampleOf().label(), str)
        
    except IndexError:
        print('No data found with prop sampleOflabel')
    try:
        dataWithstatuslabel = r.stations(exists=['statuslabel'], limit=1)[0]
        assert (dataWithstatuslabel.status().label() != None)
        assert isinstance(dataWithstatuslabel.status().label(), str)
    except IndexError:
        print('No data found with prop statuslabel')

    except ValueError:
        print('Invalid http request for prop statuslabel')
    
    try:
        dataWithmeasuresqualifier = r.stations(exists=['measuresqualifier'], limit=1)[0]
        assert (dataWithmeasuresqualifier.measures().qualifier() != None)
        assert isinstance(dataWithmeasuresqualifier.measures().qualifier(), str)
    except IndexError:
        print('No data found with prop measuresqualifier')

    except ValueError:
        print('Invalid http request for prop measuresqualifier')
    
    try:
        dataWithmeasuresperiod = r.stations(exists=['measuresperiod'], limit=1)[0]
        assert (dataWithmeasuresperiod.measures().period() != None)
        assert isinstance(dataWithmeasuresperiod.measures().period(), (int, float)) 
        
    except IndexError:
        print('No data found with prop measuresperiod')

    except ValueError:
        print('Invalid http request for prop measuresperiod')
    
        

 