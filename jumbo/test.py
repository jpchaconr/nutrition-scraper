from index import get_product_data

data = get_product_data('https://www.jumbo.cl/malva-calaf-bolsa-250-g-banadas-en-chocolate/p')
print('----------------------')
print(data)

def kJ_to_kCal(kilo_joules):
    return kilo_joules / 4,1868

nutr = {
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

nutrition_table = []

nutrition = dict()
for nutrition_info in nutrition_table:
    if nutrition_info[0] in nutr['energy']:
        if nutrition_info[2] == 'kJ':
            nutrition_info[1] = kJ_to_kCal(nutrition_info[1])
        nutrition["energy"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['fiber']:
        nutrition["fiber"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['monounsaturated_fats']:
        nutrition["monounsaturated_fats"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['polyunsaturated_fats']:
        nutrition['polyunsaturated_fats'] = nutrition_info[1]

    elif nutrition_info[0] in nutr['saturated_fats']:
        nutrition["saturated_fats"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['trans_fats']:
        nutrition["trans_fats"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['total_fats']:
        nutrition["total_fats"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['carbohydrates']:
        nutrition["carbohydrates"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['sodium']:
        if nutrition_info[2] == "mg":
            nutrition_info[1] = nutrition_info / 1000
        nutrition["sodium"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['cholesterol']:
        if nutrition_info[2] == "mg":
            nutrition_info[1] = nutrition_info / 1000
        nutrition["cholesterol"] = nutrition_info[1]

    elif nutrition_info[0] in nutr['protein']:
        nutrition["protein"] = nutrition_info[1]
    

# {'Azúcares totales (g)', 'Grasas monoinsaturadas (g)', 'Fibra (g)', 'Grasas poliinsaturadas (g)', 
# 'Hidratos de carbono disponibles (g)', 'Grasas Polinsaturadas (g)', 'Grasas Monoinsaturadas (g)', 
# 'Grasas Totales (g)', 'Energía (kJ)', 'Grasas saturadas (g)', 'Azúcares totales (mg)', 'Grasas trans (g)', 
# 'Hidratos de Carbono Disp. (g)', 'Sodio (g)', 'Ac. Grasos Trans (g)', 'Colesterol (mg)', 'Energía (kcal)', 
# 'Azúcares Totales (g)', 'Sodio (mg)', 'Colesterol (g)', 'Proteínas (g)', 'Energía (kCal)', 'Grasas Saturadas (g)'}

# def build_object():
#     pass



# {
# "product": "product_id",
# "product_measure": "string",
# "sugar": 0,
# "fiber": 0,
# "monounsaturated_fats": 0,
# "polyunsaturated_fats": 0,
# "saturated_fats": 0,
# "trans_fats": 0,
# "total_fats": 0,
# "carbohydrates": 0,
# "energy": 0,
# "sodium": 0,
# "cholesterol": 0,
# "protein": 0
# }