import PIL.Image as Image

from flashcards.text_scraper.image_filter import (
    Filter,
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

    def __init__(self, filters: list[Filter]):
        self.filters = filters

    def apply_filters(self, image: Image) -> Image:
        """
        Applies all filters in the pipeline to the image
        """
        for filter in self.filters:
            image = filter(image)
        return image


def create_pipeline(image: Image) -> Pipeline:
    """
    Creates a pipeline for the given image

    Args:
        image: the image to create the pipeline for

    Returns:
        Pipeline: the pipeline object
    """
    pipeline_type = _determine_pipeline_type(image)

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

    return Pipeline(filters)


def _determine_pipeline_type(image: Image) -> int:
    """
    Determines the pipeline type based on the image
    """
    # TODO: Implement this function
    return 1
