
import image_filter as imF



class PipelineFactory:
    def __init__(self, image):
        self.image = image
        self.filter = imF.Filter(self.image)
        
    
    def create_pipeline(self, pipeline_type):
        match pipeline_type:
            case 1:
                return Pipe1(self.image)
            case 2:
                return Pipe2(self.image)
            case 3:
                return Pipe3(self.image)
            case _:
                print("Invalid pipeline type")
                return None

    



from abc import abstractmethod


class Pipeline:
    
    @abstractmethod
    def pipe(self):
        pass
    
    def get_image(self):
        return self.image
    

class Pipe1(Pipeline):
    
    def __init__(self, image):
        self.image = image
    
    def pipe(self):
        print("Pipe1")
        filter.remove_noise()
        
    
class Pipe2(Pipeline):
    
    def __init__(self, image):
        self.image = image
    
    def pipe(self):
        print("Pipe2")
        
class Pipe3(Pipeline):
    
    def __init__(self, image):
        self.image = image
    
    def pipe(self):
        print("Pipe3")

        

        