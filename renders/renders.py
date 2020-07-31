import requests
from renders.Station import Station
from renders.Measure import Measure
from renders.Reading import Reading

class Renders:

    def readings(
    self, 
    quality=None,
    stationRLOIid=None,
    sort=None,
    stationStationReference=None,
    period=None,
    view=None,
    measure=None,
    minDate=None,
    stationWiskiID=None,
    maxDate=None,
    completeness=None,
    maxeqDate=None,
    observationType=None,
    projection=None,
    qcode=None,
    offset=None,
    observedProperty=None,
    dateTime=None,
    limit=None,
    station=None,
    earliest=None,
    date=None,
    latest=None,
    mineqDate=None,
    value=None
    ):

        params = {}
        params['_limit'] = 5
        
        if quality != None:
            params['quality'] = quality

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if sort != None:
            params['_sort'] = sort

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if period != None:
            params['period'] = period

        if view != None:
            params['view'] = view

        if measure != None:
            params['measure'] = measure

        if minDate != None:
            params['min-date'] = minDate

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if maxDate != None:
            params['max-date'] = maxDate

        if completeness != None:
            params['completeness'] = completeness

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if observationType != None:
            params['observationType'] = observationType

        if projection != None:
            params['_projection'] = projection

        if qcode != None:
            params['qcode'] = qcode

        if offset != None:
            params['_offset'] = offset

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if dateTime != None:
            params['dateTime'] = dateTime

        if limit != None:
            params['_limit'] = limit

        if station != None:
            params['station'] = station

        if earliest != None:
            params['earliest'] = earliest

        if date != None:
            params['date'] = date

        if latest != None:
            params['latest'] = latest

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
    valueStatistic=None,
    stationRLOIid=None,
    parameter=None,
    sort=None,
    datumType=None,
    stationStationReference=None,
    period=None,
    observationTypeLabel=None,
    qualifier=None,
    label=None,
    stationWiskiID=None,
    observedPropertyLabel=None,
    observationType=None,
    projection=None,
    offset=None,
    parameterName=None,
    unit=None,
    observedProperty=None,
    unitName=None,
    limit=None,
    station=None,
    valueStatisticLabel=None,
    notation=None
    ):

        params = {}
        params['_limit'] = 5
        
        if stationLabel != None:
            params['station.label'] = stationLabel

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if parameter != None:
            params['parameter'] = parameter

        if sort != None:
            params['_sort'] = sort

        if datumType != None:
            params['datumType'] = datumType

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if period != None:
            params['period'] = period

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if qualifier != None:
            params['qualifier'] = qualifier

        if label != None:
            params['label'] = label

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if observationType != None:
            params['observationType'] = observationType

        if projection != None:
            params['_projection'] = projection

        if offset != None:
            params['_offset'] = offset

        if parameterName != None:
            params['parameterName'] = parameterName

        if unit != None:
            params['unit'] = unit

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if unitName != None:
            params['unitName'] = unitName

        if limit != None:
            params['_limit'] = limit

        if station != None:
            params['station'] = station

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

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
    view=None,
    measure=None,
    earliest=None,
    minDate=None,
    latest=None,
    date=None,
    maxDate=None,
    maxeqDate=None,
    mineqDate=None,
    projection=None
    ):

        params = {}
        
        if view != None:
            params['view'] = view

        if measure != None:
            params['measure'] = measure

        if earliest != None:
            params['earliest'] = earliest

        if minDate != None:
            params['min-date'] = minDate

        if latest != None:
            params['latest'] = latest

        if date != None:
            params['date'] = date

        if maxDate != None:
            params['max-date'] = maxDate

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if projection != None:
            params['_projection'] = projection


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
    easting=None,
    statusLabel=None,
    sort=None,
    lat=None,
    riverName=None,
    dist=None,
    dateOpened=None,
    stationReference=None,
    measures=None,
    long=None,
    measuresNotation=None,
    label=None,
    type=None,
    boreholeDepth=None,
    measuresObservedProperty=None,
    measuresUnitName=None,
    projection=None,
    nrfaStationID=None,
    sampleOf=None,
    measuresValueStatisticLabel=None,
    town=None,
    offset=None,
    observedProperty=None,
    aquifer=None,
    nrfaStationURL=None,
    wiskiID=None,
    measuresPeriod=None,
    limit=None,
    northing=None,
    measuresLabel=None,
    measuresQualifier=None,
    sampleOfLabel=None,
    search=None,
    measuresObservationType=None,
    status=None,
    measuresObservedPropertyLabel=None,
    notation=None,
    RLOIid=None,
    measuresObservationTypeLabel=None,
    measuresValueStatistic=None,
    datum=None,
    catchmentName=None
    ):

        params = {}
        params['_limit'] = 5
        
        if easting != None:
            params['easting'] = easting

        if statusLabel != None:
            params['status.label'] = statusLabel

        if sort != None:
            params['_sort'] = sort

        if lat != None:
            params['lat'] = lat

        if riverName != None:
            params['riverName'] = riverName

        if dist != None:
            params['dist'] = dist

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if stationReference != None:
            params['stationReference'] = stationReference

        if measures != None:
            params['measures'] = measures

        if long != None:
            params['long'] = long

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if label != None:
            params['label'] = label

        if type != None:
            params['type'] = type

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if projection != None:
            params['_projection'] = projection

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if town != None:
            params['town'] = town

        if offset != None:
            params['_offset'] = offset

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if aquifer != None:
            params['aquifer'] = aquifer

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if limit != None:
            params['_limit'] = limit

        if northing != None:
            params['northing'] = northing

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if search != None:
            params['search'] = search

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if status != None:
            params['status'] = status

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if notation != None:
            params['notation'] = notation

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if datum != None:
            params['datum'] = datum

        if catchmentName != None:
            params['catchmentName'] = catchmentName


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
    projection=None,
    observedProperty=None,
    observationType=None,
    station=None
    ):

        params = {}
        
        if projection != None:
            params['_projection'] = projection

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if observationType != None:
            params['observationType'] = observationType

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
