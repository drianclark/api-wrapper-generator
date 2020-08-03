import requests
from renders.Measure import Measure
from renders.Reading import Reading
from renders.Station import Station

class Renders:

    def readings(
    self, 
    sort=None,
    quality=None,
    minDate=None,
    station=None,
    stationWiskiID=None,
    earliest=None,
    maxDate=None,
    offset=None,
    qcode=None,
    mineqDate=None,
    view=None,
    limit=None,
    date=None,
    projection=None,
    value=None,
    dateTime=None,
    measure=None,
    period=None,
    latest=None,
    completeness=None,
    stationStationReference=None,
    stationRLOIid=None,
    observationType=None,
    maxeqDate=None,
    observedProperty=None
    ):

        params = {}
        params['_limit'] = 5
        
        if sort != None:
            params['_sort'] = sort

        if quality != None:
            params['quality'] = quality

        if minDate != None:
            params['min-date'] = minDate

        if station != None:
            params['station'] = station

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if earliest != None:
            params['earliest'] = earliest

        if maxDate != None:
            params['max-date'] = maxDate

        if offset != None:
            params['_offset'] = offset

        if qcode != None:
            params['qcode'] = qcode

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if view != None:
            params['view'] = view

        if limit != None:
            params['_limit'] = limit

        if date != None:
            params['date'] = date

        if projection != None:
            params['_projection'] = projection

        if value != None:
            params['value'] = value

        if dateTime != None:
            params['dateTime'] = dateTime

        if measure != None:
            params['measure'] = measure

        if period != None:
            params['period'] = period

        if latest != None:
            params['latest'] = latest

        if completeness != None:
            params['completeness'] = completeness

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if observationType != None:
            params['observationType'] = observationType

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

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
    sort=None,
    datumType=None,
    valueStatisticLabel=None,
    station=None,
    stationWiskiID=None,
    parameterName=None,
    unit=None,
    parameter=None,
    stationLabel=None,
    unitName=None,
    offset=None,
    notation=None,
    qualifier=None,
    limit=None,
    projection=None,
    valueStatistic=None,
    observationTypeLabel=None,
    period=None,
    stationStationReference=None,
    stationRLOIid=None,
    observationType=None,
    observedPropertyLabel=None,
    observedProperty=None,
    label=None
    ):

        params = {}
        params['_limit'] = 5
        
        if sort != None:
            params['_sort'] = sort

        if datumType != None:
            params['datumType'] = datumType

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if station != None:
            params['station'] = station

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if parameterName != None:
            params['parameterName'] = parameterName

        if unit != None:
            params['unit'] = unit

        if parameter != None:
            params['parameter'] = parameter

        if stationLabel != None:
            params['station.label'] = stationLabel

        if unitName != None:
            params['unitName'] = unitName

        if offset != None:
            params['_offset'] = offset

        if notation != None:
            params['notation'] = notation

        if qualifier != None:
            params['qualifier'] = qualifier

        if limit != None:
            params['_limit'] = limit

        if projection != None:
            params['_projection'] = projection

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if period != None:
            params['period'] = period

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if observationType != None:
            params['observationType'] = observationType

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if label != None:
            params['label'] = label


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
    date=None,
    latest=None,
    projection=None,
    maxeqDate=None,
    minDate=None,
    mineqDate=None,
    view=None,
    earliest=None,
    measure=None,
    maxDate=None
    ):

        params = {}
        
        if date != None:
            params['date'] = date

        if latest != None:
            params['latest'] = latest

        if projection != None:
            params['_projection'] = projection

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if minDate != None:
            params['min-date'] = minDate

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if view != None:
            params['view'] = view

        if earliest != None:
            params['earliest'] = earliest

        if measure != None:
            params['measure'] = measure

        if maxDate != None:
            params['max-date'] = maxDate


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
    measuresPeriod=None,
    measuresLabel=None,
    measuresQualifier=None,
    sort=None,
    aquifer=None,
    type=None,
    measuresObservedProperty=None,
    search=None,
    wiskiID=None,
    nrfaStationURL=None,
    catchmentName=None,
    observedProperty=None,
    offset=None,
    sampleOf=None,
    measuresNotation=None,
    statusLabel=None,
    notation=None,
    measuresValueStatistic=None,
    measuresObservedPropertyLabel=None,
    sampleOfLabel=None,
    dist=None,
    limit=None,
    nrfaStationID=None,
    projection=None,
    RLOIid=None,
    datum=None,
    boreholeDepth=None,
    long=None,
    measuresObservationType=None,
    easting=None,
    measuresUnitName=None,
    riverName=None,
    town=None,
    measuresValueStatisticLabel=None,
    status=None,
    northing=None,
    dateOpened=None,
    measuresObservationTypeLabel=None,
    lat=None,
    measures=None,
    stationReference=None,
    label=None
    ):

        params = {}
        params['_limit'] = 5
        
        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if sort != None:
            params['_sort'] = sort

        if aquifer != None:
            params['aquifer'] = aquifer

        if type != None:
            params['type'] = type

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if search != None:
            params['search'] = search

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if offset != None:
            params['_offset'] = offset

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if statusLabel != None:
            params['status.label'] = statusLabel

        if notation != None:
            params['notation'] = notation

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if dist != None:
            params['dist'] = dist

        if limit != None:
            params['_limit'] = limit

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if projection != None:
            params['_projection'] = projection

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if datum != None:
            params['datum'] = datum

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if long != None:
            params['long'] = long

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if easting != None:
            params['easting'] = easting

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if riverName != None:
            params['riverName'] = riverName

        if town != None:
            params['town'] = town

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if status != None:
            params['status'] = status

        if northing != None:
            params['northing'] = northing

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if lat != None:
            params['lat'] = lat

        if measures != None:
            params['measures'] = measures

        if stationReference != None:
            params['stationReference'] = stationReference

        if label != None:
            params['label'] = label


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
    projection=None,
    observationType=None,
    observedProperty=None
    ):

        params = {}
        
        if station != None:
            params['station'] = station

        if projection != None:
            params['_projection'] = projection

        if observationType != None:
            params['observationType'] = observationType

        if observedProperty != None:
            params['observedProperty'] = observedProperty


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measure(items[0])
        

        return data
