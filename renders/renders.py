import requests

def ReadingsForOneOrMoreMeasureTimeSeries(
value=None,
stationRLOIid=None,
stationStationReference=None,
observationType=None,
quality=None,
latest=None,
maxDate=None,
limit=None,
observedProperty=None,
view=None,
mineqDate=None,
completeness=None,
earliest=None,
offset=None,
dateTime=None,
station=None,
maxeqDate=None,
date=None,
period=None,
qcode=None,
stationWiskiID=None,
measure=None,
projection=None,
sort=None,
minDate=None
):

    params = {}

    if value != None:
        params['value'] = value

    if stationRLOIid != None:
        params['station.RLOIid'] = stationRLOIid

    if stationStationReference != None:
        params['station.stationReference'] = stationStationReference

    if observationType != None:
        params['observationType'] = observationType

    if quality != None:
        params['quality'] = quality

    if latest != None:
        params['latest'] = latest

    if maxDate != None:
        params['max-date'] = maxDate

    if limit != None:
        params['_limit'] = limit

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if view != None:
        params['view'] = view

    if mineqDate != None:
        params['mineq-date'] = mineqDate

    if completeness != None:
        params['completeness'] = completeness

    if earliest != None:
        params['earliest'] = earliest

    if offset != None:
        params['_offset'] = offset

    if dateTime != None:
        params['dateTime'] = dateTime

    if station != None:
        params['station'] = station

    if maxeqDate != None:
        params['maxeq-date'] = maxeqDate

    if date != None:
        params['date'] = date

    if period != None:
        params['period'] = period

    if qcode != None:
        params['qcode'] = qcode

    if stationWiskiID != None:
        params['station.wiskiID'] = stationWiskiID

    if measure != None:
        params['measure'] = measure

    if projection != None:
        params['_projection'] = projection

    if sort != None:
        params['_sort'] = sort

    if minDate != None:
        params['min-date'] = minDate

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/data/readings', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = [Readings(item) for item in items]
    

    return data

def ListOfAllAvailableMeasurementTimeseriesInTheHydrologyDataset(
unitName=None,
stationRLOIid=None,
observationType=None,
qualifier=None,
stationStationReference=None,
label=None,
observationTypeLabel=None,
stationLabel=None,
limit=None,
observedProperty=None,
offset=None,
datumType=None,
parameterName=None,
station=None,
notation=None,
observedPropertyLabel=None,
valueStatisticLabel=None,
period=None,
unit=None,
stationWiskiID=None,
valueStatistic=None,
projection=None,
sort=None,
parameter=None
):

    params = {}

    if unitName != None:
        params['unitName'] = unitName

    if stationRLOIid != None:
        params['station.RLOIid'] = stationRLOIid

    if observationType != None:
        params['observationType'] = observationType

    if qualifier != None:
        params['qualifier'] = qualifier

    if stationStationReference != None:
        params['station.stationReference'] = stationStationReference

    if label != None:
        params['label'] = label

    if observationTypeLabel != None:
        params['observationType.label'] = observationTypeLabel

    if stationLabel != None:
        params['station.label'] = stationLabel

    if limit != None:
        params['_limit'] = limit

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if offset != None:
        params['_offset'] = offset

    if datumType != None:
        params['datumType'] = datumType

    if parameterName != None:
        params['parameterName'] = parameterName

    if station != None:
        params['station'] = station

    if notation != None:
        params['notation'] = notation

    if observedPropertyLabel != None:
        params['observedProperty.label'] = observedPropertyLabel

    if valueStatisticLabel != None:
        params['valueStatistic.label'] = valueStatisticLabel

    if period != None:
        params['period'] = period

    if unit != None:
        params['unit'] = unit

    if stationWiskiID != None:
        params['station.wiskiID'] = stationWiskiID

    if valueStatistic != None:
        params['valueStatistic'] = valueStatistic

    if projection != None:
        params['_projection'] = projection

    if sort != None:
        params['_sort'] = sort

    if parameter != None:
        params['parameter'] = parameter

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = [Measures(item) for item in items]
    

    return data

def DescriptionOfASingleMeasurementTimeseries(
projection=None,
id=None
):

    params = {}

    if projection != None:
        params['_projection'] = projection

    if id != None:
        params['id'] = id

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{id}', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = Measures(items[0])
    

    return data

def ReadingsForASingleMeasureTimeseries(
view=None,
maxeqDate=None,
date=None,
maxDate=None,
mineqDate=None,
measure=None,
projection=None,
earliest=None,
latest=None,
minDate=None
):

    params = {}

    if view != None:
        params['view'] = view

    if maxeqDate != None:
        params['maxeq-date'] = maxeqDate

    if date != None:
        params['date'] = date

    if maxDate != None:
        params['max-date'] = maxDate

    if mineqDate != None:
        params['mineq-date'] = mineqDate

    if measure != None:
        params['measure'] = measure

    if projection != None:
        params['_projection'] = projection

    if earliest != None:
        params['earliest'] = earliest

    if latest != None:
        params['latest'] = latest

    if minDate != None:
        params['min-date'] = minDate

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{measure}/readings', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = Readings(items[0])
    

    return data

def ListOfAllMonitoringStationsCanBeFilteredByNameLocationAndOtherParameters(
measuresValueStatisticLabel=None,
nrfaStationURL=None,
RLOIid=None,
aquifer=None,
measuresObservationTypeLabel=None,
measuresQualifier=None,
northing=None,
nrfaStationID=None,
measures=None,
label=None,
boreholeDepth=None,
limit=None,
catchmentName=None,
measuresValueStatistic=None,
observedProperty=None,
type=None,
dateOpened=None,
datum=None,
town=None,
measuresUnitName=None,
offset=None,
search=None,
sampleOf=None,
notation=None,
riverName=None,
measuresPeriod=None,
measuresObservedProperty=None,
lat=None,
dist=None,
stationReference=None,
wiskiID=None,
measuresObservationType=None,
statusLabel=None,
easting=None,
status=None,
sampleOfLabel=None,
measuresObservedPropertyLabel=None,
measuresNotation=None,
projection=None,
sort=None,
long=None,
measuresLabel=None
):

    params = {}

    if measuresValueStatisticLabel != None:
        params['measures.valueStatistic.label'] = measuresValueStatisticLabel

    if nrfaStationURL != None:
        params['nrfaStationURL'] = nrfaStationURL

    if RLOIid != None:
        params['RLOIid'] = RLOIid

    if aquifer != None:
        params['aquifer'] = aquifer

    if measuresObservationTypeLabel != None:
        params['measures.observationType.label'] = measuresObservationTypeLabel

    if measuresQualifier != None:
        params['measures.qualifier'] = measuresQualifier

    if northing != None:
        params['northing'] = northing

    if nrfaStationID != None:
        params['nrfaStationID'] = nrfaStationID

    if measures != None:
        params['measures'] = measures

    if label != None:
        params['label'] = label

    if boreholeDepth != None:
        params['boreholeDepth'] = boreholeDepth

    if limit != None:
        params['_limit'] = limit

    if catchmentName != None:
        params['catchmentName'] = catchmentName

    if measuresValueStatistic != None:
        params['measures.valueStatistic'] = measuresValueStatistic

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if type != None:
        params['type'] = type

    if dateOpened != None:
        params['dateOpened'] = dateOpened

    if datum != None:
        params['datum'] = datum

    if town != None:
        params['town'] = town

    if measuresUnitName != None:
        params['measures.unitName'] = measuresUnitName

    if offset != None:
        params['_offset'] = offset

    if search != None:
        params['search'] = search

    if sampleOf != None:
        params['sampleOf'] = sampleOf

    if notation != None:
        params['notation'] = notation

    if riverName != None:
        params['riverName'] = riverName

    if measuresPeriod != None:
        params['measures.period'] = measuresPeriod

    if measuresObservedProperty != None:
        params['measures.observedProperty'] = measuresObservedProperty

    if lat != None:
        params['lat'] = lat

    if dist != None:
        params['dist'] = dist

    if stationReference != None:
        params['stationReference'] = stationReference

    if wiskiID != None:
        params['wiskiID'] = wiskiID

    if measuresObservationType != None:
        params['measures.observationType'] = measuresObservationType

    if statusLabel != None:
        params['status.label'] = statusLabel

    if easting != None:
        params['easting'] = easting

    if status != None:
        params['status'] = status

    if sampleOfLabel != None:
        params['sampleOf.label'] = sampleOfLabel

    if measuresObservedPropertyLabel != None:
        params['measures.observedProperty.label'] = measuresObservedPropertyLabel

    if measuresNotation != None:
        params['measures.notation'] = measuresNotation

    if projection != None:
        params['_projection'] = projection

    if sort != None:
        params['_sort'] = sort

    if long != None:
        params['long'] = long

    if measuresLabel != None:
        params['measures.label'] = measuresLabel

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = [Stations(item) for item in items]
    

    return data

def DetailsForASingleMonitoringStation(
projection=None,
id=None
):

    params = {}

    if projection != None:
        params['_projection'] = projection

    if id != None:
        params['id'] = id

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{id}', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = Stations(items[0])
    

    return data

def ListTheTimeseriesForAStation(
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
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = Measures(items[0])
    

    return data
