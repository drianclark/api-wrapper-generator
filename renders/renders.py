import requests
from Measure import Measure
from Reading import Reading
from Station import Station

class Renders:

    def readings(
    self, 
    earliest=None,
    completeness=None,
    stationRLOIid=None,
    value=None,
    period=None,
    stationStationReference=None,
    observationType=None,
    qcode=None,
    maxDate=None,
    quality=None,
    offset=None,
    latest=None,
    date=None,
    measure=None,
    observedProperty=None,
    minDate=None,
    limit=None,
    projection=None,
    view=None,
    mineqDate=None,
    station=None,
    stationWiskiID=None,
    sort=None,
    dateTime=None,
    maxeqDate=None
    ):

        params = {}
        params['_limit'] = 5
        
        if earliest != None:
            params['earliest'] = earliest

        if completeness != None:
            params['completeness'] = completeness

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if value != None:
            params['value'] = value

        if period != None:
            params['period'] = period

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if observationType != None:
            params['observationType'] = observationType

        if qcode != None:
            params['qcode'] = qcode

        if maxDate != None:
            params['max-date'] = maxDate

        if quality != None:
            params['quality'] = quality

        if offset != None:
            params['_offset'] = offset

        if latest != None:
            params['latest'] = latest

        if date != None:
            params['date'] = date

        if measure != None:
            params['measure'] = measure

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if minDate != None:
            params['min-date'] = minDate

        if limit != None:
            params['_limit'] = limit

        if projection != None:
            params['_projection'] = projection

        if view != None:
            params['view'] = view

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if station != None:
            params['station'] = station

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if sort != None:
            params['_sort'] = sort

        if dateTime != None:
            params['dateTime'] = dateTime

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate


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
    stationRLOIid=None,
    period=None,
    observationType=None,
    parameter=None,
    stationStationReference=None,
    notation=None,
    unitName=None,
    observedPropertyLabel=None,
    observationTypeLabel=None,
    label=None,
    stationLabel=None,
    unit=None,
    offset=None,
    observedProperty=None,
    limit=None,
    projection=None,
    qualifier=None,
    station=None,
    valueStatisticLabel=None,
    stationWiskiID=None,
    valueStatistic=None,
    sort=None,
    datumType=None,
    parameterName=None
    ):

        params = {}
        params['_limit'] = 5
        
        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if period != None:
            params['period'] = period

        if observationType != None:
            params['observationType'] = observationType

        if parameter != None:
            params['parameter'] = parameter

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if notation != None:
            params['notation'] = notation

        if unitName != None:
            params['unitName'] = unitName

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if label != None:
            params['label'] = label

        if stationLabel != None:
            params['station.label'] = stationLabel

        if unit != None:
            params['unit'] = unit

        if offset != None:
            params['_offset'] = offset

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if limit != None:
            params['_limit'] = limit

        if projection != None:
            params['_projection'] = projection

        if qualifier != None:
            params['qualifier'] = qualifier

        if station != None:
            params['station'] = station

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if sort != None:
            params['_sort'] = sort

        if datumType != None:
            params['datumType'] = datumType

        if parameterName != None:
            params['parameterName'] = parameterName


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
    projection=None,
    id=None
    ):

        params = {}
        
        if projection != None:
            params['_projection'] = projection

        if id != None:
            params['id'] = id


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
    earliest=None,
    latest=None,
    date=None,
    measure=None,
    maxeqDate=None,
    minDate=None,
    projection=None,
    maxDate=None,
    view=None,
    mineqDate=None
    ):

        params = {}
        
        if earliest != None:
            params['earliest'] = earliest

        if latest != None:
            params['latest'] = latest

        if date != None:
            params['date'] = date

        if measure != None:
            params['measure'] = measure

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if minDate != None:
            params['min-date'] = minDate

        if projection != None:
            params['_projection'] = projection

        if maxDate != None:
            params['max-date'] = maxDate

        if view != None:
            params['view'] = view

        if mineqDate != None:
            params['mineq-date'] = mineqDate


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
    measuresLabel=None,
    measuresObservedProperty=None,
    measuresObservedPropertyLabel=None,
    sampleOfLabel=None,
    nrfaStationID=None,
    northing=None,
    type=None,
    riverName=None,
    notation=None,
    stationReference=None,
    dist=None,
    search=None,
    dateOpened=None,
    measuresQualifier=None,
    label=None,
    easting=None,
    town=None,
    offset=None,
    measuresUnitName=None,
    measuresPeriod=None,
    observedProperty=None,
    statusLabel=None,
    catchmentName=None,
    nrfaStationURL=None,
    long=None,
    measuresNotation=None,
    boreholeDepth=None,
    limit=None,
    projection=None,
    measuresValueStatisticLabel=None,
    measures=None,
    measuresValueStatistic=None,
    sort=None,
    RLOIid=None,
    measuresObservationType=None,
    datum=None,
    lat=None,
    measuresObservationTypeLabel=None,
    sampleOf=None,
    status=None,
    wiskiID=None,
    aquifer=None
    ):

        params = {}
        params['_limit'] = 5
        
        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if northing != None:
            params['northing'] = northing

        if type != None:
            params['type'] = type

        if riverName != None:
            params['riverName'] = riverName

        if notation != None:
            params['notation'] = notation

        if stationReference != None:
            params['stationReference'] = stationReference

        if dist != None:
            params['dist'] = dist

        if search != None:
            params['search'] = search

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if label != None:
            params['label'] = label

        if easting != None:
            params['easting'] = easting

        if town != None:
            params['town'] = town

        if offset != None:
            params['_offset'] = offset

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if statusLabel != None:
            params['status.label'] = statusLabel

        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if long != None:
            params['long'] = long

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if limit != None:
            params['_limit'] = limit

        if projection != None:
            params['_projection'] = projection

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if measures != None:
            params['measures'] = measures

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if sort != None:
            params['_sort'] = sort

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if datum != None:
            params['datum'] = datum

        if lat != None:
            params['lat'] = lat

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if status != None:
            params['status'] = status

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if aquifer != None:
            params['aquifer'] = aquifer


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
    projection=None,
    id=None
    ):

        params = {}
        
        if projection != None:
            params['_projection'] = projection

        if id != None:
            params['id'] = id


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
    station=None,
    observedProperty=None,
    projection=None,
    observationType=None
    ):

        params = {}
        
        if station != None:
            params['station'] = station

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if projection != None:
            params['_projection'] = projection

        if observationType != None:
            params['observationType'] = observationType


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measure(items[0])
        

        return data
