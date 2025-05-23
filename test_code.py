from abc import ABC, abstractmethod

class Project1(ABC):
    
    @abstractmethod
    def load_img(self):
        print("I made some update--------------1")

    @abstractmethod
    def load_model(self):
        print("I made some update--------------2")

    @abstractmethod
    def model_predict(self):
        print("I made some update--------------3")

