from abc import ABC, abstractmethod

class Project1(ABC):
    
    @abstractmethod
    def load_img(self):
        print("I made some update")

    @abstractmethod
    def load_model(self):
        print("I made some update")

    @abstractmethod
    def model_predict(self):
        print("I made some update")

