import requests

def ReadingsForOneOrMoreMeasureTimeSeries(
    completeness=None,
	date=None,
	dateTime=None,
	measure=None,
	qcode=None,
	quality=None,
	value=None,
	minDate=none,
	mineqDate=none,
	maxDate=none,
	maxeqDate=none,
	earliest=None,
	latest=None,
	station=None,
	stationRLOIid=None,
	stationWiskiID=None,
	stationReference=None,
	observationType=None,
	observedProperty=None,
	period=None):
    
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
        parameters["minDate"] = minDate 
    if mineqDate != None:
        parameters["mineqDate"] = mineqDate 
    if maxDate != None:
        parameters["maxDate"] = maxDate 
    if maxeqDate != None:
        parameters["maxeqDate"] = maxeqDate 
    if earliest != None:
        parameters["earliest"] = earliest 
    if latest != None:
        parameters["latest"] = latest 
    if station != None:
        parameters["station"] = station 
    if stationRLOIid != None:
        parameters["stationRLOIid"] = stationRLOIid 
    if stationWiskiID != None:
        parameters["stationWiskiID"] = stationWiskiID 
    if stationReference != None:
        parameters["stationReference"] = stationReference 
    if observationType != None:
        parameters["observationType"] = observationType 
    if observedProperty != None:
        parameters["observedProperty"] = observedProperty 
    if period != None:
        parameters["period"] = period 
    
    r = requests.get(
        f'/hydrology/data/readings', params=parameters
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
	stationReference=None,
	stationWiskiID=None,
	unit=None,
	unitName=None,
	valueStatistic=None,
	valueStatisticLabel=None):
    
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
        parameters["observationTypeLabel"] = observationTypeLabel 
    if observedProperty != None:
        parameters["observedProperty"] = observedProperty 
    if observedPropertyLabel != None:
        parameters["observedPropertyLabel"] = observedPropertyLabel 
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
        parameters["stationRLOIid"] = stationRLOIid 
    if stationLabel != None:
        parameters["stationLabel"] = stationLabel 
    if stationReference != None:
        parameters["stationReference"] = stationReference 
    if stationWiskiID != None:
        parameters["stationWiskiID"] = stationWiskiID 
    if unit != None:
        parameters["unit"] = unit 
    if unitName != None:
        parameters["unitName"] = unitName 
    if valueStatistic != None:
        parameters["valueStatistic"] = valueStatistic 
    if valueStatisticLabel != None:
        parameters["valueStatisticLabel"] = valueStatisticLabel 
    
    r = requests.get(
        f'/hydrology/id/measures', params=parameters
    )

    items = r.json()
    return items
    
def DescriptionOfASingleMeasurementTimeseries(
    id=None):
    
    parameters = {}
                
    if id != None:
        parameters["id"] = id 
    
    r = requests.get(
        f'/hydrology/id/measures/{id}', params=parameters
    )

    items = r.json()
    return items
    
def ReadingsForASingleMeasureTimeseries(
    measure=None,
	date=None,
	minDate=none,
	mineqDate=none,
	maxDate=none,
	maxeqDate=none,
	earliest=None,
	latest=None):
    
    parameters = {}
                
    if measure != None:
        parameters["measure"] = measure 
    if date != None:
        parameters["date"] = date 
    if minDate != None:
        parameters["minDate"] = minDate 
    if mineqDate != None:
        parameters["mineqDate"] = mineqDate 
    if maxDate != None:
        parameters["maxDate"] = maxDate 
    if maxeqDate != None:
        parameters["maxeqDate"] = maxeqDate 
    if earliest != None:
        parameters["earliest"] = earliest 
    if latest != None:
        parameters["latest"] = latest 
    
    r = requests.get(
        f'/hydrology/id/measures/{measure}/readings', params=parameters
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
	measuresObservationType.label=None,
	measuresObservedProperty=None,
	measuresObservedProperty.label=None,
	measuresPeriod=None,
	measuresQualifier=None,
	measuresUnitName=None,
	measuresValueStatistic=None,
	measuresValueStatistic.label=None,
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
	observedProperty=None):
    
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
        parameters["measuresLabel"] = measuresLabel 
    if measuresNotation != None:
        parameters["measuresNotation"] = measuresNotation 
    if measuresObservationType != None:
        parameters["measuresObservationType"] = measuresObservationType 
    if measuresObservationType.label != None:
        parameters["measuresObservationType.label"] = measuresObservationType.label 
    if measuresObservedProperty != None:
        parameters["measuresObservedProperty"] = measuresObservedProperty 
    if measuresObservedProperty.label != None:
        parameters["measuresObservedProperty.label"] = measuresObservedProperty.label 
    if measuresPeriod != None:
        parameters["measuresPeriod"] = measuresPeriod 
    if measuresQualifier != None:
        parameters["measuresQualifier"] = measuresQualifier 
    if measuresUnitName != None:
        parameters["measuresUnitName"] = measuresUnitName 
    if measuresValueStatistic != None:
        parameters["measuresValueStatistic"] = measuresValueStatistic 
    if measuresValueStatistic.label != None:
        parameters["measuresValueStatistic.label"] = measuresValueStatistic.label 
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
        parameters["sampleOfLabel"] = sampleOfLabel 
    if stationReference != None:
        parameters["stationReference"] = stationReference 
    if status != None:
        parameters["status"] = status 
    if statusLabel != None:
        parameters["statusLabel"] = statusLabel 
    if town != None:
        parameters["town"] = town 
    if type != None:
        parameters["type"] = type 
    if wiskiID != None:
        parameters["wiskiID"] = wiskiID 
    if observedProperty != None:
        parameters["observedProperty"] = observedProperty 
    
    r = requests.get(
        f'/hydrology/id/stations', params=parameters
    )

    items = r.json()
    return items
    
def DetailsForASingleMonitoringStation(
    id=None):
    
    parameters = {}
                
    if id != None:
        parameters["id"] = id 
    
    r = requests.get(
        f'/hydrology/id/stations/{id}', params=parameters
    )

    items = r.json()
    return items
    
def ListTheTimeseriesForAStation(
    station=None,
	observationType=None,
	observedProperty=None):
    
    parameters = {}
                
    if station != None:
        parameters["station"] = station 
    if observationType != None:
        parameters["observationType"] = observationType 
    if observedProperty != None:
        parameters["observedProperty"] = observedProperty 
    
    r = requests.get(
        f'/hydrology/id/stations/{station}/measures', params=parameters
    )

    items = r.json()
    return items
    
