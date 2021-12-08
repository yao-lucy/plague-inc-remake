transmissionNames = [
    "Bird 1",
    "Bird 2",
    "Rodent 1",
    "Rodent 2",
    "Livestock 1",
    "Livestock 2",
    "Insect 1",
    "Insect 2",
    "Blood 1",
    "Blood 2",
    "Air 1",
    "Air 2",
    "Water 1",
    "Water 2",
    "Extreme Zoonosis",
    "Extreme Haemato phagy",
    "Extreme Bioaerosol"
    ]

transmissionBaseCosts = {
    "Bird 1": 12,
    "Bird 2": 18,
    "Rodent 1": 10,
    "Rodent 2": 16,
    "Livestock 1": 7,
    "Livestock 2": 12,
    "Insect 1": 9,
    "Insect 2": 20,
    "Blood 1": 8,
    "Blood 2": 13,
    "Air 1": 9,
    "Air 2": 14,
    "Water 1": 9,
    "Water 2": 15,
    "Extreme Zoonosis": 22,
    "Extreme Haemato phagy": 24,
    "Extreme Bioaerosol": 18 
    }

transmissionEffects = {
    "Bird 1": [("infectivity",None,3), ("spread","land",9)],
    "Bird 2": [("infectivity",None,6), ("spread","land",90)],
    "Rodent 1": [("infectivity",None,3), ("infectivity","urban",0.8)],
    "Rodent 2": [("infectivity",None,6), ("infectivity","urban",1.2)],
    "Livestock 1": [("infectivity",None,2), ("infectivity","rural",0.8)],
    "Livestock 2": [("infectivity",None,4), ("infectivity","rural",1.2)],
    "Insect 1": [("infectivity",None,4), ("infectivity","hot",0.1)],
    "Insect 2": [("infectivity",None,8), ("infectivity","hot",0.3)],
    "Blood 1":[("infectivity",None,2), ("infectivity","poor",0.8)],
    "Blood 2": [("infectivity",None,4), ("infectivity","poor",1.2)],
    "Air 1": [("infectivity",None,4), ("infectivity","arid",0.8), ("spread","air",9)],
    "Air 2": [("infectivity",None,7), ("infectivity","arid",1.2), ("spread","air",90)],
    "Water 1": [("infectivity",None,4), ("infectivity","humid",0.8), ("spread","water",9)],
    "Water 2": [("infectivity",None,8), ("infectivity","humid",1.2), ("spread","water",90)],
    "Extreme Zoonosis": [("infectivity",None,5), ("infectivity","urban",1), ("infectivity","rural",1), ("spread","land",10)],
    "Extreme Haemato phagy": [("infectivity",None,5), ("infectivity","poor",1), ("infectivity","hot",0.3)],
    "Extreme Bioaerosol": [("infectivity",None,5), ("infectivity","humid",1.3), ("infectivity","arid",1.3), ("spread","water",20), ("spread","air",20)] 
    }

transmissionPrerequisites = {
    "Bird 1": set(),
    "Bird 2": {"Bird 1"},
    "Rodent 1": set(),
    "Rodent 2": {"Rodent 1"},
    "Livestock 1": set(),
    "Livestock 2": {"Livestock 1"},
    "Insect 1": set(),
    "Insect 2": {"Insect 1"},
    "Blood 1": set(),
    "Blood 2": {"Blood 1"},
    "Air 1": set(),
    "Air 2": {"Air 1"},
    "Water 1": set(),
    "Water 2": {"Water 1"},
    "Extreme Zoonosis": {"Livestock 2", "Bird 2", "Rodent 2"},
    "Extreme Haemato phagy": {"Blood 2", "Insect 2"},
    "Extreme Bioaerosol": {"Air 2", "Water 2"} 
    }

transmissionGridCoords = {
    "Bird 1": (0, 0),
    "Bird 2": (1, 0),
    "Rodent 1": (0, 2),
    "Rodent 2": (1, 1),
    "Livestock 1": (4, 1),
    "Livestock 2": (3, 1),
    "Insect 1": (0, 5),
    "Insect 2": (1, 4),
    "Blood 1": (4, 5),
    "Blood 2": (3, 4),
    "Air 1": (7, 0),
    "Air 2": (8, 1),
    "Water 1": (7, 3),
    "Water 2": (8, 3),
    "Extreme Zoonosis": (2, 1),
    "Extreme Haemato phagy": (2, 4),
    "Extreme Bioaerosol": (8, 2) 
    }