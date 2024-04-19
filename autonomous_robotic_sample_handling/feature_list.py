from navigate.tools.decorators import FeatureList
from navigate.model.features.feature_related_functions import (
    ExampleFeature,
    SelectSample,
    AcquireSample,
    AttachToMicroscope,
    RemoveFromMicroscope,
    ReturnSample,
)


@FeatureList
def example_feature():
    return [
        {"name": ExampleFeature},
    ]

@FeatureList
def select_sample():
    return [
        {"name": SelectSample},
    ]

@FeatureList
def acquire_sample():
    return [
        {"name": AcquireSample},
    ]

@FeatureList
def attach_to_microscope():
    return [
        {"name": AttachToMicroscope},
    ]

@FeatureList
def remove_from_microscope():
    return [
        {"name": RemoveFromMicroscope},
    ]

@FeatureList
def return_sample():
    return [
        {"name": ReturnSample},
    ]