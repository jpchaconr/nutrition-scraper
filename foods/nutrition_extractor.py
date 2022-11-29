def calories(nutrition, measure):
    nutrition["energy"] = measure

def fats(nutrition, measure):
    nutrition["total_fats"] = measure

def sat_fats(nutrition, measure):
    nutrition["saturated_fats"] = measure

def poli_sat_fats(nutrition, measure):
    nutrition["polyunsaturated_fats"] = measure

def mono_sat_fats(nutrition, measure):
    nutrition["monounsaturated_fats"] = measure

def trans_fats(nutrition, measure):
    nutrition["trans_fats"] = measure

def colesterol(nutrition, measure):
    measure = round(measure / 1000, 3)
    nutrition["cholesterol"] = measure

def carbs(nutrition, measure):
    nutrition["carbohydrates"] = measure

def fiber(nutrition, measure):
    nutrition["fiber"] = measure

def sugar(nutrition, measure):
    nutrition["sugar"] = measure

def protein(nutrition, measure):
    nutrition["protein"] = measure

strategy = {
    "Calorías": calories,
    "Grasas": fats,
    "Saturadas": sat_fats,
    "Polisaturadas": poli_sat_fats,
    "Monosaturadas": mono_sat_fats,
    "Trans": trans_fats,
    "Colesterol": colesterol,
    "Carbohidrato": carbs,
    "Fibra dietética": fiber,
    "Azúcares": sugar,
    "Proteína": protein,
}
