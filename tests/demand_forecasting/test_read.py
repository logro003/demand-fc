from unittest.mock import patch
from io import StringIO
import pandas as pd
from demand_forecasting.read import read_data


def test_read_data_success():
    """Testing reading import data"""
    csv_content = generate_mock_data()

    with patch(
        "demand_forecasting.read.pd.read_csv",
        return_value=pd.read_csv(StringIO(csv_content)),
    ):
        # Call the function with the mocked pd.read_csv
        result = read_data("dummy.csv")
    print(result)

    # Assert that the function returns the expected DataFrame
    expected_data = pd.DataFrame(
        {
            "ride_id": [
                "97341db7-f89f-45db-9dd1-bcc2620fc1db",
                "646c160f-bbb7-4c78-b2ca-bdd8644a8400",
            ],
            "city_name": ["voiholm", "voiholm"],
            "start_time": [
                "2020-08-05 04:27:40.425797 UTC",
                "2020-08-05 07:47:29.060615 UTC",
            ],
            "start_lon": [11.908586502075194, 11.908669471740723],
            "start_lat": [57.6871223449707, 57.687049865722656],
            "h3index_big": ["881f250613fffff", "881f250613fffff"],
            "h3index_small": ["891f250612bffff", "891f250612bffff"],
        }
    )
    print(expected_data)
    pd.testing.assert_frame_equal(result, expected_data)


def generate_mock_data():
    """Generating csv mock data for testing"""
    csv_content = "ride_id,city_name,start_time,start_lon,start_lat,h3index_big,h3index_small\n97341db7-f89f-45db-9dd1-bcc2620fc1db,voiholm,2020-08-05 04:27:40.425797 UTC,11.908586502075194,57.6871223449707,881f250613fffff,891f250612bffff\n646c160f-bbb7-4c78-b2ca-bdd8644a8400,voiholm,2020-08-05 07:47:29.060615 UTC,11.908669471740723,57.687049865722656,881f250613fffff,891f250612bffff"
    return csv_content
