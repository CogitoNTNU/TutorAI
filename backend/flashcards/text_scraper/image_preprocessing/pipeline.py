
class PipelineFactory:
    def __init__(self, image):
        self.image = image
        
    
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
    

class Pipe1(Pipeline):
    
    def __init__(self, image):
        self.image = image
    
    def pipe(self):
        print("Pipe1")
        
    
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

        

        