def test_simple_example():
    from datetime import datetime, timedelta
    from opendrift.models.oceandrift import OceanDrift

    o = OceanDrift(loglevel=20)
    o.set_config('environment:fallback:x_sea_water_velocity', 0)
    o.set_config('environment:fallback:y_sea_water_velocity', 1)
    o.set_config('environment:fallback:land_binary_mask', 0)

    o.seed_elements(lon=4.0, lat=60.0, radius=0, number=1, time=datetime(2015, 1, 1), radius_type='uniform')

    o.run(duration=timedelta(hours=1))

    assert o.elements.lat[0] > 60
    assert o.elements.lon[0] == 4
