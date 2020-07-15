class ObservedProperty:

    def __init__(self, dict):
        for k, v in dict.items():
            setattr(self, "_" + k, v)

        try: 
            self._id = dict["@id"]
        except:
            pass

    
        
    def label(self):
        try:
            value = self._label
        except AttributeError:
            value = None

        return value
        
    
        
    def label(self):
        try:
            value = self._label
        except AttributeError:
            value = None

        return value
        
    