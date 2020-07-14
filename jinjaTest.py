import requests

def ReadingsForOneOrMoreMeasureTimeSeries(
stationStationReference=None,
observationType=None,
earliest=None,
limit=None,
completeness=None,
dateTime=None,
mineqDate=None,
stationRLOIid=None,
projection=None,
latest=None,
quality=None,
maxeqDate=None,
observedProperty=None,
measure=None,
station=None,
offset=None,
value=None,
maxDate=None,
view=None,
date=None,
qcode=None,
period=None,
stationWiskiID=None,
minDate=None,
sort=None
):

    params = {}

    if stationStationReference != None:
        params['station.stationReference'] = stationStationReference

    if observationType != None:
        params['observationType'] = observationType

    if earliest != None:
        params['earliest'] = earliest

    if limit != None:
        params['_limit'] = limit

    if completeness != None:
        params['completeness'] = completeness

    if dateTime != None:
        params['dateTime'] = dateTime

    if mineqDate != None:
        params['mineq-date'] = mineqDate

    if stationRLOIid != None:
        params['station.RLOIid'] = stationRLOIid

    if projection != None:
        params['_projection'] = projection

    if latest != None:
        params['latest'] = latest

    if quality != None:
        params['quality'] = quality

    if maxeqDate != None:
        params['maxeq-date'] = maxeqDate

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if measure != None:
        params['measure'] = measure

    if station != None:
        params['station'] = station

    if offset != None:
        params['_offset'] = offset

    if value != None:
        params['value'] = value

    if maxDate != None:
        params['max-date'] = maxDate

    if view != None:
        params['view'] = view

    if date != None:
        params['date'] = date

    if qcode != None:
        params['qcode'] = qcode

    if period != None:
        params['period'] = period

    if stationWiskiID != None:
        params['station.wiskiID'] = stationWiskiID

    if minDate != None:
        params['min-date'] = minDate

    if sort != None:
        params['_sort'] = sort

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/data/readings', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()["items"]

    return data

def ListOfAllAvailableMeasurementTimeseriesInTheHydrologyDataset(
datumType=None,
stationStationReference=None,
observationType=None,
valueStatisticLabel=None,
limit=None,
observationTypeLabel=None,
unitName=None,
stationRLOIid=None,
observedPropertyLabel=None,
projection=None,
label=None,
valueStatistic=None,
parameterName=None,
notation=None,
observedProperty=None,
unit=None,
station=None,
parameter=None,
offset=None,
qualifier=None,
period=None,
stationWiskiID=None,
stationLabel=None,
sort=None
):

    params = {}

    if datumType != None:
        params['datumType'] = datumType

    if stationStationReference != None:
        params['station.stationReference'] = stationStationReference

    if observationType != None:
        params['observationType'] = observationType

    if valueStatisticLabel != None:
        params['valueStatistic.label'] = valueStatisticLabel

    if limit != None:
        params['_limit'] = limit

    if observationTypeLabel != None:
        params['observationType.label'] = observationTypeLabel

    if unitName != None:
        params['unitName'] = unitName

    if stationRLOIid != None:
        params['station.RLOIid'] = stationRLOIid

    if observedPropertyLabel != None:
        params['observedProperty.label'] = observedPropertyLabel

    if projection != None:
        params['_projection'] = projection

    if label != None:
        params['label'] = label

    if valueStatistic != None:
        params['valueStatistic'] = valueStatistic

    if parameterName != None:
        params['parameterName'] = parameterName

    if notation != None:
        params['notation'] = notation

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if unit != None:
        params['unit'] = unit

    if station != None:
        params['station'] = station

    if parameter != None:
        params['parameter'] = parameter

    if offset != None:
        params['_offset'] = offset

    if qualifier != None:
        params['qualifier'] = qualifier

    if period != None:
        params['period'] = period

    if stationWiskiID != None:
        params['station.wiskiID'] = stationWiskiID

    if stationLabel != None:
        params['station.label'] = stationLabel

    if sort != None:
        params['_sort'] = sort

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()["items"]

    return data

def DescriptionOfASingleMeasurementTimeseries(
id=None,
projection=None
):

    params = {}

    if id != None:
        params['id'] = id

    if projection != None:
        params['_projection'] = projection

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{id}', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()["items"]

    return data

def ReadingsForASingleMeasureTimeseries(
maxeqDate=None,
mineqDate=None,
measure=None,
maxDate=None,
view=None,
date=None,
earliest=None,
latest=None,
minDate=None,
projection=None
):

    params = {}

    if maxeqDate != None:
        params['maxeq-date'] = maxeqDate

    if mineqDate != None:
        params['mineq-date'] = mineqDate

    if measure != None:
        params['measure'] = measure

    if maxDate != None:
        params['max-date'] = maxDate

    if view != None:
        params['view'] = view

    if date != None:
        params['date'] = date

    if earliest != None:
        params['earliest'] = earliest

    if latest != None:
        params['latest'] = latest

    if minDate != None:
        params['min-date'] = minDate

    if projection != None:
        params['_projection'] = projection

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{measure}/readings', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()["items"]

    return data

def ListOfAllMonitoringStationsCanBeFilteredByNameLocationAndOtherParameters(
aquifer=None,
stationReference=None,
statusLabel=None,
measuresObservedPropertyLabel=None,
nrfaStationURL=None,
town=None,
measuresPeriod=None,
riverName=None,
measures=None,
measuresObservedProperty=None,
limit=None,
boreholeDepth=None,
measuresUnitName=None,
status=None,
dateOpened=None,
measuresNotation=None,
easting=None,
search=None,
measuresValueStatistic=None,
type=None,
projection=None,
label=None,
measuresQualifier=None,
datum=None,
dist=None,
lat=None,
catchmentName=None,
notation=None,
measuresValueStatisticLabel=None,
measuresLabel=None,
observedProperty=None,
RLOIid=None,
sampleOfLabel=None,
long=None,
measuresObservationType=None,
offset=None,
nrfaStationID=None,
sampleOf=None,
measuresObservationTypeLabel=None,
wiskiID=None,
northing=None,
sort=None
):

    params = {}

    if aquifer != None:
        params['aquifer'] = aquifer

    if stationReference != None:
        params['stationReference'] = stationReference

    if statusLabel != None:
        params['status.label'] = statusLabel

    if measuresObservedPropertyLabel != None:
        params['measures.observedProperty.label'] = measuresObservedPropertyLabel

    if nrfaStationURL != None:
        params['nrfaStationURL'] = nrfaStationURL

    if town != None:
        params['town'] = town

    if measuresPeriod != None:
        params['measures.period'] = measuresPeriod

    if riverName != None:
        params['riverName'] = riverName

    if measures != None:
        params['measures'] = measures

    if measuresObservedProperty != None:
        params['measures.observedProperty'] = measuresObservedProperty

    if limit != None:
        params['_limit'] = limit

    if boreholeDepth != None:
        params['boreholeDepth'] = boreholeDepth

    if measuresUnitName != None:
        params['measures.unitName'] = measuresUnitName

    if status != None:
        params['status'] = status

    if dateOpened != None:
        params['dateOpened'] = dateOpened

    if measuresNotation != None:
        params['measures.notation'] = measuresNotation

    if easting != None:
        params['easting'] = easting

    if search != None:
        params['search'] = search

    if measuresValueStatistic != None:
        params['measures.valueStatistic'] = measuresValueStatistic

    if type != None:
        params['type'] = type

    if projection != None:
        params['_projection'] = projection

    if label != None:
        params['label'] = label

    if measuresQualifier != None:
        params['measures.qualifier'] = measuresQualifier

    if datum != None:
        params['datum'] = datum

    if dist != None:
        params['dist'] = dist

    if lat != None:
        params['lat'] = lat

    if catchmentName != None:
        params['catchmentName'] = catchmentName

    if notation != None:
        params['notation'] = notation

    if measuresValueStatisticLabel != None:
        params['measures.valueStatistic.label'] = measuresValueStatisticLabel

    if measuresLabel != None:
        params['measures.label'] = measuresLabel

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if RLOIid != None:
        params['RLOIid'] = RLOIid

    if sampleOfLabel != None:
        params['sampleOf.label'] = sampleOfLabel

    if long != None:
        params['long'] = long

    if measuresObservationType != None:
        params['measures.observationType'] = measuresObservationType

    if offset != None:
        params['_offset'] = offset

    if nrfaStationID != None:
        params['nrfaStationID'] = nrfaStationID

    if sampleOf != None:
        params['sampleOf'] = sampleOf

    if measuresObservationTypeLabel != None:
        params['measures.observationType.label'] = measuresObservationTypeLabel

    if wiskiID != None:
        params['wiskiID'] = wiskiID

    if northing != None:
        params['northing'] = northing

    if sort != None:
        params['_sort'] = sort

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()["items"]

    return data

def DetailsForASingleMonitoringStation(
id=None,
projection=None
):

    params = {}

    if id != None:
        params['id'] = id

    if projection != None:
        params['_projection'] = projection

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{id}', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()["items"]

    return data

def ListTheTimeseriesForAStation(
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

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()["items"]

    return data
