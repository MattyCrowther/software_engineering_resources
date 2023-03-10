
class Planet:

    def __init__(self,
                 name,
                 radius_metres,
                 mass_kilograms,
                 orbital_period_seconds,
                 surface_temperature_kelvin):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin











def main():

    mercury = Planet("Mercury",
                     radius_metres=2439.7e3,
                     mass_kilograms=3.3022e23,
                     orbital_period_seconds=7.60052e6,
                     surface_temperature_kelvin=340)

    venus = Planet("Venus",
                   radius_metres=6051.8e3,
                   mass_kilograms=4.8676e24,
                   orbital_period_seconds=1.94142e7,
                   surface_temperature_kelvin=737)

    earth = Planet("Earth",
                   radius_metres=6371.0e3,
                   mass_kilograms=5.972e24,
                   orbital_period_seconds=3.15581e7,
                   surface_temperature_kelvin=288)

    mars = Planet("Mars",
                  radius_metres=3389.5e3,
                  mass_kilograms=6.4185e23,
                  orbital_period_seconds=5.93543e7,
                  surface_temperature_kelvin=210)

    return mercury, venus, earth, mars

if __name__ == '__main__':
  main()