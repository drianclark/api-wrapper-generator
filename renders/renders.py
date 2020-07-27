import requests
from Stations import Stations
from Measures import Measures
from Readings import Readings

class Renders:

    def readings(
    self, 
    date=None,
    projection=None,
    latest=None,
    period=None,
    completeness=None,
    stationStationReference=None,
    observedProperty=None,
    observationType=None,
    measure=None,
    station=None,
    value=None,
    maxeqDate=None,
    earliest=None,
    stationRLOIid=None,
    quality=None,
    minDate=None,
    qcode=None,
    view=None,
    maxDate=None,
    sort=None,
    dateTime=None,
    offset=None,
    mineqDate=None,
    stationWiskiID=None,
    limit=None
    ):

        params = {}
        params['_limit'] = 5
        
        if date != None:
            params['date'] = date

        if projection != None:
            params['_projection'] = projection

        if latest != None:
            params['latest'] = latest

        if period != None:
            params['period'] = period

        if completeness != None:
            params['completeness'] = completeness

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if observationType != None:
            params['observationType'] = observationType

        if measure != None:
            params['measure'] = measure

        if station != None:
            params['station'] = station

        if value != None:
            params['value'] = value

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if earliest != None:
            params['earliest'] = earliest

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if quality != None:
            params['quality'] = quality

        if minDate != None:
            params['min-date'] = minDate

        if qcode != None:
            params['qcode'] = qcode

        if view != None:
            params['view'] = view

        if maxDate != None:
            params['max-date'] = maxDate

        if sort != None:
            params['_sort'] = sort

        if dateTime != None:
            params['dateTime'] = dateTime

        if offset != None:
            params['_offset'] = offset

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if limit != None:
            params['_limit'] = limit


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/data/readings.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = [Readings(item) for item in items]
        

        return data

    def measures(
    self, 
    label=None,
    stationLabel=None,
    projection=None,
    qualifier=None,
    period=None,
    valueStatisticLabel=None,
    observedPropertyLabel=None,
    unitName=None,
    observedProperty=None,
    observationTypeLabel=None,
    stationStationReference=None,
    observationType=None,
    parameterName=None,
    station=None,
    unit=None,
    stationRLOIid=None,
    valueStatistic=None,
    parameter=None,
    sort=None,
    offset=None,
    datumType=None,
    stationWiskiID=None,
    limit=None,
    notation=None
    ):

        params = {}
        params['_limit'] = 5
        
        if label != None:
            params['label'] = label

        if stationLabel != None:
            params['station.label'] = stationLabel

        if projection != None:
            params['_projection'] = projection

        if qualifier != None:
            params['qualifier'] = qualifier

        if period != None:
            params['period'] = period

        if valueStatisticLabel != None:
            params['valueStatistic.label'] = valueStatisticLabel

        if observedPropertyLabel != None:
            params['observedProperty.label'] = observedPropertyLabel

        if unitName != None:
            params['unitName'] = unitName

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if observationTypeLabel != None:
            params['observationType.label'] = observationTypeLabel

        if stationStationReference != None:
            params['station.stationReference'] = stationStationReference

        if observationType != None:
            params['observationType'] = observationType

        if parameterName != None:
            params['parameterName'] = parameterName

        if station != None:
            params['station'] = station

        if unit != None:
            params['unit'] = unit

        if stationRLOIid != None:
            params['station.RLOIid'] = stationRLOIid

        if valueStatistic != None:
            params['valueStatistic'] = valueStatistic

        if parameter != None:
            params['parameter'] = parameter

        if sort != None:
            params['_sort'] = sort

        if offset != None:
            params['_offset'] = offset

        if datumType != None:
            params['datumType'] = datumType

        if stationWiskiID != None:
            params['station.wiskiID'] = stationWiskiID

        if limit != None:
            params['_limit'] = limit

        if notation != None:
            params['notation'] = notation


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = [Measures(item) for item in items]
        

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
        data = Measures(items[0])
        

        return data

    def readingsByMeasure(
    self, 
    maxDate=None,
    date=None,
    projection=None,
    latest=None,
    measure=None,
    minDate=None,
    mineqDate=None,
    view=None,
    maxeqDate=None,
    earliest=None
    ):

        params = {}
        
        if maxDate != None:
            params['max-date'] = maxDate

        if date != None:
            params['date'] = date

        if projection != None:
            params['_projection'] = projection

        if latest != None:
            params['latest'] = latest

        if measure != None:
            params['measure'] = measure

        if minDate != None:
            params['min-date'] = minDate

        if mineqDate != None:
            params['mineq-date'] = mineqDate

        if view != None:
            params['view'] = view

        if maxeqDate != None:
            params['maxeq-date'] = maxeqDate

        if earliest != None:
            params['earliest'] = earliest


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{measure}/readings.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Readings(items[0])
        

        return data

    def stations(
    self, 
    catchmentName=None,
    label=None,
    projection=None,
    status=None,
    statusLabel=None,
    dist=None,
    sampleOfLabel=None,
    boreholeDepth=None,
    measuresObservationType=None,
    easting=None,
    northing=None,
    measuresLabel=None,
    nrfaStationURL=None,
    search=None,
    measuresPeriod=None,
    observedProperty=None,
    measures=None,
    dateOpened=None,
    datum=None,
    town=None,
    notation=None,
    measuresValueStatistic=None,
    wiskiID=None,
    lat=None,
    RLOIid=None,
    sampleOf=None,
    nrfaStationID=None,
    measuresQualifier=None,
    aquifer=None,
    measuresValueStatisticLabel=None,
    measuresObservationTypeLabel=None,
    type=None,
    long=None,
    measuresObservedProperty=None,
    stationReference=None,
    sort=None,
    offset=None,
    riverName=None,
    measuresUnitName=None,
    measuresNotation=None,
    limit=None,
    measuresObservedPropertyLabel=None
    ):

        params = {}
        params['_limit'] = 5
        
        if catchmentName != None:
            params['catchmentName'] = catchmentName

        if label != None:
            params['label'] = label

        if projection != None:
            params['_projection'] = projection

        if status != None:
            params['status'] = status

        if statusLabel != None:
            params['status.label'] = statusLabel

        if dist != None:
            params['dist'] = dist

        if sampleOfLabel != None:
            params['sampleOf.label'] = sampleOfLabel

        if boreholeDepth != None:
            params['boreholeDepth'] = boreholeDepth

        if measuresObservationType != None:
            params['measures.observationType'] = measuresObservationType

        if easting != None:
            params['easting'] = easting

        if northing != None:
            params['northing'] = northing

        if measuresLabel != None:
            params['measures.label'] = measuresLabel

        if nrfaStationURL != None:
            params['nrfaStationURL'] = nrfaStationURL

        if search != None:
            params['search'] = search

        if measuresPeriod != None:
            params['measures.period'] = measuresPeriod

        if observedProperty != None:
            params['observedProperty'] = observedProperty

        if measures != None:
            params['measures'] = measures

        if dateOpened != None:
            params['dateOpened'] = dateOpened

        if datum != None:
            params['datum'] = datum

        if town != None:
            params['town'] = town

        if notation != None:
            params['notation'] = notation

        if measuresValueStatistic != None:
            params['measures.valueStatistic'] = measuresValueStatistic

        if wiskiID != None:
            params['wiskiID'] = wiskiID

        if lat != None:
            params['lat'] = lat

        if RLOIid != None:
            params['RLOIid'] = RLOIid

        if sampleOf != None:
            params['sampleOf'] = sampleOf

        if nrfaStationID != None:
            params['nrfaStationID'] = nrfaStationID

        if measuresQualifier != None:
            params['measures.qualifier'] = measuresQualifier

        if aquifer != None:
            params['aquifer'] = aquifer

        if measuresValueStatisticLabel != None:
            params['measures.valueStatistic.label'] = measuresValueStatisticLabel

        if measuresObservationTypeLabel != None:
            params['measures.observationType.label'] = measuresObservationTypeLabel

        if type != None:
            params['type'] = type

        if long != None:
            params['long'] = long

        if measuresObservedProperty != None:
            params['measures.observedProperty'] = measuresObservedProperty

        if stationReference != None:
            params['stationReference'] = stationReference

        if sort != None:
            params['_sort'] = sort

        if offset != None:
            params['_offset'] = offset

        if riverName != None:
            params['riverName'] = riverName

        if measuresUnitName != None:
            params['measures.unitName'] = measuresUnitName

        if measuresNotation != None:
            params['measures.notation'] = measuresNotation

        if limit != None:
            params['_limit'] = limit

        if measuresObservedPropertyLabel != None:
            params['measures.observedProperty.label'] = measuresObservedPropertyLabel


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = [Stations(item) for item in items]
        

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
        data = Stations(items[0])
        

        return data

    def measuresByStation(
    self, 
    observationType=None,
    projection=None,
    station=None,
    observedProperty=None
    ):

        params = {}
        
        if observationType != None:
            params['observationType'] = observationType

        if projection != None:
            params['_projection'] = projection

        if station != None:
            params['station'] = station

        if observedProperty != None:
            params['observedProperty'] = observedProperty


        try:
            r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures.json', params=params)
            r.raise_for_status()

        except:
            raise ValueError("Request failed")

        items = r.json()["items"]
        data = Measures(items[0])
        

        return data
