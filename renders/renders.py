import requests
from renders.Reading import Reading
from renders.Station import Station
from renders.Measure import Measure

class Renders:

    def readings(
    self,
    exists=[],
    minDate=None,
    stationRLOIid=None,
    offset=None,
    qcode=None,
    mineqDate=None,
    dateTime=None,
    date=None,
    earliest=None,
    station=None,
    projection=None,
    maxeqDate=None,
    observedProperty=None,
    quality=None,
    stationWiskiID=None,
    completeness=None,
    sort=None,
    maxDate=None,
    limit=None,
    view=None,
    stationStationReference=None,
    latest=None,
    period=None,
    observationType=None,
    measure=None,
    value=None
    ):

        params = {}
        params['_limit'] = 5
        
        if minDate != None:
            params['min-date'] = minDate

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if offset != None:
            params['_offset'] = offset

        if qcode != None:
            params['qcode'] = qcode

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if dateTime != None:
            params['dateTime'] = dateTime

        if date != None:
            params['date'] = date

        if earliest != None:
            params['earliest'] = earliest

        if station != None:
            params['station'] = station

        if projection != None:
            params['_projection'] = projection

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if quality != None:
            params['quality'] = quality

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if completeness != None:
            params['completeness'] = completeness

        if sort != None:
            params['_sort'] = sort

        if maxDate != None:
            params['max-date'] = maxDate

        if limit != None:
            params['_limit'] = limit

        if view != None:
            params['view'] = view

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if latest != None:
            params['latest'] = latest

        if period != None:
            params['period'] = period

        if observationType != None:
            params['observationType'] = observationType

        if measure != None:
            params['measure'] = measure

        if value != None:
            params['value'] = value

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

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
    exists=[],
    unitName=None,
    qualifier=None,
    parameterName=None,
    stationRLOIid=None,
    offset=None,
    notation=None,
    observationTypeLabel=None,
    station=None,
    projection=None,
    valueStatistic=None,
    observedProperty=None,
    valueStatisticLabel=None,
    stationWiskiID=None,
    stationLabel=None,
    label=None,
    sort=None,
    parameter=None,
    limit=None,
    unit=None,
    stationStationReference=None,
    observedPropertyLabel=None,
    period=None,
    observationType=None,
    datumType=None
    ):

        params = {}
        params['_limit'] = 5
        
        if unitName != None:
            params['unitName'] = unitName

        if qualifier != None:
            params['qualifier'] = qualifier

        if parameterName != None:
            params['parameterName'] = parameterName

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if offset != None:
            params['_offset'] = offset

        if notation != None:
            params['notation'] = notation

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if station != None:
            params['station'] = station

        if projection != None:
            params['_projection'] = projection

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if stationLabel != None:
            params['station.label'] = stationLabel

        if label != None:
            params['label'] = label

        if sort != None:
            params['_sort'] = sort

        if parameter != None:
            params['parameter'] = parameter

        if limit != None:
            params['_limit'] = limit

        if unit != None:
            params['unit'] = unit

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if period != None:
            params['period'] = period

        if observationType != None:
            params['observationType'] = observationType

        if datumType != None:
            params['datumType'] = datumType

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

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
    exists=[],
    id=None,
    projection=None
    ):

        params = {}
        
        if id != None:
            params['id'] = id

        if projection != None:
            params['_projection'] = projection

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

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
    exists=[],
    latest=None,
    minDate=None,
    date=None,
    earliest=None,
    projection=None,
    maxeqDate=None,
    maxDate=None,
    measure=None,
    view=None,
    mineqDate=None
    ):

        params = {}
        
        if latest != None:
            params['latest'] = latest

        if minDate != None:
            params['min-date'] = minDate

        if date != None:
            params['date'] = date

        if earliest != None:
            params['earliest'] = earliest

        if projection != None:
            params['_projection'] = projection

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if maxDate != None:
            params['max-date'] = maxDate

        if measure != None:
            params['measure'] = measure

        if view != None:
            params['view'] = view

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

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
    exists=[],
    measuresPeriod=None,
    status=None,
    lat=None,
    measuresObservedPropertyLabel=None,
    long=None,
    offset=None,
    sampleOf=None,
    notation=None,
    datum=None,
    type=None,
    catchmentName=None,
    town=None,
    measures=None,
    measuresQualifier=None,
    projection=None,
    observedProperty=None,
    measuresLabel=None,
    measuresValueStatistic=None,
    measuresObservationType=None,
    search=None,
    dist=None,
    aquifer=None,
    label=None,
    sort=None,
    measuresObservationTypeLabel=None,
    nrfaStationURL=None,
    limit=None,
    measuresUnitName=None,
    nrfaStationID=None,
    stationReference=None,
    wiskiID=None,
    dateOpened=None,
    easting=None,
    measuresValueStatisticLabel=None,
    northing=None,
    measuresNotation=None,
    boreholeDepth=None,
    measuresObservedProperty=None,
    sampleOfLabel=None,
    RLOIid=None,
    riverName=None,
    statusLabel=None
    ):

        params = {}
        params['_limit'] = 5
        
        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if status != None:
            params['status'] = status

        if lat != None:
            params['lat'] = lat

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if long != None:
            params['long'] = long

        if offset != None:
            params['_offset'] = offset

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if notation != None:
            params['notation'] = notation

        if datum != None:
            params['datum'] = datum

        if type != None:
            params['type'] = type

        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if town != None:
            params['town'] = town

        if measures != None:
            params['measures'] = measures

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if projection != None:
            params['_projection'] = projection

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if search != None:
            params['search'] = search

        if dist != None:
            params['dist'] = dist

        if aquifer != None:
            params['aquifer'] = aquifer

        if label != None:
            params['label'] = label

        if sort != None:
            params['_sort'] = sort

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if limit != None:
            params['_limit'] = limit

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if stationReference != None:
            params['stationReference'] = stationReference

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if easting != None:
            params['easting'] = easting

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if northing != None:
            params['northing'] = northing

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if riverName != None:
            params['riverName'] = riverName

        if statusLabel != None:
            params['status.label'] = statusLabel

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

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
    exists=[],
    id=None,
    projection=None
    ):

        params = {}
        
        if id != None:
            params['id'] = id

        if projection != None:
            params['_projection'] = projection

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

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
    exists=[],
    observedProperty=None,
    projection=None,
    station=None,
    observationType=None
    ):

        params = {}
        
        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if projection != None:
            params['_projection'] = projection

        if station != None:
            params['station'] = station

        if observationType != None:
            params['observationType'] = observationType

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measure(items[0])
        

        return data
