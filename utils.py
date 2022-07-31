nutrition_names_map = {
    "sugar": ['Azúcares totales (g)', 'Azúcares Totales (g)', 'Azúcares totales (mg)'],
    "fiber": ['Fibra (g)'],
    "monounsaturated_fats": ['Grasas monoinsaturadas (g)', 'Grasas Monoinsaturadas (g)'],
    "polyunsaturated_fats": ['Grasas poliinsaturadas (g)', 'Grasas Polinsaturadas (g)', 'Grasas Poliinsaturadas (g)'],
    "saturated_fats": ['Grasas saturadas (g)', 'Grasas Saturadas (g)'],
    "trans_fats": ['Grasas trans (g)', 'Ac. Grasos Trans (g)', ],
    "total_fats": ['Grasas Totales (g)'],
    "carbohydrates": ['Hidratos de carbono disponibles (g)', 'Hidratos de Carbono Disp. (g)', 'Hidratos de Carbono disponibles (g)'],
    "energy": ['Energía (kJ)', 'Energía (kcal)', 'Energía (kCal)'],
    "sodium": ['Sodio (g)', 'Sodio (mg)'],
    "cholesterol": ['Colesterol (mg)', 'Colesterol (g)'],
    "protein": ['Proteínas (g)']
}

def build_nutrition_dict(nutrition_table):
    nutrition = dict()
    for nutrition_info in nutrition_table:
        if nutrition_info[0] in nutrition_names_map['energy']:
            if nutrition_info[2] == 'kJ':
                nutrition_info[1] = kJ_to_kCal(nutrition_info[1])
            nutrition["energy"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['fiber']:
            nutrition["fiber"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['monounsaturated_fats']:
            nutrition["monounsaturated_fats"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['polyunsaturated_fats']:
            nutrition['polyunsaturated_fats'] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['saturated_fats']:
            nutrition["saturated_fats"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['trans_fats']:
            nutrition["trans_fats"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['total_fats']:
            nutrition["total_fats"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['carbohydrates']:
            nutrition["carbohydrates"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['sodium']:
            if nutrition_info[2] == "mg":
                nutrition_info[1] = nutrition_info[1] / 1000
            nutrition["sodium"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['cholesterol']:
            if nutrition_info[2] == "mg":
                nutrition_info[1] = nutrition_info[1] / 1000
            nutrition["cholesterol"] = nutrition_info[1]
        elif nutrition_info[0] in nutrition_names_map['protein']:
            nutrition["protein"] = nutrition_info[1]
    return nutrition

def kJ_to_kCal(kilo_joules):
    return kilo_joules / 4,1868
