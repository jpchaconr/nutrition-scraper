import re

nutrition_type_map = {
    "Peso": "weigth",
    "Energía (Kcal)": "energy",
    "Hidratos de Carbono": "carbohydrates",
    "Proteínas": "protein",
    "Grasas": "total_fats",
    "de las cuales saturadas": "saturated_fats",
    "de las cuales trans": "trans_fats",
    "Fibra": "fiber",
    "Sal": "sodium",
}

def split_measure_unit(quantity):
    measure_unit = re.split('(\d+\.?\d*)', quantity.strip())[1:]
    print(measure_unit)
    return (float(measure_unit[0]), measure_unit[1])

def build_nutricion_dict(nutrition):
    nutri = {}
    aux = 100 / nutrition[0][1]
    for attr in nutrition[1:]:
        if attr[2] == 'mg':
            nutri[attr[0]] = round(attr[1] / 1000 * aux, 3)
        else:
            nutri[attr[0]] = round(attr[1] * aux, 3)
    return nutri
