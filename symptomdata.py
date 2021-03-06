symptomNames = [
    "Nausea",
    "Coughing",
    "Rash",
    "Insomnia",
    "Cysts",
    "Anaemia",
    "Vomiting",
    "Pneumonia",
    "Sneezing",
    "Sweating",
    "Paranoia",
    "Hyper sensitivity",
    "Abscesses",
    "Haemophilia",
    "Pulmonary Oedema",
    "Fever",
    "Inflammation",
    "Tumours",
    "Diarrhoea",
    "Pulmonary Fibrosis",
    "Immune Suppression",
    "Skin Lesions",
    "Seizures",
    "Paralysis",
    "Systemic Infection",
    "Internal Haemor rahaging",
    "Dysentery",
    "Insanity",
    "Necrosis",
    "Hemorrhagic Shock",
    "Coma",
    "Total Organ Failure"
    ]

symptomBaseCosts = {
    "Nausea": 2,
    "Coughing": 4,
    "Rash": 3,
    "Insomnia": 2,
    "Cysts": 2,
    "Anaemia": 2,
    "Vomiting": 3,
    "Pneumonia": 3,
    "Sneezing": 5,
    "Sweating": 3,
    "Paranoia": 4,
    "Hyper sensitivity": 2,
    "Abscesses": 2,
    "Haemophilia": 3,
    "Pulmonary Oedema": 7,
    "Fever": 9,
    "Inflammation": 5,
    "Tumours": 11,
    "Diarrhoea": 6,
    "Pulmonary Fibrosis": 6,
    "Immune Suppression": 12,
    "Skin Lesions": 8,
    "Seizures": 4,
    "Paralysis": 10,
    "Systemic Infection": 17,
    "Internal Haemor rahaging": 12,
    "Dysentery": 19,
    "Insanity": 18,
    "Necrosis": 27,
    "Hemorrhagic Shock": 23,
    "Coma": 21,
    "Total Organ Failure": 28
    }

symptomEffects = {
    "Nausea": [("infectivity", None, 1), ("severity", None, 1), ("lethality", None, 0)],
    "Coughing": [("infectivity", None, 3), ("severity", None, 1), ("lethality", None, 0)],
    "Rash": [("infectivity", None, 2), ("severity", None, 1), ("lethality", None, 0)],
    "Insomnia": [("infectivity", None, 0), ("severity", None, 3), ("lethality", None, 0)],
    "Cysts": [("infectivity", None, 2), ("severity", None, 2), ("lethality", None, 0)],
    "Anaemia": [("infectivity", None, 1), ("severity", None, 1), ("lethality", None, 0)],
    "Vomiting": [("infectivity", None, 3), ("severity", None, 1), ("lethality", None, 0)],
    "Pneumonia": [("infectivity", None, 3), ("severity", None, 2), ("lethality", None, 0)],
    "Sneezing": [("infectivity", None, 5), ("severity", None, 1), ("lethality", None, 0)],
    "Sweating": [("infectivity", None, 2), ("severity", None, 1), ("lethality", None, 0)],
    "Paranoia": [("infectivity", None, 0), ("severity", None, 4), ("lethality", None, 0)],
    "Hyper sensitivity": [("infectivity", None, 1), ("severity", None, 2), ("lethality", None, 0)],
    "Abscesses": [("infectivity", None, 4), ("severity", None, 4), ("lethality", None, 0)],
    "Haemophilia": [("infectivity", None, 4), ("severity", None, 3), ("lethality", None, 0)],
    "Pulmonary Oedema": [("infectivity", None, 5), ("severity", None, 4), ("lethality", None, 2)],
    "Fever": [("infectivity", None, 4), ("severity", None, 3), ("lethality", None, 3)],
    "Inflammation": [("infectivity", None, 2), ("severity", None, 2), ("lethality", None, 2)],
    "Tumours": [("infectivity", None, 1), ("severity", None, 0), ("lethality", None, 3)],
    "Diarrhoea": [("infectivity", None, 6), ("severity", None, 4), ("lethality", None, 1)],
    "Pulmonary Fibrosis": [("infectivity", None, 3), ("severity", None, 3), ("lethality", None, 2)],
    "Immune Suppression": [("infectivity", None, 2), ("severity", None, 6), ("lethality", None, 4)],
    "Skin Lesions": [("infectivity", None, 11), ("severity", None, 4), ("lethality", None, 0)],
    "Seizures": [("infectivity", None, 1), ("severity", None, 7), ("lethality", None, 3)],
    "Paralysis": [("infectivity", None, 2), ("severity", None, 5), ("lethality", None, 1)],
    "Systemic Infection": [("infectivity", None, 6), ("severity", None, 7), ("lethality", None, 6)],
    "Internal Haemor rahaging": [("infectivity", None, 0), ("severity", None, 9), ("lethality", None, 7)],
    "Dysentery": [("infectivity", None, 8), ("severity", None, 14), ("lethality", None, 8)],
    "Insanity": [("infectivity", None, 6), ("severity", None, 15), ("lethality", None, 0)],
    "Necrosis": [("infectivity", None, 10), ("severity", None, 20), ("lethality", None, 13)],
    "Hemorrhagic Shock": [("infectivity", None, 0), ("severity", None, 15), ("lethality", None, 15)],
    "Coma": [("infectivity", None, 0), ("severity", None, 15), ("lethality", None, 2)],
    "Total Organ Failure": [("infectivity", None, 0), ("severity", None, 20), ("lethality", None, 25)]
    }

symptomPrerequisites = {
    "Nausea": set(),
    "Coughing": set(),
    "Rash": set(),
    "Insomnia": set(),
    "Cysts": set(),
    "Anaemia": set(),
    "Vomiting": {"Nausea"},
    "Pneumonia": {"Coughing"},
    "Sneezing": {"Coughing"},
    "Sweating": {"Rash"},
    "Paranoia": {"Insomnia"},
    "Hyper sensitivity": {"Cysts"},
    "Abscesses": {"Cysts"},
    "Haemophilia": {"Anaemia"},
    "Pulmonary Oedema": {"Pneumonia", "Vomiting"},
    "Fever": {"Sweating"},
    "Inflammation": {"Hyper sensitivity", "Paranoia"},
    "Tumours": {"Abscesses", "Haemophilia"},
    "Diarrhoea": {"Vomiting", "Pulmonary Oedema"},
    "Pulmonary Fibrosis": {"Pneumonia", "Pulmonary Oedema"},
    "Immune Suppression": {"Sneezing"},
    "Skin Lesions": {"Sweating", "Fever"},
    "Seizures": {"Inflammation", "Paranoia"},
    "Paralysis": {"Inflammation", "Hyper sensitivity"},
    "Systemic Infection": {"Tumours", "Abscesses"},
    "Internal Haemor rahaging": {"Haemophilia", "Tumours"},
    "Dysentery": {"Diarrhoea"},
    "Insanity": {"Seizures"},
    "Necrosis": {"Skin Lesions"},
    "Hemorrhagic Shock": {"Internal Haemor rahaging"},
    "Coma": {"Paralysis", "Systemic Infection"},
    "Total Organ Failure": {"Immune Spression", "Pulmonary Fibrosis"}
    }

symptomGridCoords = {
    "Nausea": (0, 0),
    "Coughing": (4, 0),
    "Rash": (8, 0),
    "Insomnia": (0, 5),
    "Cysts": (4, 5),
    "Anaemia": (8, 5),
    "Vomiting": (1, 0),
    "Pneumonia": (3, 0),
    "Sneezing": (5, 0),
    "Sweating": (7, 0),
    "Paranoia": (1, 4),
    "Hyper sensitivity": (3, 4),
    "Abscesses": (5, 4),
    "Haemophilia": (7, 4),
    "Pulmonary Oedema": (2, 1),
    "Fever": (6, 1),
    "Inflammation": (2, 4),
    "Tumours": (6, 4),
    "Diarrhoea": (1, 1),
    "Pulmonary Fibrosis": (3, 1),
    "Immune Suppression": (5, 1),
    "Skin Lesions": (7, 1),
    "Seizures": (1, 3),
    "Paralysis": (3, 3),
    "Systemic Infection": (5, 3),
    "Internal Haemor rahaging": (7, 3),
    "Dysentery": (0, 2),
    "Insanity": (0, 3),
    "Necrosis": (8, 2),
    "Hemorrhagic Shock": (8, 3),
    "Coma": (4, 3),
    "Total Organ Failure": (4, 2)
    }