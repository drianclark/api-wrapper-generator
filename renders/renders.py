import requests
from renders.Reading import Reading
from renders.Station import Station
from renders.Measure import Measure

class Renders:

    def readings(
    self,
    exists=[],
    stationWiskiID=None,
    projection=None,
    completeness=None,
    quality=None,
    qcode=None,
    latest=None,
    period=None,
    stationRLOIid=None,
    observedProperty=None,
    dateTime=None,
    maxeqDate=None,
    earliest=None,
    offset=None,
    minDate=None,
    observationType=None,
    limit=None,
    maxDate=None,
    date=None,
    station=None,
    sort=None,
    mineqDate=None,
    value=None,
    stationStationReference=None,
    view=None,
    measure=None
    ):

        params = {}
        params['_limit'] = 5
        
        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if projection != None:
            params['_projection'] = projection

        if completeness != None:
            params['completeness'] = completeness

        if quality != None:
            params['quality'] = quality

        if qcode != None:
            params['qcode'] = qcode

        if latest != None:
            params['latest'] = latest

        if period != None:
            params['period'] = period

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if dateTime != None:
            params['dateTime'] = dateTime

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if earliest != None:
            params['earliest'] = earliest

        if offset != None:
            params['_offset'] = offset

        if minDate != None:
            params['min-date'] = minDate

        if observationType != None:
            params['observationType'] = observationType

        if limit != None:
            params['_limit'] = limit

        if maxDate != None:
            params['max-date'] = maxDate

        if date != None:
            params['date'] = date

        if station != None:
            params['station'] = station

        if sort != None:
            params['_sort'] = sort

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if value != None:
            params['value'] = value

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if view != None:
            params['view'] = view

        if measure != None:
            params['measure'] = measure

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

        try:
            r = requests.get('https://hydrology-test.epimorphics.net/hydrology/data/readings.json', params=params)
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
    stationWiskiID=None,
    projection=None,
    observationTypeLabel=None,
    notation=None,
    unit=None,
    datumType=None,
    period=None,
    stationRLOIid=None,
    observedProperty=None,
    unitName=None,
    parameter=None,
    offset=None,
    observationType=None,
    observedPropertyLabel=None,
    parameterName=None,
    limit=None,
    stationLabel=None,
    qualifier=None,
    station=None,
    valueStatistic=None,
    sort=None,
    stationStationReference=None,
    valueStatisticLabel=None
    ):

        params = {}
        params['_limit'] = 5
        
        if label != None:
            params['label'] = label

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if projection != None:
            params['_projection'] = projection

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if notation != None:
            params['notation'] = notation

        if unit != None:
            params['unit'] = unit

        if datumType != None:
            params['datumType'] = datumType

        if period != None:
            params['period'] = period

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if unitName != None:
            params['unitName'] = unitName

        if parameter != None:
            params['parameter'] = parameter

        if offset != None:
            params['_offset'] = offset

        if observationType != None:
            params['observationType'] = observationType

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if parameterName != None:
            params['parameterName'] = parameterName

        if limit != None:
            params['_limit'] = limit

        if stationLabel != None:
            params['station.label'] = stationLabel

        if qualifier != None:
            params['qualifier'] = qualifier

        if station != None:
            params['station'] = station

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if sort != None:
            params['_sort'] = sort

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

        try:
            r = requests.get('https://hydrology-test.epimorphics.net/hydrology/id/measures.json', params=params)
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
            r = requests.get('https://hydrology-test.epimorphics.net/hydrology/id/measures/{id}.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measure(items[0])
        

        return data

    def readingsByMeasure(
    self,
    exists=[],
    maxDate=None,
    date=None,
    latest=None,
    projection=None,
    minDate=None,
    mineqDate=None,
    maxeqDate=None,
    view=None,
    measure=None,
    earliest=None
    ):

        params = {}
        
        if maxDate != None:
            params['max-date'] = maxDate

        if date != None:
            params['date'] = date

        if latest != None:
            params['latest'] = latest

        if projection != None:
            params['_projection'] = projection

        if minDate != None:
            params['min-date'] = minDate

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if view != None:
            params['view'] = view

        if measure != None:
            params['measure'] = measure

        if earliest != None:
            params['earliest'] = earliest

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

        try:
            r = requests.get('https://hydrology-test.epimorphics.net/hydrology/id/measures/{measure}/readings.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Reading(items[0])
        

        return data

    def stations(
    self,
    exists=[],
    measuresNotation=None,
    measuresLabel=None,
    label=None,
    RLOIid=None,
    measuresObservedPropertyLabel=None,
    status=None,
    projection=None,
    notation=None,
    dateOpened=None,
    aquifer=None,
    stationReference=None,
    measuresValueStatistic=None,
    town=None,
    type=None,
    easting=None,
    boreholeDepth=None,
    observedProperty=None,
    sampleOf=None,
    measuresUnitName=None,
    measuresValueStatisticLabel=None,
    measuresQualifier=None,
    datum=None,
    measuresObservedProperty=None,
    offset=None,
    nrfaStationID=None,
    wiskiID=None,
    sampleOfLabel=None,
    long=None,
    nrfaStationURL=None,
    statusLabel=None,
    limit=None,
    measuresObservationType=None,
    catchmentName=None,
    measuresObservationTypeLabel=None,
    sort=None,
    measures=None,
    lat=None,
    riverName=None,
    search=None,
    dist=None,
    northing=None,
    measuresPeriod=None
    ):

        params = {}
        params['_limit'] = 5
        
        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if label != None:
            params['label'] = label

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel

        if status != None:
            params['status'] = status

        if projection != None:
            params['_projection'] = projection

        if notation != None:
            params['notation'] = notation

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if aquifer != None:
            params['aquifer'] = aquifer

        if stationReference != None:
            params['stationReference'] = stationReference

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if town != None:
            params['town'] = town

        if type != None:
            params['type'] = type

        if easting != None:
            params['easting'] = easting

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if datum != None:
            params['datum'] = datum

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if offset != None:
            params['_offset'] = offset

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if long != None:
            params['long'] = long

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if statusLabel != None:
            params['status.label'] = statusLabel

        if limit != None:
            params['_limit'] = limit

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if sort != None:
            params['_sort'] = sort

        if measures != None:
            params['measures'] = measures

        if lat != None:
            params['lat'] = lat

        if riverName != None:
            params['riverName'] = riverName

        if search != None:
            params['search'] = search

        if dist != None:
            params['dist'] = dist

        if northing != None:
            params['northing'] = northing

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

        try:
            r = requests.get('https://hydrology-test.epimorphics.net/hydrology/id/stations.json', params=params)
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
            r = requests.get('https://hydrology-test.epimorphics.net/hydrology/id/stations/{id}.json', params=params)
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
    station=None,
    observationType=None,
    projection=None
    ):

        params = {}
        
        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if station != None:
            params['station'] = station

        if observationType != None:
            params['observationType'] = observationType

        if projection != None:
            params['_projection'] = projection

        for prop in exists:
            params[f'exists-{prop}'] = 'true'

        try:
            r = requests.get('https://hydrology-test.epimorphics.net/hydrology/id/stations/{station}/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measure(items[0])
        

        return data
