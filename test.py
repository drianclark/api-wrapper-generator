import requests


def ReadingsForOneOrMoreMeasureTimeSeries(
completeness=None,
date=None,
dateTime=None,
measure=None,
qcode=None,
quality=None,
value=None,
minDate=None,
mineqDate=None,
maxDate=None,
maxeqDate=None,
earliest=None,
latest=None,
station=None,
stationRLOIid=None,
stationWiskiID=None,
stationStationReference=None,
observationType=None,
observedProperty=None,
period=None,
_offset=None,
_limit=None,
_sort=None,
_projection=None):
    
    parameters = {}
                
    if completeness != None:
        parameters["completeness"] = completeness
    if date != None:
        parameters["date"] = date
    if dateTime != None:
        parameters["dateTime"] = dateTime
    if measure != None:
        parameters["measure"] = measure
    if qcode != None:
        parameters["qcode"] = qcode
    if quality != None:
        parameters["quality"] = quality
    if value != None:
        parameters["value"] = value
    if minDate != None:
        parameters["min-date"] = minDate
    if mineqDate != None:
        parameters["mineq-date"] = mineqDate
    if maxDate != None:
        parameters["max-date"] = maxDate
    if maxeqDate != None:
        parameters["maxeq-date"] = maxeqDate
    if earliest != None:
        parameters["earliest"] = earliest
    if latest != None:
        parameters["latest"] = latest
    if station != None:
        parameters["station"] = station
    if stationRLOIid != None:
        parameters["station.RLOIid"] = stationRLOIid
    if stationWiskiID != None:
        parameters["station.wiskiID"] = stationWiskiID
    if stationStationReference != None:
        parameters["station.stationReference"] = stationStationReference
    if observationType != None:
        parameters["observationType"] = observationType
    if observedProperty != None:
        parameters["observedProperty"] = observedProperty
    if period != None:
        parameters["period"] = period
    if _offset != None:
        parameters["_offset"] = _offset
    if _limit != None:
        parameters["_limit"] = _limit
    if _sort != None:
        parameters["_sort"] = _sort
    if _projection != None:
        parameters["_projection"] = _projection

    r = requests.get(
        'https://environment.data.gov.uk/hydrology/data/readings', params=parameters
    )

    items = r.json()
    return items
    

def ListOfAllAvailableMeasurementTimeseriesInTheHydrologyDataset(
datumType=None,
label=None,
notation=None,
observationType=None,
observationTypeLabel=None,
observedProperty=None,
observedPropertyLabel=None,
parameter=None,
parameterName=None,
period=None,
qualifier=None,
station=None,
stationRLOIid=None,
stationLabel=None,
stationStationReference=None,
stationWiskiID=None,
unit=None,
unitName=None,
valueStatistic=None,
valueStatisticLabel=None,
_offset=None,
_limit=None,
_sort=None,
_projection=None):
    
    parameters = {}
                
    if datumType != None:
        parameters["datumType"] = datumType
    if label != None:
        parameters["label"] = label
    if notation != None:
        parameters["notation"] = notation
    if observationType != None:
        parameters["observationType"] = observationType
    if observationTypeLabel != None:
        parameters["observationType.label"] = observationTypeLabel
    if observedProperty != None:
        parameters["observedProperty"] = observedProperty
    if observedPropertyLabel != None:
        parameters["observedProperty.label"] = observedPropertyLabel
    if parameter != None:
        parameters["parameter"] = parameter
    if parameterName != None:
        parameters["parameterName"] = parameterName
    if period != None:
        parameters["period"] = period
    if qualifier != None:
        parameters["qualifier"] = qualifier
    if station != None:
        parameters["station"] = station
    if stationRLOIid != None:
        parameters["station.RLOIid"] = stationRLOIid
    if stationLabel != None:
        parameters["station.label"] = stationLabel
    if stationStationReference != None:
        parameters["station.stationReference"] = stationStationReference
    if stationWiskiID != None:
        parameters["station.wiskiID"] = stationWiskiID
    if unit != None:
        parameters["unit"] = unit
    if unitName != None:
        parameters["unitName"] = unitName
    if valueStatistic != None:
        parameters["valueStatistic"] = valueStatistic
    if valueStatisticLabel != None:
        parameters["valueStatistic.label"] = valueStatisticLabel
    if _offset != None:
        parameters["_offset"] = _offset
    if _limit != None:
        parameters["_limit"] = _limit
    if _sort != None:
        parameters["_sort"] = _sort
    if _projection != None:
        parameters["_projection"] = _projection

    r = requests.get(
        'https://environment.data.gov.uk/hydrology/id/measures', params=parameters
    )

    items = r.json()
    return items
    

def DescriptionOfASingleMeasurementTimeseries(
id,
_projection=None):
    
    parameters = {}
                
    if _projection != None:
        parameters["_projection"] = _projection

    r = requests.get(
        'https://environment.data.gov.uk/hydrology/id/measures/{id}', params=parameters
    )

    items = r.json()
    return items
    

def ReadingsForASingleMeasureTimeseries(
measure,
date=None,
minDate=None,
mineqDate=None,
maxDate=None,
maxeqDate=None,
earliest=None,
latest=None,
_projection=None):
    
    parameters = {}
                
    if date != None:
        parameters["date"] = date
    if minDate != None:
        parameters["min-date"] = minDate
    if mineqDate != None:
        parameters["mineq-date"] = mineqDate
    if maxDate != None:
        parameters["max-date"] = maxDate
    if maxeqDate != None:
        parameters["maxeq-date"] = maxeqDate
    if earliest != None:
        parameters["earliest"] = earliest
    if latest != None:
        parameters["latest"] = latest
    if _projection != None:
        parameters["_projection"] = _projection

    r = requests.get(
        'https://environment.data.gov.uk/hydrology/id/measures/{measure}/readings', params=parameters
    )

    items = r.json()
    return items
    

def ListOfAllMonitoringStationsCanBeFilteredByNameLocationAndOtherParameters(
RLOIid=None,
aquifer=None,
boreholeDepth=None,
catchmentName=None,
dateOpened=None,
datum=None,
easting=None,
label=None,
lat=None,
long=None,
measures=None,
measuresLabel=None,
measuresNotation=None,
measuresObservationType=None,
measuresObservationTypeLabel=None,
measuresObservedProperty=None,
measuresObservedPropertyLabel=None,
measuresPeriod=None,
measuresQualifier=None,
measuresUnitName=None,
measuresValueStatistic=None,
measuresValueStatisticLabel=None,
northing=None,
notation=None,
nrfaStationID=None,
nrfaStationURL=None,
riverName=None,
sampleOf=None,
sampleOfLabel=None,
stationReference=None,
status=None,
statusLabel=None,
town=None,
type=None,
wiskiID=None,
observedProperty=None,
easting=None,
northing=None,
search=None,
long=None,
_offset=None,
lat=None,
_limit=None,
_sort=None,
dist=None,
_projection=None):
    
    parameters = {}
                
    if RLOIid != None:
        parameters["RLOIid"] = RLOIid
    if aquifer != None:
        parameters["aquifer"] = aquifer
    if boreholeDepth != None:
        parameters["boreholeDepth"] = boreholeDepth
    if catchmentName != None:
        parameters["catchmentName"] = catchmentName
    if dateOpened != None:
        parameters["dateOpened"] = dateOpened
    if datum != None:
        parameters["datum"] = datum
    if easting != None:
        parameters["easting"] = easting
    if label != None:
        parameters["label"] = label
    if lat != None:
        parameters["lat"] = lat
    if long != None:
        parameters["long"] = long
    if measures != None:
        parameters["measures"] = measures
    if measuresLabel != None:
        parameters["measures.label"] = measuresLabel
    if measuresNotation != None:
        parameters["measures.notation"] = measuresNotation
    if measuresObservationType != None:
        parameters["measures.observationType"] = measuresObservationType
    if measuresObservationTypeLabel != None:
        parameters["measures.observationType.label"] = measuresObservationTypeLabel
    if measuresObservedProperty != None:
        parameters["measures.observedProperty"] = measuresObservedProperty
    if measuresObservedPropertyLabel != None:
        parameters["measures.observedProperty.label"] = measuresObservedPropertyLabel
    if measuresPeriod != None:
        parameters["measures.period"] = measuresPeriod
    if measuresQualifier != None:
        parameters["measures.qualifier"] = measuresQualifier
    if measuresUnitName != None:
        parameters["measures.unitName"] = measuresUnitName
    if measuresValueStatistic != None:
        parameters["measures.valueStatistic"] = measuresValueStatistic
    if measuresValueStatisticLabel != None:
        parameters["measures.valueStatistic.label"] = measuresValueStatisticLabel
    if northing != None:
        parameters["northing"] = northing
    if notation != None:
        parameters["notation"] = notation
    if nrfaStationID != None:
        parameters["nrfaStationID"] = nrfaStationID
    if nrfaStationURL != None:
        parameters["nrfaStationURL"] = nrfaStationURL
    if riverName != None:
        parameters["riverName"] = riverName
    if sampleOf != None:
        parameters["sampleOf"] = sampleOf
    if sampleOfLabel != None:
        parameters["sampleOf.label"] = sampleOfLabel
    if stationReference != None:
        parameters["stationReference"] = stationReference
    if status != None:
        parameters["status"] = status
    if statusLabel != None:
        parameters["status.label"] = statusLabel
    if town != None:
        parameters["town"] = town
    if type != None:
        parameters["type"] = type
    if wiskiID != None:
        parameters["wiskiID"] = wiskiID
    if observedProperty != None:
        parameters["observedProperty"] = observedProperty
    if easting != None:
        parameters["easting"] = easting
    if northing != None:
        parameters["northing"] = northing
    if search != None:
        parameters["search"] = search
    if long != None:
        parameters["long"] = long
    if _offset != None:
        parameters["_offset"] = _offset
    if lat != None:
        parameters["lat"] = lat
    if _limit != None:
        parameters["_limit"] = _limit
    if _sort != None:
        parameters["_sort"] = _sort
    if dist != None:
        parameters["dist"] = dist
    if _projection != None:
        parameters["_projection"] = _projection

    r = requests.get(
        'https://environment.data.gov.uk/hydrology/id/stations', params=parameters
    )

    items = r.json()
    return items
    

def DetailsForASingleMonitoringStation(
id,
_projection=None):
    
    parameters = {}
                
    if _projection != None:
        parameters["_projection"] = _projection

    r = requests.get(
        'https://environment.data.gov.uk/hydrology/id/stations/{id}', params=parameters
    )

    items = r.json()
    return items
    

def ListTheTimeseriesForAStation(
station,
observationType=None,
observedProperty=None,
_projection=None):
    
    parameters = {}
                
    if observationType != None:
        parameters["observationType"] = observationType
    if observedProperty != None:
        parameters["observedProperty"] = observedProperty
    if _projection != None:
        parameters["_projection"] = _projection

    r = requests.get(
        'https://environment.data.gov.uk/hydrology/id/stations/{station}/measures', params=parameters
    )

    items = r.json()
    return items
    
