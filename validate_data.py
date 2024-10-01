import pandas as pd
import pytest

# Read the sampled CSV files
weather_df = pd.read_csv('sampled_weather_df.csv')
field_df = pd.read_csv('sampled_field_df.csv')

# Define test functions
def test_read_weather_DataFrame_shape():
    """
    Test if the shape of the weather DataFrame is as expected.
    """
    assert weather_df.shape == (1843, 4)

def test_read_field_DataFrame_shape():
    """
    Test if the shape of the field DataFrame is as expected.
    """
    assert field_df.shape == (5654, 19)

def test_weather_DataFrame_columns():
    """
    Test if the columns of the weather DataFrame are as expected.
    """
    expected_columns = ['Weather_station_ID', 'Message', 'Measurement', 'Value']  # Replace with the expected column names
    assert list(weather_df.columns) == expected_columns

def test_field_DataFrame_columns():
    """
    Test if the columns of the field DataFrame are as expected.
    """
    expected_columns = ['Field_ID', 
                        'Elevation',
                        'Latitude',
                        'Longitude',
                        'Location',
                        'Slope',
                        'Rainfall',
                        'Min_temperature_C',
                        'Max_temperature_C',
                        'Ave_temps',
                        'Soil_fertility',
                        'Soil_type',
                        'pH',
                        'Pollution_level',
                        'Plot_size',
                        'Annual_yield',
                        'Crop_type',
                        'Standard_yield',
                        'Weather_station']  # Replace with the expected column names
    assert list(field_df.columns) == expected_columns

def test_field_DataFrame_non_negative_elevation():
    """
    Test if the elevation values in the field DataFrame are non-negative.
    """
    assert (field_df['Elevation'] >= 0).all()

def test_crop_types_are_valid():
    """
    Test if the crop types in the field DataFrame are valid.
    """
    valid_crop_types = ['cassava', 'tea', 'wheat', 'potato', 'banana', 'coffee', 'rice', 'maize']  # Replace with the valid crop types
    assert field_df['Crop_type'].isin(valid_crop_types).all()

def test_positive_rainfall_values():
    """
    Test if the rainfall values in both the field and weather DataFrame are positive.
    """
    # Extract rainfall values from field_df
    field_rainfall_values = field_df['Rainfall']
    
    # Extract rainfall values from weather_df
    weather_rainfall_values = weather_df[weather_df['Measurement'] == 'Rainfall']['Value']
    
    # Concatenate the two Series
    all_rainfall_values = pd.concat([weather_rainfall_values, field_rainfall_values])
    
    # Perform the assertion
    assert (all_rainfall_values >= 0).all()
