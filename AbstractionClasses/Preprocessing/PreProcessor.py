from abc import ABC,abstractmethod

class PreProcessor(ABC):

    def __init__(self, preprocessor_type: str):
        self.preprocessor_type = preprocessor_type
        
    @abstractmethod
    def process_data(self, data):
        '''
            Implement Preprocessing
        '''
        pass