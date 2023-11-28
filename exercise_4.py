# A country can be said as being big if it is:

# Big in terms of population.
# Big in terms of area.
# Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

# Population is greater than 20 million.
# Area is larger than 3 million square km.
# Also, create a method which compares a country's population density to another country object. Return a string in the following format:

# {country} has a {smaller / larger} population density than {other_country}

class Country:
    def __init__(self, country, population, area) -> None:
        self.country = country
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()

    def check_if_big(self) -> bool:
        return self.population > 20000000 or self.area > 3000000

    def compare_pd(self, other_country) -> str:
        population_density = self.population / self.area
        population_density_other_country = other_country.population / other_country.areal
        if population_density > population_density_other_country:
            return f"{self.country} has a larger population density than {other_country.country}"
        else:
            return f"{self.country} has a smaller population density than {other_country.country}"
            
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
print(andorra.compare_pd(australia))