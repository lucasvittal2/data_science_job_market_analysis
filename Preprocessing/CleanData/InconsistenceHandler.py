from AbstractionClasses.Preprocessing.DataCleaner import DataCleaner



class InconsistenceHandler(DataCleaner):
    
    def __init__(self, eliminate_by):
        self.eliminate_by = eliminate_by
    
    def eliminate_inconsistences(self, data):
        pass
    
    def eliminate_redudances(self, data):
        pass
    
    def clean_data(self, data):
        
        if "INCONSISTENCE" in self.eliminate_by:
            cleaned_data=  self.eliminate_inconsistences(data)
        elif "REDUNDANCES" in self.eliminate_by:
            cleaned_data = self.eliminate_redudances(data)
        else:
            raise NotImplementedError("Inconsistence Handling method not implemented! \n \
                try some of available methods: 'INCONSISTENCE_...', 'REDUNDANCES_...' ")
        return  cleaned_data