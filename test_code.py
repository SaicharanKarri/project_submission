from abc import ABC, abstractmethod

class Project1(ABC):
    
    @abstractmethod
    def load_img(self):
        pass

    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def model_predict(self):
        pass

