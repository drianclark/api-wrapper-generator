import requests
from Station import Station
from Measure import Measure
from Reading import Reading

class Renders:

    def readings(
    self, 
    minDate=None,
    limit=None,
    stationRLOIid=None,
    completeness=None,
    offset=None,
    earliest=None,
    measure=None,
    observationType=None,
    maxeqDate=None,
    projection=None,
    period=None,
    quality=None,
    observedProperty=None,
    dateTime=None,
    date=None,
    stationWiskiID=None,
    maxDate=None,
    stationStationReference=None,
    qcode=None,
    station=None,
    latest=None,
    sort=None,
    view=None,
    mineqDate=None,
    value=None
    ):

        params = {}
        params['_limit'] = 5
        
        if minDate != None:
            params['min-date'] = minDate

        if limit != None:
            params['_limit'] = limit

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if completeness != None:
            params['completeness'] = completeness

        if offset != None:
            params['_offset'] = offset

        if earliest != None:
            params['earliest'] = earliest

        if measure != None:
            params['measure'] = measure

        if observationType != None:
            params['observationType'] = observationType

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if projection != None:
            params['_projection'] = projection

        if period != None:
            params['period'] = period

        if quality != None:
            params['quality'] = quality

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if dateTime != None:
            params['dateTime'] = dateTime

        if date != None:
            params['date'] = date

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if maxDate != None:
            params['max-date'] = maxDate

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if qcode != None:
            params['qcode'] = qcode

        if station != None:
            params['station'] = station

        if latest != None:
            params['latest'] = latest

        if sort != None:
            params['_sort'] = sort

        if view != None:
            params['view'] = view

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
    parameterName=None,
    limit=None,
    valueStatistic=None,
    stationRLOIid=None,
    offset=None,
    valueStatisticLabel=None,
    stationLabel=None,
    observationType=None,
    projection=None,
    unitName=None,
    observedPropertyLabel=None,
    period=None,
    label=None,
    observedProperty=None,
    parameter=None,
    unit=None,
    stationWiskiID=None,
    datumType=None,
    stationStationReference=None,
    station=None,
    sort=None,
    notation=None,
    qualifier=None,
    observationTypeLabel=None
    ):

        params = {}
        params['_limit'] = 5
        
        if parameterName != None:
            params['parameterName'] = parameterName

        if limit != None:
            params['_limit'] = limit

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if offset != None:
            params['_offset'] = offset

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if stationLabel != None:
            params['station.label'] = stationLabel

        if observationType != None:
            params['observationType'] = observationType

        if projection != None:
            params['_projection'] = projection

        if unitName != None:
            params['unitName'] = unitName

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if period != None:
            params['period'] = period

        if label != None:
            params['label'] = label

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if parameter != None:
            params['parameter'] = parameter

        if unit != None:
            params['unit'] = unit

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if datumType != None:
            params['datumType'] = datumType

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if station != None:
            params['station'] = station

        if sort != None:
            params['_sort'] = sort

        if notation != None:
            params['notation'] = notation

        if qualifier != None:
            params['qualifier'] = qualifier

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel


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
    date=None,
    minDate=None,
    maxDate=None,
    projection=None,
    view=None,
    earliest=None,
    latest=None,
    mineqDate=None,
    measure=None,
    maxeqDate=None
    ):

        params = {}
        
        if date != None:
            params['date'] = date

        if minDate != None:
            params['min-date'] = minDate

        if maxDate != None:
            params['max-date'] = maxDate

        if projection != None:
            params['_projection'] = projection

        if view != None:
            params['view'] = view

        if earliest != None:
            params['earliest'] = earliest

        if latest != None:
            params['latest'] = latest

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if measure != None:
            params['measure'] = measure

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate


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
    catchmentName=None,
    boreholeDepth=None,
    measuresObservedPropertyLabel=None,
    measuresValueStatistic=None,
    measuresValueStatisticLabel=None,
    limit=None,
    dist=None,
    long=None,
    measuresObservationTypeLabel=None,
    northing=None,
    search=None,
    offset=None,
    measuresQualifier=None,
    projection=None,
    measuresUnitName=None,
    stationReference=None,
    measuresLabel=None,
    measuresNotation=None,
    nrfaStationURL=None,
    wiskiID=None,
    label=None,
    observedProperty=None,
    dateOpened=None,
    statusLabel=None,
    aquifer=None,
    sampleOf=None,
    measures=None,
    sampleOfLabel=None,
    status=None,
    easting=None,
    measuresObservationType=None,
    measuresPeriod=None,
    RLOIid=None,
    sort=None,
    notation=None,
    town=None,
    measuresObservedProperty=None,
    riverName=None,
    type=None,
    nrfaStationID=None,
    datum=None,
    lat=None
    ):

        params = {}
        params['_limit'] = 5
        
        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if limit != None:
            params['_limit'] = limit

        if dist != None:
            params['dist'] = dist

        if long != None:
            params['long'] = long

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if northing != None:
            params['northing'] = northing

        if search != None:
            params['search'] = search

        if offset != None:
            params['_offset'] = offset

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if projection != None:
            params['_projection'] = projection

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if stationReference != None:
            params['stationReference'] = stationReference

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if label != None:
            params['label'] = label

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if statusLabel != None:
            params['status.label'] = statusLabel

        if aquifer != None:
            params['aquifer'] = aquifer

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if measures != None:
            params['measures'] = measures

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if status != None:
            params['status'] = status

        if easting != None:
            params['easting'] = easting

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if sort != None:
            params['_sort'] = sort

        if notation != None:
            params['notation'] = notation

        if town != None:
            params['town'] = town

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if riverName != None:
            params['riverName'] = riverName

        if type != None:
            params['type'] = type

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if datum != None:
            params['datum'] = datum

        if lat != None:
            params['lat'] = lat


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
    station=None,
    observationType=None,
    observedProperty=None,
    projection=None
    ):

        params = {}
        
        if station != None:
            params['station'] = station

        if observationType != None:
            params['observationType'] = observationType

        if observedProperty != None:
            params['observedProperty'] = observedProperty

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
