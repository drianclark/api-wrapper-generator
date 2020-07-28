import requests
from Station import Station
from Reading import Reading
from Measure import Measure

class Renders:

    def readings(
    self, 
    sort=None,
    maxDate=None,
    station=None,
    observationType=None,
    measure=None,
    earliest=None,
    date=None,
    quality=None,
    stationRLOIid=None,
    offset=None,
    qcode=None,
    view=None,
    stationStationReference=None,
    latest=None,
    dateTime=None,
    completeness=None,
    period=None,
    maxeqDate=None,
    minDate=None,
    stationWiskiID=None,
    projection=None,
    observedProperty=None,
    limit=None,
    mineqDate=None,
    value=None
    ):

        params = {}
        params['_limit'] = 5
        
        if sort != None:
            params['_sort'] = sort

        if maxDate != None:
            params['max-date'] = maxDate

        if station != None:
            params['station'] = station

        if observationType != None:
            params['observationType'] = observationType

        if measure != None:
            params['measure'] = measure

        if earliest != None:
            params['earliest'] = earliest

        if date != None:
            params['date'] = date

        if quality != None:
            params['quality'] = quality

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if offset != None:
            params['_offset'] = offset

        if qcode != None:
            params['qcode'] = qcode

        if view != None:
            params['view'] = view

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if latest != None:
            params['latest'] = latest

        if dateTime != None:
            params['dateTime'] = dateTime

        if completeness != None:
            params['completeness'] = completeness

        if period != None:
            params['period'] = period

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if minDate != None:
            params['min-date'] = minDate

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if projection != None:
            params['_projection'] = projection

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if limit != None:
            params['_limit'] = limit

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if value != None:
            params['value'] = value


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
    stationLabel=None,
    sort=None,
    qualifier=None,
    station=None,
    observationType=None,
    observationTypeLabel=None,
    observedPropertyLabel=None,
    stationRLOIid=None,
    label=None,
    offset=None,
    valueStatistic=None,
    unit=None,
    stationStationReference=None,
    datumType=None,
    period=None,
    unitName=None,
    valueStatisticLabel=None,
    parameterName=None,
    stationWiskiID=None,
    projection=None,
    observedProperty=None,
    limit=None,
    parameter=None,
    notation=None
    ):

        params = {}
        params['_limit'] = 5
        
        if stationLabel != None:
            params['station.label'] = stationLabel

        if sort != None:
            params['_sort'] = sort

        if qualifier != None:
            params['qualifier'] = qualifier

        if station != None:
            params['station'] = station

        if observationType != None:
            params['observationType'] = observationType

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if label != None:
            params['label'] = label

        if offset != None:
            params['_offset'] = offset

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if unit != None:
            params['unit'] = unit

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if datumType != None:
            params['datumType'] = datumType

        if period != None:
            params['period'] = period

        if unitName != None:
            params['unitName'] = unitName

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if parameterName != None:
            params['parameterName'] = parameterName

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if projection != None:
            params['_projection'] = projection

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if limit != None:
            params['_limit'] = limit

        if parameter != None:
            params['parameter'] = parameter

        if notation != None:
            params['notation'] = notation


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
    earliest=None,
    date=None,
    maxeqDate=None,
    mineqDate=None,
    minDate=None,
    view=None,
    projection=None,
    maxDate=None,
    latest=None,
    measure=None
    ):

        params = {}
        
        if earliest != None:
            params['earliest'] = earliest

        if date != None:
            params['date'] = date

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if minDate != None:
            params['min-date'] = minDate

        if view != None:
            params['view'] = view

        if projection != None:
            params['_projection'] = projection

        if maxDate != None:
            params['max-date'] = maxDate

        if latest != None:
            params['latest'] = latest

        if measure != None:
            params['measure'] = measure


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
    measuresNotation=None,
    measuresObservedProperty=None,
    measuresObservedPropertyLabel=None,
    nrfaStationURL=None,
    measuresQualifier=None,
    boreholeDepth=None,
    measures=None,
    measuresPeriod=None,
    sort=None,
    nrfaStationID=None,
    status=None,
    riverName=None,
    RLOIid=None,
    northing=None,
    sampleOfLabel=None,
    measuresLabel=None,
    measuresUnitName=None,
    statusLabel=None,
    datum=None,
    measuresObservationType=None,
    stationReference=None,
    measuresValueStatisticLabel=None,
    measuresValueStatistic=None,
    wiskiID=None,
    label=None,
    search=None,
    offset=None,
    long=None,
    town=None,
    easting=None,
    lat=None,
    dist=None,
    aquifer=None,
    dateOpened=None,
    projection=None,
    observedProperty=None,
    measuresObservationTypeLabel=None,
    limit=None,
    catchmentName=None,
    sampleOf=None,
    notation=None,
    type=None
    ):

        params = {}
        params['_limit'] = 5
        
        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if measures != None:
            params['measures'] = measures

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if sort != None:
            params['_sort'] = sort

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if status != None:
            params['status'] = status

        if riverName != None:
            params['riverName'] = riverName

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if northing != None:
            params['northing'] = northing

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if statusLabel != None:
            params['status.label'] = statusLabel

        if datum != None:
            params['datum'] = datum

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if stationReference != None:
            params['stationReference'] = stationReference

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if label != None:
            params['label'] = label

        if search != None:
            params['search'] = search

        if offset != None:
            params['_offset'] = offset

        if long != None:
            params['long'] = long

        if town != None:
            params['town'] = town

        if easting != None:
            params['easting'] = easting

        if lat != None:
            params['lat'] = lat

        if dist != None:
            params['dist'] = dist

        if aquifer != None:
            params['aquifer'] = aquifer

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if projection != None:
            params['_projection'] = projection

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if limit != None:
            params['_limit'] = limit

        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if notation != None:
            params['notation'] = notation

        if type != None:
            params['type'] = type


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
    observedProperty=None,
    observationType=None,
    projection=None,
    station=None
    ):

        params = {}
        
        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if observationType != None:
            params['observationType'] = observationType

        if projection != None:
            params['_projection'] = projection

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
