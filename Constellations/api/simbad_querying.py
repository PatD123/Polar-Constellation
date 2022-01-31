from astroquery.simbad import Simbad
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
from astropy.coordinates.funcs import get_constellation
import math
from plotting_hemis import plot_polar

stars = open("brightest_stars.txt", "r").readlines()

def calc_radius(angle):
    return math.cos(angle * math.pi / 180) * 100

def get_view(user_lat, user_long, user_time):
    for star in stars:
        result_table = Simbad.query_object(star)
        RA_DEC = result_table["RA"].data[0] + " " + result_table["DEC"].data[0]
        c = SkyCoord(RA_DEC, unit=(u.hour, u.deg))

        my_house = EarthLocation(lat=user_lat*u.deg, lon=user_long*u.deg, height=77.0*u.m)
        utcoffset = -5*u.hour  # Eastern Daylight Time
        time = Time('2022-1-30 09:45:00') - utcoffset

        altaz = c.transform_to(AltAz(obstime=time,location=my_house))

        radius = calc_radius(altaz.alt.dms[0])
        angle = 360 - altaz.az.dms[0]

        if star == "Rotanev\n":
            return plot_polar(radius, angle)
            break


    
