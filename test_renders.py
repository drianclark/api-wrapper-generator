from renders.renders import Renders
from renders.ObservationType import ObservationType
from renders.ObservedProperty import ObservedProperty
from renders.SampleOf import SampleOf
from renders.ValueStatistic import ValueStatistic
from renders.Station import Station
from renders.Reading import Reading
from renders.Status import Status
from renders.Measure import Measure


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
        dataWithvalueStatisticlabel = r.measures(exists=['valueStatistic'], limit=1)[0]
        assert (dataWithvalueStatisticlabel.valueStatistic().label() != None)
        assert isinstance(dataWithvalueStatisticlabel.valueStatistic().label(), str)
        
    except IndexError:
        print('No data found with prop valueStatistic.label')
    
    except ValueError:
        print('Invalid http request for prop valueStatistic.label')

    except AttributeError:
        try:
            if isinstance(dataWithvalueStatisticlabel.valueStatistic(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithvalueStatisticlabel.valueStatistic())
        except AttributeError: 
            print('valueStatistic.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('valueStatistic.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithobservationTypelabel = r.measures(exists=['observationType'], limit=1)[0]
        assert (dataWithobservationTypelabel.observationType().label() != None)
        assert isinstance(dataWithobservationTypelabel.observationType().label(), str)
        
    except IndexError:
        print('No data found with prop observationType.label')
    
    except ValueError:
        print('Invalid http request for prop observationType.label')

    except AttributeError:
        try:
            if isinstance(dataWithobservationTypelabel.observationType(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithobservationTypelabel.observationType())
        except AttributeError: 
            print('observationType.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('observationType.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithobservedPropertylabel = r.measures(exists=['observedProperty'], limit=1)[0]
        assert (dataWithobservedPropertylabel.observedProperty().label() != None)
        assert isinstance(dataWithobservedPropertylabel.observedProperty().label(), str)
        
    except IndexError:
        print('No data found with prop observedProperty.label')
    
    except ValueError:
        print('Invalid http request for prop observedProperty.label')

    except AttributeError:
        try:
            if isinstance(dataWithobservedPropertylabel.observedProperty(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithobservedPropertylabel.observedProperty())
        except AttributeError: 
            print('observedProperty.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('observedProperty.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithstationlabel = r.measures(exists=['station'], limit=1)[0]
        assert (dataWithstationlabel.station().label() != None)
        assert isinstance(dataWithstationlabel.station().label(), str)
        
    except IndexError:
        print('No data found with prop station.label')
    
    except ValueError:
        print('Invalid http request for prop station.label')

    except AttributeError:
        try:
            if isinstance(dataWithstationlabel.station(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithstationlabel.station())
        except AttributeError: 
            print('station.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('station.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithstationwiskiID = r.measures(exists=['station.wiskiID'], limit=1)[0]
        assert (dataWithstationwiskiID.station().wiskiID() != None)
        assert isinstance(dataWithstationwiskiID.station().wiskiID(), str)
        
    except IndexError:
        print('No data found with prop station.wiskiID')

    except ValueError:
        print('Invalid http request for prop stationwiskiID')

    except AttributeError:
        try:
            assert all(isinstance(x.wiskiID(), str) for x in dataWithstationwiskiID.station())
        except AttributeError: 
            print('station.wiskiID: AttributeError most likely due to array wrongly specified as object in spec')
    
    try:
        dataWithstationstationReference = r.measures(exists=['station.stationReference'], limit=1)[0]
        assert (dataWithstationstationReference.station().stationReference() != None)
        assert isinstance(dataWithstationstationReference.station().stationReference(), str)
        
    except IndexError:
        print('No data found with prop station.stationReference')

    except ValueError:
        print('Invalid http request for prop stationstationReference')

    except AttributeError:
        try:
            assert all(isinstance(x.stationReference(), str) for x in dataWithstationstationReference.station())
        except AttributeError: 
            print('station.stationReference: AttributeError most likely due to array wrongly specified as object in spec')
    
    try:
        dataWithstationRLOIid = r.measures(exists=['station.RLOIid'], limit=1)[0]
        assert (dataWithstationRLOIid.station().RLOIid() != None)
        assert isinstance(dataWithstationRLOIid.station().RLOIid(), str)
        
    except IndexError:
        print('No data found with prop station.RLOIid')

    except ValueError:
        print('Invalid http request for prop stationRLOIid')

    except AttributeError:
        try:
            assert all(isinstance(x.RLOIid(), str) for x in dataWithstationRLOIid.station())
        except AttributeError: 
            print('station.RLOIid: AttributeError most likely due to array wrongly specified as object in spec')
    

def testStations():
    data = r.stations()

    assert all(isinstance(x, Station) for x in data)

    assert all(x.type() != None for x in data)
    try:
        assert all(isinstance(x.type(), list) for x in data)
    except NameError:
        assert all(isinstance(x.type(), dict) for x in data)
    

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
        dataWithmeasureslabel = r.stations(exists=['measures'], limit=1)[0]
        assert (dataWithmeasureslabel.measures().label() != None)
        assert isinstance(dataWithmeasureslabel.measures().label(), str)
        
    except IndexError:
        print('No data found with prop measures.label')
    
    except ValueError:
        print('Invalid http request for prop measures.label')

    except AttributeError:
        try:
            if isinstance(dataWithmeasureslabel.measures(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithmeasureslabel.measures())
        except AttributeError: 
            print('measures.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('measures.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithmeasuresobservedPropertylabel = r.stations(exists=['measures.observedProperty'], limit=1)[0]
        assert (dataWithmeasuresobservedPropertylabel.measures().observedProperty().label() != None)
        assert isinstance(dataWithmeasuresobservedPropertylabel.measures().observedProperty().label(), str)
        
    except IndexError:
        print('No data found with prop measures.observedProperty.label')
    
    except ValueError:
        print('Invalid http request for prop measures.observedProperty.label')

    except AttributeError:
        try:
            if isinstance(dataWithmeasuresobservedPropertylabel.measures().observedProperty(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithmeasuresobservedPropertylabel.measures().observedProperty())
        except AttributeError: 
            print('measures.observedProperty.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('measures.observedProperty.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithmeasuresunitName = r.stations(exists=['measures'], limit=1)[0]
        assert (dataWithmeasuresunitName.measures().unitName() != None)
        assert isinstance(dataWithmeasuresunitName.measures().unitName(), str)
        
    except IndexError:
        print('No data found with prop measures.unitName')
    
    except ValueError:
        print('Invalid http request for prop measures.unitName')

    except AttributeError:
        try:
            if isinstance(dataWithmeasuresunitName.measures(), list):    
                assert all(isinstance(x.unitName(), str) for x in dataWithmeasuresunitName.measures())
        except AttributeError: 
            print('measures.unitName: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('measures.unitName: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithmeasuresnotation = r.stations(exists=['measures'], limit=1)[0]
        assert (dataWithmeasuresnotation.measures().notation() != None)
        assert isinstance(dataWithmeasuresnotation.measures().notation(), str)
        
    except IndexError:
        print('No data found with prop measures.notation')
    
    except ValueError:
        print('Invalid http request for prop measures.notation')

    except AttributeError:
        try:
            if isinstance(dataWithmeasuresnotation.measures(), list):    
                assert all(isinstance(x.notation(), str) for x in dataWithmeasuresnotation.measures())
        except AttributeError: 
            print('measures.notation: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('measures.notation: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithmeasuresvalueStatisticlabel = r.stations(exists=['measures.valueStatistic'], limit=1)[0]
        assert (dataWithmeasuresvalueStatisticlabel.measures().valueStatistic().label() != None)
        assert isinstance(dataWithmeasuresvalueStatisticlabel.measures().valueStatistic().label(), str)
        
    except IndexError:
        print('No data found with prop measures.valueStatistic.label')
    
    except ValueError:
        print('Invalid http request for prop measures.valueStatistic.label')

    except AttributeError:
        try:
            if isinstance(dataWithmeasuresvalueStatisticlabel.measures().valueStatistic(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithmeasuresvalueStatisticlabel.measures().valueStatistic())
        except AttributeError: 
            print('measures.valueStatistic.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('measures.valueStatistic.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithmeasuresobservationTypelabel = r.stations(exists=['measures.observationType'], limit=1)[0]
        assert (dataWithmeasuresobservationTypelabel.measures().observationType().label() != None)
        assert isinstance(dataWithmeasuresobservationTypelabel.measures().observationType().label(), str)
        
    except IndexError:
        print('No data found with prop measures.observationType.label')
    
    except ValueError:
        print('Invalid http request for prop measures.observationType.label')

    except AttributeError:
        try:
            if isinstance(dataWithmeasuresobservationTypelabel.measures().observationType(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithmeasuresobservationTypelabel.measures().observationType())
        except AttributeError: 
            print('measures.observationType.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('measures.observationType.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithsampleOflabel = r.stations(exists=['sampleOf'], limit=1)[0]
        assert (dataWithsampleOflabel.sampleOf().label() != None)
        assert isinstance(dataWithsampleOflabel.sampleOf().label(), str)
        
    except IndexError:
        print('No data found with prop sampleOf.label')
    
    except ValueError:
        print('Invalid http request for prop sampleOf.label')

    except AttributeError:
        try:
            if isinstance(dataWithsampleOflabel.sampleOf(), list):    
                assert all(isinstance(x.label(), str) for x in dataWithsampleOflabel.sampleOf())
        except AttributeError: 
            print('sampleOf.label: AttributeError most likely due to array wrongly specified as object in spec')
            return
        
        print('sampleOf.label: AttributeError most likely due to a null ancestor attribute')

    
    try:
        dataWithstatuslabel = r.stations(exists=['status.label'], limit=1)[0]
        assert (dataWithstatuslabel.status().label() != None)
        assert isinstance(dataWithstatuslabel.status().label(), str)
        
    except IndexError:
        print('No data found with prop status.label')

    except ValueError:
        print('Invalid http request for prop statuslabel')

    except AttributeError:
        try:
            assert all(isinstance(x.label(), str) for x in dataWithstatuslabel.status())
        except AttributeError: 
            print('status.label: AttributeError most likely due to array wrongly specified as object in spec')
    
    try:
        dataWithmeasuresqualifier = r.stations(exists=['measures.qualifier'], limit=1)[0]
        assert (dataWithmeasuresqualifier.measures().qualifier() != None)
        assert isinstance(dataWithmeasuresqualifier.measures().qualifier(), str)
        
    except IndexError:
        print('No data found with prop measures.qualifier')

    except ValueError:
        print('Invalid http request for prop measuresqualifier')

    except AttributeError:
        try:
            assert all(isinstance(x.qualifier(), str) for x in dataWithmeasuresqualifier.measures())
        except AttributeError: 
            print('measures.qualifier: AttributeError most likely due to array wrongly specified as object in spec')
    
    try:
        dataWithmeasuresperiod = r.stations(exists=['measures.period'], limit=1)[0]
        assert (dataWithmeasuresperiod.measures().period() != None)
        assert isinstance(dataWithmeasuresperiod.measures().period(), (int, float))
        
    except IndexError:
        print('No data found with prop measures.period')

    except ValueError:
        print('Invalid http request for prop measuresperiod')

    except AttributeError:
        try:
            assert all(isinstance(x.period(), (int, float)) for x in dataWithmeasuresperiod.measures())
        except AttributeError: 
            print('measures.period: AttributeError most likely due to array wrongly specified as object in spec')
    

 