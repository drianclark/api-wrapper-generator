import requests

def ReadingsForOneOrMoreMeasureTimeSeries(
measure=None,
earliest=None,
value=None,
maxeqDate=None,
qcode=None,
period=None,
completeness=None,
dateTime=None,
limit=None,
sort=None,
observedProperty=None,
mineqDate=None,
offset=None,
station=None,
projection=None,
view=None,
stationStationReference=None,
date=None,
minDate=None,
observationType=None,
quality=None,
stationWiskiID=None,
latest=None,
maxDate=None,
stationRLOIid=None
):

    params = {}

    if measure != None:
        params['measure'] = measure

    if earliest != None:
        params['earliest'] = earliest

    if value != None:
        params['value'] = value

    if maxeqDate != None:
        params['maxeq-date'] = maxeqDate

    if qcode != None:
        params['qcode'] = qcode

    if period != None:
        params['period'] = period

    if completeness != None:
        params['completeness'] = completeness

    if dateTime != None:
        params['dateTime'] = dateTime

    if limit != None:
        params['_limit'] = limit

    if sort != None:
        params['_sort'] = sort

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if mineqDate != None:
        params['mineq-date'] = mineqDate

    if offset != None:
        params['_offset'] = offset

    if station != None:
        params['station'] = station

    if projection != None:
        params['_projection'] = projection

    if view != None:
        params['view'] = view

    if stationStationReference != None:
        params['station.stationReference'] = stationStationReference

    if date != None:
        params['date'] = date

    if minDate != None:
        params['min-date'] = minDate

    if observationType != None:
        params['observationType'] = observationType

    if quality != None:
        params['quality'] = quality

    if stationWiskiID != None:
        params['station.wiskiID'] = stationWiskiID

    if latest != None:
        params['latest'] = latest

    if maxDate != None:
        params['max-date'] = maxDate

    if stationRLOIid != None:
        params['station.RLOIid'] = stationRLOIid

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/data/readings', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = [Readings(item) for item in items]
    

    return data

def ListOfAllAvailableMeasurementTimeseriesInTheHydrologyDataset(
parameterName=None,
valueStatisticLabel=None,
label=None,
observationTypeLabel=None,
period=None,
limit=None,
sort=None,
observedProperty=None,
stationLabel=None,
offset=None,
valueStatistic=None,
station=None,
notation=None,
unit=None,
unitName=None,
projection=None,
stationStationReference=None,
observationType=None,
qualifier=None,
datumType=None,
parameter=None,
stationWiskiID=None,
observedPropertyLabel=None,
stationRLOIid=None
):

    params = {}

    if parameterName != None:
        params['parameterName'] = parameterName

    if valueStatisticLabel != None:
        params['valueStatistic.label'] = valueStatisticLabel

    if label != None:
        params['label'] = label

    if observationTypeLabel != None:
        params['observationType.label'] = observationTypeLabel

    if period != None:
        params['period'] = period

    if limit != None:
        params['_limit'] = limit

    if sort != None:
        params['_sort'] = sort

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if stationLabel != None:
        params['station.label'] = stationLabel

    if offset != None:
        params['_offset'] = offset

    if valueStatistic != None:
        params['valueStatistic'] = valueStatistic

    if station != None:
        params['station'] = station

    if notation != None:
        params['notation'] = notation

    if unit != None:
        params['unit'] = unit

    if unitName != None:
        params['unitName'] = unitName

    if projection != None:
        params['_projection'] = projection

    if stationStationReference != None:
        params['station.stationReference'] = stationStationReference

    if observationType != None:
        params['observationType'] = observationType

    if qualifier != None:
        params['qualifier'] = qualifier

    if datumType != None:
        params['datumType'] = datumType

    if parameter != None:
        params['parameter'] = parameter

    if stationWiskiID != None:
        params['station.wiskiID'] = stationWiskiID

    if observedPropertyLabel != None:
        params['observedProperty.label'] = observedPropertyLabel

    if stationRLOIid != None:
        params['station.RLOIid'] = stationRLOIid

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = [TimeSeries(item) for item in items]
    

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
    data = TimeSeries(items[0])
    

    return data

def ReadingsForASingleMeasureTimeseries(
date=None,
minDate=None,
measure=None,
projection=None,
earliest=None,
view=None,
latest=None,
maxeqDate=None,
mineqDate=None,
maxDate=None
):

    params = {}

    if date != None:
        params['date'] = date

    if minDate != None:
        params['min-date'] = minDate

    if measure != None:
        params['measure'] = measure

    if projection != None:
        params['_projection'] = projection

    if earliest != None:
        params['earliest'] = earliest

    if view != None:
        params['view'] = view

    if latest != None:
        params['latest'] = latest

    if maxeqDate != None:
        params['maxeq-date'] = maxeqDate

    if mineqDate != None:
        params['mineq-date'] = mineqDate

    if maxDate != None:
        params['max-date'] = maxDate

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{measure}/readings', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = Reading(items[0])
    

    return data

def ListOfAllMonitoringStationsCanBeFilteredByNameLocationAndOtherParameters(
sampleOf=None,
boreholeDepth=None,
easting=None,
stationReference=None,
measuresNotation=None,
nrfaStationURL=None,
measuresObservedPropertyLabel=None,
measuresPeriod=None,
measuresQualifier=None,
measuresObservationType=None,
dateOpened=None,
label=None,
lat=None,
status=None,
town=None,
measures=None,
measuresValueStatisticLabel=None,
measuresValueStatistic=None,
northing=None,
nrfaStationID=None,
RLOIid=None,
limit=None,
wiskiID=None,
sort=None,
riverName=None,
measuresObservedProperty=None,
observedProperty=None,
statusLabel=None,
type=None,
sampleOfLabel=None,
offset=None,
notation=None,
projection=None,
long=None,
measuresObservationTypeLabel=None,
search=None,
measuresUnitName=None,
dist=None,
aquifer=None,
catchmentName=None,
measuresLabel=None,
datum=None
):

    params = {}

    if sampleOf != None:
        params['sampleOf'] = sampleOf

    if boreholeDepth != None:
        params['boreholeDepth'] = boreholeDepth

    if easting != None:
        params['easting'] = easting

    if stationReference != None:
        params['stationReference'] = stationReference

    if measuresNotation != None:
        params['measures.notation'] = measuresNotation

    if nrfaStationURL != None:
        params['nrfaStationURL'] = nrfaStationURL

    if measuresObservedPropertyLabel != None:
        params['measures.observedProperty.label'] = measuresObservedPropertyLabel

    if measuresPeriod != None:
        params['measures.period'] = measuresPeriod

    if measuresQualifier != None:
        params['measures.qualifier'] = measuresQualifier

    if measuresObservationType != None:
        params['measures.observationType'] = measuresObservationType

    if dateOpened != None:
        params['dateOpened'] = dateOpened

    if label != None:
        params['label'] = label

    if lat != None:
        params['lat'] = lat

    if status != None:
        params['status'] = status

    if town != None:
        params['town'] = town

    if measures != None:
        params['measures'] = measures

    if measuresValueStatisticLabel != None:
        params['measures.valueStatistic.label'] = measuresValueStatisticLabel

    if measuresValueStatistic != None:
        params['measures.valueStatistic'] = measuresValueStatistic

    if northing != None:
        params['northing'] = northing

    if nrfaStationID != None:
        params['nrfaStationID'] = nrfaStationID

    if RLOIid != None:
        params['RLOIid'] = RLOIid

    if limit != None:
        params['_limit'] = limit

    if wiskiID != None:
        params['wiskiID'] = wiskiID

    if sort != None:
        params['_sort'] = sort

    if riverName != None:
        params['riverName'] = riverName

    if measuresObservedProperty != None:
        params['measures.observedProperty'] = measuresObservedProperty

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if statusLabel != None:
        params['status.label'] = statusLabel

    if type != None:
        params['type'] = type

    if sampleOfLabel != None:
        params['sampleOf.label'] = sampleOfLabel

    if offset != None:
        params['_offset'] = offset

    if notation != None:
        params['notation'] = notation

    if projection != None:
        params['_projection'] = projection

    if long != None:
        params['long'] = long

    if measuresObservationTypeLabel != None:
        params['measures.observationType.label'] = measuresObservationTypeLabel

    if search != None:
        params['search'] = search

    if measuresUnitName != None:
        params['measures.unitName'] = measuresUnitName

    if dist != None:
        params['dist'] = dist

    if aquifer != None:
        params['aquifer'] = aquifer

    if catchmentName != None:
        params['catchmentName'] = catchmentName

    if measuresLabel != None:
        params['measures.label'] = measuresLabel

    if datum != None:
        params['datum'] = datum

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = [Station(item) for item in items]
    

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
    data = Station(items[0])
    

    return data

def ListTheTimeseriesForAStation(
projection=None,
observationType=None,
station=None,
observedProperty=None
):

    params = {}

    if projection != None:
        params['_projection'] = projection

    if observationType != None:
        params['observationType'] = observationType

    if station != None:
        params['station'] = station

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    items = r.json()["items"]
    data = [TimeSeries(item) for item in items]
    

    return data
