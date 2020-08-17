import requests
from renders.Measure import Measure
from renders.Reading import Reading
from renders.Station import Station

class Renders:

    def readings(
    self,
    exists=[],
    completeness=None,
    offset=None,
    latest=None,
    mineqDate=None,
    earliest=None,
    minDate=None,
    observationType=None,
    stationStationReference=None,
    date=None,
    measure=None,
    limit=None,
    stationWiskiID=None,
    qcode=None,
    sort=None,
    view=None,
    observedProperty=None,
    projection=None,
    period=None,
    stationRLOIid=None,
    station=None,
    maxDate=None,
    dateTime=None,
    maxeqDate=None,
    quality=None,
    value=None
    ):

        params = {}
        params['_limit'] = 5
        
        if completeness != None:
            params['completeness'] = completeness

        if offset != None:
            params['_offset'] = offset

        if latest != None:
            params['latest'] = latest

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if earliest != None:
            params['earliest'] = earliest

        if minDate != None:
            params['min-date'] = minDate

        if observationType != None:
            params['observationType'] = observationType

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if date != None:
            params['date'] = date

        if measure != None:
            params['measure'] = measure

        if limit != None:
            params['_limit'] = limit

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if qcode != None:
            params['qcode'] = qcode

        if sort != None:
            params['_sort'] = sort

        if view != None:
            params['view'] = view

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if projection != None:
            params['_projection'] = projection

        if period != None:
            params['period'] = period

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if station != None:
            params['station'] = station

        if maxDate != None:
            params['max-date'] = maxDate

        if dateTime != None:
            params['dateTime'] = dateTime

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if quality != None:
            params['quality'] = quality

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
    label=None,
    unitName=None,
    offset=None,
    datumType=None,
    valueStatistic=None,
    observationType=None,
    unit=None,
    stationStationReference=None,
    limit=None,
    stationWiskiID=None,
    observedPropertyLabel=None,
    valueStatisticLabel=None,
    qualifier=None,
    sort=None,
    observationTypeLabel=None,
    observedProperty=None,
    projection=None,
    period=None,
    stationLabel=None,
    stationRLOIid=None,
    parameter=None,
    station=None,
    notation=None,
    parameterName=None
    ):

        params = {}
        params['_limit'] = 5
        
        if label != None:
            params['label'] = label

        if unitName != None:
            params['unitName'] = unitName

        if offset != None:
            params['_offset'] = offset

        if datumType != None:
            params['datumType'] = datumType

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if observationType != None:
            params['observationType'] = observationType

        if unit != None:
            params['unit'] = unit

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if limit != None:
            params['_limit'] = limit

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if qualifier != None:
            params['qualifier'] = qualifier

        if sort != None:
            params['_sort'] = sort

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if projection != None:
            params['_projection'] = projection

        if period != None:
            params['period'] = period

        if stationLabel != None:
            params['station.label'] = stationLabel

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if parameter != None:
            params['parameter'] = parameter

        if station != None:
            params['station'] = station

        if notation != None:
            params['notation'] = notation

        if parameterName != None:
            params['parameterName'] = parameterName

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
    projection=None,
    id=None
    ):

        params = {}
        
        if projection != None:
            params['_projection'] = projection

        if id != None:
            params['id'] = id

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
    minDate=None,
    projection=None,
    date=None,
    measure=None,
    maxDate=None,
    maxeqDate=None,
    latest=None,
    mineqDate=None,
    earliest=None,
    view=None
    ):

        params = {}
        
        if minDate != None:
            params['min-date'] = minDate

        if projection != None:
            params['_projection'] = projection

        if date != None:
            params['date'] = date

        if measure != None:
            params['measure'] = measure

        if maxDate != None:
            params['max-date'] = maxDate

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if latest != None:
            params['latest'] = latest

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if earliest != None:
            params['earliest'] = earliest

        if view != None:
            params['view'] = view

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
    RLOIid=None,
    label=None,
    measuresPeriod=None,
    measuresObservedProperty=None,
    offset=None,
    dist=None,
    stationReference=None,
    type=None,
    statusLabel=None,
    nrfaStationURL=None,
    lat=None,
    limit=None,
    measuresValueStatistic=None,
    sampleOf=None,
    boreholeDepth=None,
    sort=None,
    town=None,
    search=None,
    measuresObservationType=None,
    observedProperty=None,
    projection=None,
    wiskiID=None,
    dateOpened=None,
    measuresObservedPropertyLabel=None,
    datum=None,
    northing=None,
    measuresUnitName=None,
    measuresLabel=None,
    measuresNotation=None,
    measuresValueStatisticLabel=None,
    notation=None,
    aquifer=None,
    easting=None,
    measures=None,
    status=None,
    sampleOfLabel=None,
    nrfaStationID=None,
    catchmentName=None,
    long=None,
    measuresQualifier=None,
    measuresObservationTypeLabel=None,
    riverName=None
    ):

        params = {}
        params['_limit'] = 5
        
        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if label != None:
            params['label'] = label

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if offset != None:
            params['_offset'] = offset

        if dist != None:
            params['dist'] = dist

        if stationReference != None:
            params['stationReference'] = stationReference

        if type != None:
            params['type'] = type

        if statusLabel != None:
            params['status.label'] = statusLabel

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if lat != None:
            params['lat'] = lat

        if limit != None:
            params['_limit'] = limit

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if sort != None:
            params['_sort'] = sort

        if town != None:
            params['town'] = town

        if search != None:
            params['search'] = search

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if projection != None:
            params['_projection'] = projection

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if datum != None:
            params['datum'] = datum

        if northing != None:
            params['northing'] = northing

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if notation != None:
            params['notation'] = notation

        if aquifer != None:
            params['aquifer'] = aquifer

        if easting != None:
            params['easting'] = easting

        if measures != None:
            params['measures'] = measures

        if status != None:
            params['status'] = status

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if long != None:
            params['long'] = long

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if riverName != None:
            params['riverName'] = riverName

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
    projection=None,
    id=None
    ):

        params = {}
        
        if projection != None:
            params['_projection'] = projection

        if id != None:
            params['id'] = id

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
    station=None,
    observationType=None,
    projection=None,
    observedProperty=None
    ):

        params = {}
        
        if station != None:
            params['station'] = station

        if observationType != None:
            params['observationType'] = observationType

        if projection != None:
            params['_projection'] = projection

        if observedProperty != None:
            params['observedProperty'] = observedProperty

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
