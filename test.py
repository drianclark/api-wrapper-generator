def readings(completeness, date, dateTime, measure, qcode, quality, value, minDate=none, mineqDate=none, maxDate=none, maxeqDate=none, earliest=None, latest=None, station=None, stationRLOIid=None, stationWiskiID=None, stationReference=None, observationType=None, observedProperty=None, period=None):

        parameters = {}
    
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
            f'/data/readings', params=parameters
        )

        items = r.json()

        return items
    