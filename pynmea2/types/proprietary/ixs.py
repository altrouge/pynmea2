# IxBlue (ex ixsea)

from decimal import Decimal

from ... import nmea
from ...nmea_utils import *
""" Support for proprietary messages from ixBlue receivers.
    Documentation: https://www.igp.de/manuals/7-INS-InterfaceLibrary_MU-INSIII-AN-001-O.pdf
"""
class IXS(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        sentence_type = data[1]
        name = manufacturer + sentence_type
        cls = _cls.sentence_types.get(name, _cls)
        return super(IXS, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = data[1]
        super(IXS, self).__init__(manufacturer, data)


class IXSHSPOS_(IXS, LatLonFix):
    """ IxBlue Halliburton Position Message
    """
    fields = (
        ('Empty', '_'),
        ('Sentence Type', 'type'),
        ('Timestamp', 'timestamp', timestamp),
        ('Latitude', 'lat'),
        ('Latitude Direction', 'lat_dir'),
        ('Longitude', 'lon'),
        ('Longitude Direction', 'lon_dir'),
        ('Depth Ellipsoid', 'depth', float),
        ('Altitude', 'altitude', float),
        ('Standard deviation of latitude error (meters)', 'std_dev_latitude', float),
        ('Standard deviation of longitude error (meters)', 'std_dev_longitude', float),
        ('Latitude/longitude covariance error (meters)', 'cov_latitude_longitude', float),
        ('Depth standard deviation (meters)', 'std_dev_depth', float),
        ('UTM zone longitude integer', 'utm_longitude_int', int),
        ('UTM zone latitude character', 'utm_latitude_char'),
        ('UTM zone position east (meters)', 'utm_east', float),
        ('UTM zone position north (meters)', 'utm_north', float),
        ('Estimate of DVL (dopler velocity log) course misalignment (degrees)', 'dvl_misalignment', float),
        ('Estimate of DVL (dopler velocity log) scale factor (%)', 'dvl_scale_factor', float),
        ('Speed of sound (m/s)', 'sound_speed', float)
    )

class IXSHSATIT(IXS):
    """ IxBlue Halliburton Attitude Message
    """
    fields = (
        ('Empty', '_'),
        ('Sentence Type', 'type'),
        ('Heading (degrees)', 'heading', float),
        ('Roll (degrees), + if port up', 'roll', float),
        ('Pitch (degrees), + if bow down', 'pitch', float),
        ('Heave (meters)', 'heave', float),
        ('XV3 rotation rate (degrees/sec)', 'xv3_rotation_rate', float),
        ('XV1 rotation rate (degrees/sec)', 'xv1_rotation_rate', float),
        ('XV2 rotation rate (degrees/sec)', 'xv2_rotation_rate', float),
        ('Horizontal speed course (degrees)', 'horizontal_speed_course', float),
        ('Horizontal speed (meters/sec)', 'horizontal_speed', float),
        ('Speed XV1 (meters/sec)', 'xv1_speed', float),
        ('Speed XV2 (meters/sec)', 'xv2_speed', float),
        ('Speed XV3 (meters/sec)', 'xv3_speed', float),
        ('Heading standard deviation error (degrees)', 'std_dev_heading', float),
        ('Roll standard deviation error (degrees)', 'std_dev_roll', float),
        ('Pitch standard deviation error (degrees)', 'std_dev_pitch', float),
        ('North speed standard deviation error (meters/sec)', 'std_dev_north_speed', float),
        ('East speed standard deviation error (meters/sec)', 'std_dev_east_speed', float),
        ('Vertical speed standard deviation error (meters/sec)', 'std_dev_vertical_speed', float)
    )
