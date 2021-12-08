abilityNames = [
    "Cold Resistance 1",
    "Cold Resistance 2",
    "Heat Resistance 1",
    "Heat Resistance 2",
    "Environ mental Hardening",
    "Drug Resistance 1",
    "Drug Resistance 2",
    "Genetic Hardening 1",
    "Genetic Hardening 2",
    "Genetic Reshuffle 1",
    "Genetic Reshuffle 2",
    "Genetic Reshuffle 3"
    ]

abilityBaseCosts = {
    "Cold Resistance 1": 7,
    "Cold Resistance 2": 12,
    "Heat Resistance 1": 11,
    "Heat Resistance 2": 22,
    "Environ mental Hardening": 30,
    "Drug Resistance 1": 11,
    "Drug Resistance 2": 25,
    "Genetic Hardening 1": 7,
    "Genetic Hardening 2": 22,
    "Genetic Reshuffle 1": 17,
    "Genetic Reshuffle 2": 21,
    "Genetic Reshuffle 3": 25
    }

abilityEffects = {            
    "Cold Resistance 1": [("infectivity", "cold", 0.3)],
    "Cold Resistance 2": [("infectivity", "cold", 0.6)],
    "Heat Resistance 1": [("infectivity", "hot", 0.3)],
    "Heat Resistance 2": [("infectivity", "hot", 0.6)], 
    "Environ mental Hardening": [("infectivity", "cold", 1), ("infectivity", "hot", 1)],
    "Drug Resistance 1": [("infectivity", "wealthy", 0.3)],
    "Drug Resistance 2": [("infectivity", "wealthy", 0.7)],
    "Genetic Hardening 1": [("efficiency", "cold", 0.3)],
    "Genetic Hardening 2": [("efficiency", "cold", 0.3)],
    "Genetic Reshuffle 1": [("requirement", "cold", 0.3)],
    "Genetic Reshuffle 2": [("requirement", "cold", 0.3)],
    "Genetic Reshuffle 3": [("requirement", "cold", 0.3)]
    }

abilityPrerequisites = {
    "Cold Resistance 1": set(), 
    "Cold Resistance 2": {"Cold Resistance 1"},
    "Heat Resistance 1": set(), 
    "Heat Resistance 2": {"Heat Resistance 1"}, 
    "Environ mental Hardening": {"Cold Resistance 2", "Heat Resistance 2"},
    "Drug Resistance 1": set(), 
    "Drug Resistance 2": {"Drug Resistance 1"},
    "Genetic Hardening 1": set(),
    "Genetic Hardening 2": {"Genetic Hardening 1"},
    "Genetic Reshuffle 1": {"Drug Resistance 2", "Genetic Hardening 2"},
    "Genetic Reshuffle 2": {"Genetic Reshuffle 1"},
    "Genetic Reshuffle 3": {"Genetic Reshuffle 2"}
    }
    
 
abilityGridCoords = {
    "Cold Resistance 1": (0, 0),
    "Cold Resistance 2": (1, 0),
    "Heat Resistance 1": (0, 2),
    "Heat Resistance 2": (1, 1),
    "Environ mental Hardening": (2, 1),
    "Drug Resistance 1": (0, 4),
    "Drug Resistance 2": (1, 3),
    "Genetic Hardening 1": (1, 4),
    "Genetic Hardening 2": (2, 5),
    "Genetic Reshuffle 1": (2, 4),
    "Genetic Reshuffle 2": (3, 4),
    "Genetic Reshuffle 3": (4, 4)
    }