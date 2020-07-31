import requests
from renders.Reading import Reading
from renders.Measure import Measure
from renders.Station import Station

class Renders:

    def readings(
    self, 
    offset=None,
    maxeqDate=None,
    quality=None,
    dateTime=None,
    value=None,
    stationStationReference=None,
    earliest=None,
    limit=None,
    maxDate=None,
    latest=None,
    completeness=None,
    sort=None,
    stationRLOIid=None,
    projection=None,
    observationType=None,
    view=None,
    measure=None,
    qcode=None,
    station=None,
    stationWiskiID=None,
    mineqDate=None,
    date=None,
    minDate=None,
    period=None,
    observedProperty=None
    ):

        params = {}
        params['_limit'] = 5
        
        if offset != None:
            params['_offset'] = offset

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if quality != None:
            params['quality'] = quality

        if dateTime != None:
            params['dateTime'] = dateTime

        if value != None:
            params['value'] = value

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if earliest != None:
            params['earliest'] = earliest

        if limit != None:
            params['_limit'] = limit

        if maxDate != None:
            params['max-date'] = maxDate

        if latest != None:
            params['latest'] = latest

        if completeness != None:
            params['completeness'] = completeness

        if sort != None:
            params['_sort'] = sort

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if projection != None:
            params['_projection'] = projection

        if observationType != None:
            params['observationType'] = observationType

        if view != None:
            params['view'] = view

        if measure != None:
            params['measure'] = measure

        if qcode != None:
            params['qcode'] = qcode

        if station != None:
            params['station'] = station

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if date != None:
            params['date'] = date

        if minDate != None:
            params['min-date'] = minDate

        if period != None:
            params['period'] = period

        if observedProperty != None:
            params['observedProperty'] = observedProperty


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/data/readings.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = [Reading(item) for item in items]
        

        return data

    def measures(
    self, 
    offset=None,
    valueStatisticLabel=None,
    qualifier=None,
    stationStationReference=None,
    limit=None,
    notation=None,
    sort=None,
    parameterName=None,
    stationRLOIid=None,
    datumType=None,
    projection=None,
    observationType=None,
    unitName=None,
    unit=None,
    label=None,
    stationLabel=None,
    station=None,
    stationWiskiID=None,
    valueStatistic=None,
    parameter=None,
    observationTypeLabel=None,
    observedPropertyLabel=None,
    period=None,
    observedProperty=None
    ):

        params = {}
        params['_limit'] = 5
        
        if offset != None:
            params['_offset'] = offset

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if qualifier != None:
            params['qualifier'] = qualifier

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if limit != None:
            params['_limit'] = limit

        if notation != None:
            params['notation'] = notation

        if sort != None:
            params['_sort'] = sort

        if parameterName != None:
            params['parameterName'] = parameterName

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if datumType != None:
            params['datumType'] = datumType

        if projection != None:
            params['_projection'] = projection

        if observationType != None:
            params['observationType'] = observationType

        if unitName != None:
            params['unitName'] = unitName

        if unit != None:
            params['unit'] = unit

        if label != None:
            params['label'] = label

        if stationLabel != None:
            params['station.label'] = stationLabel

        if station != None:
            params['station'] = station

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if parameter != None:
            params['parameter'] = parameter

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if period != None:
            params['period'] = period

        if observedProperty != None:
            params['observedProperty'] = observedProperty


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = [Measure(item) for item in items]
        

        return data

    def measuresById(
    self, 
    id=None,
    projection=None
    ):

        params = {}
        
        if id != None:
            params['id'] = id

        if projection != None:
            params['_projection'] = projection


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{id}.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measure(items[0])
        

        return data

    def readingsByMeasure(
    self, 
    projection=None,
    minDate=None,
    maxeqDate=None,
    maxDate=None,
    latest=None,
    view=None,
    measure=None,
    mineqDate=None,
    earliest=None,
    date=None
    ):

        params = {}
        
        if projection != None:
            params['_projection'] = projection

        if minDate != None:
            params['min-date'] = minDate

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if maxDate != None:
            params['max-date'] = maxDate

        if latest != None:
            params['latest'] = latest

        if view != None:
            params['view'] = view

        if measure != None:
            params['measure'] = measure

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if earliest != None:
            params['earliest'] = earliest

        if date != None:
            params['date'] = date


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{measure}/readings.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Reading(items[0])
        

        return data

    def stations(
    self, 
    measuresUnitName=None,
    measuresObservationTypeLabel=None,
    offset=None,
    measures=None,
    measuresQualifier=None,
    measuresObservedProperty=None,
    status=None,
    datum=None,
    dateOpened=None,
    measuresLabel=None,
    limit=None,
    notation=None,
    search=None,
    boreholeDepth=None,
    measuresValueStatisticLabel=None,
    northing=None,
    dist=None,
    sort=None,
    measuresObservationType=None,
    nrfaStationID=None,
    sampleOf=None,
    measuresPeriod=None,
    projection=None,
    sampleOfLabel=None,
    riverName=None,
    label=None,
    catchmentName=None,
    town=None,
    measuresNotation=None,
    measuresObservedPropertyLabel=None,
    RLOIid=None,
    wiskiID=None,
    type=None,
    statusLabel=None,
    long=None,
    stationReference=None,
    aquifer=None,
    measuresValueStatistic=None,
    observedProperty=None,
    easting=None,
    lat=None,
    nrfaStationURL=None
    ):

        params = {}
        params['_limit'] = 5
        
        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if offset != None:
            params['_offset'] = offset

        if measures != None:
            params['measures'] = measures

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if status != None:
            params['status'] = status

        if datum != None:
            params['datum'] = datum

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if limit != None:
            params['_limit'] = limit

        if notation != None:
            params['notation'] = notation

        if search != None:
            params['search'] = search

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if northing != None:
            params['northing'] = northing

        if dist != None:
            params['dist'] = dist

        if sort != None:
            params['_sort'] = sort

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if projection != None:
            params['_projection'] = projection

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if riverName != None:
            params['riverName'] = riverName

        if label != None:
            params['label'] = label

        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if town != None:
            params['town'] = town

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if type != None:
            params['type'] = type

        if statusLabel != None:
            params['status.label'] = statusLabel

        if long != None:
            params['long'] = long

        if stationReference != None:
            params['stationReference'] = stationReference

        if aquifer != None:
            params['aquifer'] = aquifer

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if easting != None:
            params['easting'] = easting

        if lat != None:
            params['lat'] = lat

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = [Station(item) for item in items]
        

        return data

    def stationsById(
    self, 
    id=None,
    projection=None
    ):

        params = {}
        
        if id != None:
            params['id'] = id

        if projection != None:
            params['_projection'] = projection


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{id}.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Station(items[0])
        

        return data

    def measuresByStation(
    self, 
    projection=None,
    observationType=None,
    observedProperty=None,
    station=None
    ):

        params = {}
        
        if projection != None:
            params['_projection'] = projection

        if observationType != None:
            params['observationType'] = observationType

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if station != None:
            params['station'] = station


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measure(items[0])
        

        return data
