import requests
from Station import Station
from Reading import Reading
from Measure import Measure

class Renders:

    def readings(
    self, 
    dateTime=None,
    limit=None,
    sort=None,
    qcode=None,
    offset=None,
    minDate=None,
    quality=None,
    observationType=None,
    value=None,
    stationStationReference=None,
    view=None,
    period=None,
    latest=None,
    earliest=None,
    maxeqDate=None,
    measure=None,
    mineqDate=None,
    stationRLOIid=None,
    observedProperty=None,
    maxDate=None,
    projection=None,
    completeness=None,
    date=None,
    station=None,
    stationWiskiID=None
    ):

        params = {}
        params['_limit'] = 5
        
        if dateTime != None:
            params['dateTime'] = dateTime

        if limit != None:
            params['_limit'] = limit

        if sort != None:
            params['_sort'] = sort

        if qcode != None:
            params['qcode'] = qcode

        if offset != None:
            params['_offset'] = offset

        if minDate != None:
            params['min-date'] = minDate

        if quality != None:
            params['quality'] = quality

        if observationType != None:
            params['observationType'] = observationType

        if value != None:
            params['value'] = value

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if view != None:
            params['view'] = view

        if period != None:
            params['period'] = period

        if latest != None:
            params['latest'] = latest

        if earliest != None:
            params['earliest'] = earliest

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if measure != None:
            params['measure'] = measure

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if maxDate != None:
            params['max-date'] = maxDate

        if projection != None:
            params['_projection'] = projection

        if completeness != None:
            params['completeness'] = completeness

        if date != None:
            params['date'] = date

        if station != None:
            params['station'] = station

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID


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
    unit=None,
    limit=None,
    label=None,
    sort=None,
    notation=None,
    offset=None,
    observationType=None,
    stationStationReference=None,
    period=None,
    parameter=None,
    valueStatistic=None,
    stationLabel=None,
    observedPropertyLabel=None,
    stationRLOIid=None,
    observedProperty=None,
    projection=None,
    parameterName=None,
    qualifier=None,
    unitName=None,
    valueStatisticLabel=None,
    observationTypeLabel=None,
    datumType=None,
    station=None,
    stationWiskiID=None
    ):

        params = {}
        params['_limit'] = 5
        
        if unit != None:
            params['unit'] = unit

        if limit != None:
            params['_limit'] = limit

        if label != None:
            params['label'] = label

        if sort != None:
            params['_sort'] = sort

        if notation != None:
            params['notation'] = notation

        if offset != None:
            params['_offset'] = offset

        if observationType != None:
            params['observationType'] = observationType

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if period != None:
            params['period'] = period

        if parameter != None:
            params['parameter'] = parameter

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if stationLabel != None:
            params['station.label'] = stationLabel

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if projection != None:
            params['_projection'] = projection

        if parameterName != None:
            params['parameterName'] = parameterName

        if qualifier != None:
            params['qualifier'] = qualifier

        if unitName != None:
            params['unitName'] = unitName

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if datumType != None:
            params['datumType'] = datumType

        if station != None:
            params['station'] = station

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID


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
    maxeqDate=None,
    minDate=None,
    maxDate=None,
    measure=None,
    projection=None,
    view=None,
    mineqDate=None,
    date=None,
    latest=None
    ):

        params = {}
        
        if earliest != None:
            params['earliest'] = earliest

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if minDate != None:
            params['min-date'] = minDate

        if maxDate != None:
            params['max-date'] = maxDate

        if measure != None:
            params['measure'] = measure

        if projection != None:
            params['_projection'] = projection

        if view != None:
            params['view'] = view

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if date != None:
            params['date'] = date

        if latest != None:
            params['latest'] = latest


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
    lat=None,
    measuresObservationType=None,
    type=None,
    limit=None,
    dist=None,
    label=None,
    sort=None,
    notation=None,
    measuresPeriod=None,
    aquifer=None,
    measuresObservedPropertyLabel=None,
    offset=None,
    datum=None,
    nrfaStationID=None,
    dateOpened=None,
    easting=None,
    RLOIid=None,
    sampleOf=None,
    statusLabel=None,
    northing=None,
    sampleOfLabel=None,
    search=None,
    measuresQualifier=None,
    wiskiID=None,
    measuresObservationTypeLabel=None,
    riverName=None,
    long=None,
    measuresUnitName=None,
    boreholeDepth=None,
    measuresObservedProperty=None,
    measures=None,
    measuresValueStatisticLabel=None,
    measuresNotation=None,
    observedProperty=None,
    nrfaStationURL=None,
    stationReference=None,
    town=None,
    projection=None,
    catchmentName=None,
    measuresLabel=None,
    measuresValueStatistic=None,
    status=None
    ):

        params = {}
        params['_limit'] = 5
        
        if lat != None:
            params['lat'] = lat

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if type != None:
            params['type'] = type

        if limit != None:
            params['_limit'] = limit

        if dist != None:
            params['dist'] = dist

        if label != None:
            params['label'] = label

        if sort != None:
            params['_sort'] = sort

        if notation != None:
            params['notation'] = notation

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if aquifer != None:
            params['aquifer'] = aquifer

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if offset != None:
            params['_offset'] = offset

        if datum != None:
            params['datum'] = datum

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if easting != None:
            params['easting'] = easting

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if statusLabel != None:
            params['status.label'] = statusLabel

        if northing != None:
            params['northing'] = northing

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if search != None:
            params['search'] = search

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if riverName != None:
            params['riverName'] = riverName

        if long != None:
            params['long'] = long

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if measures != None:
            params['measures'] = measures

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if stationReference != None:
            params['stationReference'] = stationReference

        if town != None:
            params['town'] = town

        if projection != None:
            params['_projection'] = projection

        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if status != None:
            params['status'] = status


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
    observationType=None,
    observedProperty=None,
    station=None,
    projection=None
    ):

        params = {}
        
        if observationType != None:
            params['observationType'] = observationType

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if station != None:
            params['station'] = station

        if projection != None:
            params['_projection'] = projection


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measure(items[0])
        

        return data
