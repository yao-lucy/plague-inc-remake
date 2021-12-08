# name, population, populationDensity, development, temperature, weather, airIn, airOut, waterIn, waterOut, neighbors

countryNames = [
    "North America",
    "South America",
    "Europe",
    "Africa",
    "Asia",
    "Australia",
    # "Antarctica"
    ]

# population = {
#     "North America": 587615000,
#     "South America": 428240000,
#     "Europe": 742648000,
#     "Africa": 1287920000,
#     "Asia": 4545133000,
#     "Australia": 41261000,
#     "Antarctica": 4490
#     }

population = {
    "North America": 587615123,
    "South America": 428244567,
    "Europe": 742648891,
    "Africa": 1287922345,
    "Asia": 4545133678,
    "Australia": 41261910,
    "Antarctica": 4490
    }

populationDensity = {
    "North America": "rural",
    "South America": "rural",
    "Europe": "suburban",
    "Africa": "suburban",
    "Asia": "urban",
    "Australia": "rural",
    "Antarctica": "rural"
    }

development = {
    "North America": 1,
    "South America": 3,
    "Europe": 1,
    "Africa": 3,
    "Asia": 2,
    "Australia": 1,
    "Antarctica": 2
    }

temperature = {
    "North America": "mild",
    "South America": "hot",
    "Europe": "cold",
    "Africa": "hot",
    "Asia": "mild",
    "Australia": "hot",
    "Antarctica": "cold"
    }

weather = {
    "North America": "normal",
    "South America": "humid",
    "Europe": "normal",
    "Africa": "arid",
    "Asia": "normal",
    "Australia": "arid",
    "Antarctica": "normal"
    }

airOut = {
    "North America": {"South America", "Europe", "Africa", "Asia", "Australia"},
    "South America": {"North America", "Europe", "Africa", "Asia"},
    "Europe": {"North America", "South America", "Africa", "Asia"},
    "Africa": {"North America", "South America", "Europe", "Asia"},
    "Asia": {"North America", "South America", "Europe", "Africa",  "Australia"},
    "Australia": {"North America", "Asia"},
    "Antarctica": {}
    }

waterOut = {
    "North America": {"South America", "Europe", "Africa", "Asia", "Australia"},
    "South America": {"North America", "Europe", "Africa", "Asia"},
    "Europe": {"North America", "South America", "Africa", "Asia", "Antarctica"},
    "Africa": {"North America", "South America", "Europe", "Asia"},
    "Asia": {"North America", "South America", "Europe", "Africa",  "Australia"},
    "Australia": {"North America", "Asia"},
    "Antarctica": {"North America", "Europe"}
    }

neighbors = {
    "North America": {"South America"},
    "South America": {"North America"},
    "Europe": {"Africa", "Asia"},
    "Africa": {"Europe", "Asia"},
    "Asia": {"Africa", "Europe"},
    "Australia": set(),
    "Antarctica": set()
    }
    
coords = {
    "North America": (200, 180),
    "South America": (305, 326),
    "Europe": (500, 172),
    "Africa": (505, 273),
    "Asia": (662, 173),
    "Australia": (781, 359),
    "Antarctica": set()
    }