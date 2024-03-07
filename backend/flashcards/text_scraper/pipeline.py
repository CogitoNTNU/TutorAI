import image_filter as imF
import cv2



class PipelineFactory:
    def __init__(self, image):
        self.image = image
    
    def create_pipeline(self, pipeline_type):
        """creates pipeline based on what type of pipeline is requested

        Args:
            pipeline_type (_type_): per now only 1, 2, 3 are valid

        Returns:
            _type_: a pipeline object
        """
        filters = []
        match pipeline_type:
            case 1:
                filters.append(imF.Remove_noise())
                filters.append(imF.Binarize())
                filters.append(imF.Add_borders())
                filters.append(imF.Deskew())
                filters.append(imF.Remove_borders())
            case 2:
                filters.append(imF.Remove_noise())
                filters.append(imF.Deskew())
            case 3:
                filters.append(imF.Grayscale())
                filters.append(imF.Remove_borders())
                
            case _:
                print("Invalid pipeline type")
                
        return Pipeline(self.image, filters)



class Pipeline:
    
    def __init__(self, image, filters):
        self.image = image
        self.filters = filters
    
    def pipe(self):
    
        """
        loops through each filter and applies it to the image
        
        """
        
        for filter in self.filters:
            self.image = filter(self.image)
    
    def get_image(self):
        return self.image
    
    
  

import PIL.Image as Image 

if __name__=="__main__":
    image_file = "TutorAI/backend/flashcards/text_scraper/assets/page_01_rotated.jpg"
    image = cv2.imread(image_file)
    pipeline: Pipeline = PipelineFactory(image).create_pipeline(1)
    pipeline.pipe()
    
    imF.Display()(pipeline.get_image())
    
    
    
    
    
    
    
    