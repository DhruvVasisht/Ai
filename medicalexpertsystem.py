# Facts
facts = {
    "fever": False,
    "cough": False,
    "sore_throat": False,
    "body_ache": False
}

# Rules
rules = [
    {"conditions": ["fever", "cough"], "conclusion": "Patient may have the flu."},
    {"conditions": ["fever", "sore_throat"], "conclusion": "Patient may have viral."},
    {"conditions": ["cough", "body_ache"], "conclusion": "Patient may have cough."}
]

# Inference engine
def infer():
    for rule in rules:
        match = True
        for condition in rule["conditions"]:
            if not facts[condition]:
                match = False
                break
        if match:
            print(rule["conclusion"])

# User interface
print("Enter symptoms (fever, cough, sore throat):")
symptoms = input().split()
for symptom in symptoms:
    if symptom in facts:
        facts[symptom] = True
    infer()