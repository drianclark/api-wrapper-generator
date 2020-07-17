import requests

def ReadingsForOneOrMoreMeasureTimeSeries(
earliest=None,
station=None,
view=None,
period=None,
value=None,
projection=None,
minDate=None,
mineqDate=None,
stationRLOIid=None,
latest=None,
offset=None,
limit=None,
quality=None,
completeness=None,
maxeqDate=None,
observationType=None,
qcode=None,
observedProperty=None,
measure=None,
dateTime=None,
stationWiskiID=None,
stationStationReference=None,
sort=None,
date=None,
maxDate=None
):

    params = {}

    if earliest != None:
        params['earliest'] = earliest

    if station != None:
        params['station'] = station

    if view != None:
        params['view'] = view

    if period != None:
        params['period'] = period

    if value != None:
        params['value'] = value

    if projection != None:
        params['_projection'] = projection

    if minDate != None:
        params['min-date'] = minDate

    if mineqDate != None:
        params['mineq-date'] = mineqDate

    if stationRLOIid != None:
        params['station.RLOIid'] = stationRLOIid

    if latest != None:
        params['latest'] = latest

    if offset != None:
        params['_offset'] = offset

    if limit != None:
        params['_limit'] = limit

    if quality != None:
        params['quality'] = quality

    if completeness != None:
        params['completeness'] = completeness

    if maxeqDate != None:
        params['maxeq-date'] = maxeqDate

    if observationType != None:
        params['observationType'] = observationType

    if qcode != None:
        params['qcode'] = qcode

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if measure != None:
        params['measure'] = measure

    if dateTime != None:
        params['dateTime'] = dateTime

    if stationWiskiID != None:
        params['station.wiskiID'] = stationWiskiID

    if stationStationReference != None:
        params['station.stationReference'] = stationStationReference

    if sort != None:
        params['_sort'] = sort

    if date != None:
        params['date'] = date

    if maxDate != None:
        params['max-date'] = maxDate

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/data/readings', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()

    return data

def ListOfAllAvailableMeasurementTimeseriesInTheHydrologyDataset(
notation=None,
station=None,
unit=None,
period=None,
observationTypeLabel=None,
projection=None,
label=None,
parameter=None,
stationRLOIid=None,
valueStatistic=None,
stationLabel=None,
observedPropertyLabel=None,
valueStatisticLabel=None,
offset=None,
limit=None,
observationType=None,
observedProperty=None,
parameterName=None,
stationWiskiID=None,
unitName=None,
qualifier=None,
stationStationReference=None,
sort=None,
datumType=None
):

    params = {}

    if notation != None:
        params['notation'] = notation

    if station != None:
        params['station'] = station

    if unit != None:
        params['unit'] = unit

    if period != None:
        params['period'] = period

    if observationTypeLabel != None:
        params['observationType.label'] = observationTypeLabel

    if projection != None:
        params['_projection'] = projection

    if label != None:
        params['label'] = label

    if parameter != None:
        params['parameter'] = parameter

    if stationRLOIid != None:
        params['station.RLOIid'] = stationRLOIid

    if valueStatistic != None:
        params['valueStatistic'] = valueStatistic

    if stationLabel != None:
        params['station.label'] = stationLabel

    if observedPropertyLabel != None:
        params['observedProperty.label'] = observedPropertyLabel

    if valueStatisticLabel != None:
        params['valueStatistic.label'] = valueStatisticLabel

    if offset != None:
        params['_offset'] = offset

    if limit != None:
        params['_limit'] = limit

    if observationType != None:
        params['observationType'] = observationType

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if parameterName != None:
        params['parameterName'] = parameterName

    if stationWiskiID != None:
        params['station.wiskiID'] = stationWiskiID

    if unitName != None:
        params['unitName'] = unitName

    if qualifier != None:
        params['qualifier'] = qualifier

    if stationStationReference != None:
        params['station.stationReference'] = stationStationReference

    if sort != None:
        params['_sort'] = sort

    if datumType != None:
        params['datumType'] = datumType

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()

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

    data = r.json()

    return data

def ReadingsForASingleMeasureTimeseries(
mineqDate=None,
maxeqDate=None,
earliest=None,
view=None,
measure=None,
projection=None,
latest=None,
date=None,
maxDate=None,
minDate=None
):

    params = {}

    if mineqDate != None:
        params['mineq-date'] = mineqDate

    if maxeqDate != None:
        params['maxeq-date'] = maxeqDate

    if earliest != None:
        params['earliest'] = earliest

    if view != None:
        params['view'] = view

    if measure != None:
        params['measure'] = measure

    if projection != None:
        params['_projection'] = projection

    if latest != None:
        params['latest'] = latest

    if date != None:
        params['date'] = date

    if maxDate != None:
        params['max-date'] = maxDate

    if minDate != None:
        params['min-date'] = minDate

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/measures/{measure}/readings', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()

    return data

def ListOfAllMonitoringStationsCanBeFilteredByNameLocationAndOtherParameters(
easting=None,
datum=None,
status=None,
notation=None,
type=None,
measuresObservedPropertyLabel=None,
catchmentName=None,
nrfaStationURL=None,
projection=None,
measuresValueStatistic=None,
measures=None,
lat=None,
measuresObservedProperty=None,
riverName=None,
measuresValueStatisticLabel=None,
label=None,
aquifer=None,
measuresLabel=None,
statusLabel=None,
sampleOf=None,
offset=None,
limit=None,
stationReference=None,
measuresPeriod=None,
measuresUnitName=None,
sampleOfLabel=None,
measuresQualifier=None,
observedProperty=None,
measuresObservationTypeLabel=None,
measuresNotation=None,
northing=None,
wiskiID=None,
long=None,
boreholeDepth=None,
town=None,
nrfaStationID=None,
sort=None,
dateOpened=None,
measuresObservationType=None,
dist=None,
RLOIid=None,
search=None
):

    params = {}

    if easting != None:
        params['easting'] = easting

    if datum != None:
        params['datum'] = datum

    if status != None:
        params['status'] = status

    if notation != None:
        params['notation'] = notation

    if type != None:
        params['type'] = type

    if measuresObservedPropertyLabel != None:
        params['measures.observedProperty.label'] = measuresObservedPropertyLabel

    if catchmentName != None:
        params['catchmentName'] = catchmentName

    if nrfaStationURL != None:
        params['nrfaStationURL'] = nrfaStationURL

    if projection != None:
        params['_projection'] = projection

    if measuresValueStatistic != None:
        params['measures.valueStatistic'] = measuresValueStatistic

    if measures != None:
        params['measures'] = measures

    if lat != None:
        params['lat'] = lat

    if measuresObservedProperty != None:
        params['measures.observedProperty'] = measuresObservedProperty

    if riverName != None:
        params['riverName'] = riverName

    if measuresValueStatisticLabel != None:
        params['measures.valueStatistic.label'] = measuresValueStatisticLabel

    if label != None:
        params['label'] = label

    if aquifer != None:
        params['aquifer'] = aquifer

    if measuresLabel != None:
        params['measures.label'] = measuresLabel

    if statusLabel != None:
        params['status.label'] = statusLabel

    if sampleOf != None:
        params['sampleOf'] = sampleOf

    if offset != None:
        params['_offset'] = offset

    if limit != None:
        params['_limit'] = limit

    if stationReference != None:
        params['stationReference'] = stationReference

    if measuresPeriod != None:
        params['measures.period'] = measuresPeriod

    if measuresUnitName != None:
        params['measures.unitName'] = measuresUnitName

    if sampleOfLabel != None:
        params['sampleOf.label'] = sampleOfLabel

    if measuresQualifier != None:
        params['measures.qualifier'] = measuresQualifier

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if measuresObservationTypeLabel != None:
        params['measures.observationType.label'] = measuresObservationTypeLabel

    if measuresNotation != None:
        params['measures.notation'] = measuresNotation

    if northing != None:
        params['northing'] = northing

    if wiskiID != None:
        params['wiskiID'] = wiskiID

    if long != None:
        params['long'] = long

    if boreholeDepth != None:
        params['boreholeDepth'] = boreholeDepth

    if town != None:
        params['town'] = town

    if nrfaStationID != None:
        params['nrfaStationID'] = nrfaStationID

    if sort != None:
        params['_sort'] = sort

    if dateOpened != None:
        params['dateOpened'] = dateOpened

    if measuresObservationType != None:
        params['measures.observationType'] = measuresObservationType

    if dist != None:
        params['dist'] = dist

    if RLOIid != None:
        params['RLOIid'] = RLOIid

    if search != None:
        params['search'] = search

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()

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

    data = r.json()

    return data

def ListTheTimeseriesForAStation(
station=None,
projection=None,
observedProperty=None,
observationType=None
):

    params = {}

    if station != None:
        params['station'] = station

    if projection != None:
        params['_projection'] = projection

    if observedProperty != None:
        params['observedProperty'] = observedProperty

    if observationType != None:
        params['observationType'] = observationType

    try:
        r = requests.get('https://environment.data.gov.uk/hydrology/id/stations/{station}/measures', params=params)
        r.raise_for_status()

    except:
        raise ValueError("Request failed")

    data = r.json()

    return data
