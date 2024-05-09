import PIL.Image as Image

from flashcards.text_scraper.image_filter import (
    remove_borders,
    deskew,
    add_borders,
    remove_noise,
    binarize,
    grayscale,
)


class Pipeline:
    """
    The pipeline class is responsible for applying a series of filters to an image
    """

    def __init__(self, image, filters):
        self.image: Image = image
        self.filters = filters

    def apply_filters(self):
        """
        Method that applies all the filters in the pipeline to the image
        """

        for filter in self.filters:
            self.image = filter(self.image)

    def get_image(self) -> Image:
        return self.image


class PipelineFactory:
    def __init__(self, image):
        self.image = image

    def create_pipeline(self, pipeline_type) -> Pipeline:
        """creates pipeline based on what type of pipeline is requested

        Args:
            pipeline_type (_type_): per now only 1, 2, 3 are valid

        Returns:
            _type_: a pipeline object
        """
        filters = []
        match pipeline_type:
            case 1:
                filters.append(remove_noise())
                filters.append(binarize())
                filters.append(add_borders())
                filters.append(deskew())
                filters.append(remove_borders())
            case 2:
                filters.append(remove_noise())
                filters.append(deskew())
            case 3:
                filters.append(grayscale())
                filters.append(remove_borders())

            case _:
                print("Invalid pipeline type")

        return Pipeline(self.image, filters)
