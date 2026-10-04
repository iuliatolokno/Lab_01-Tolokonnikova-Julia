from toolkit.errors import ConverterError
conversions_dlina = { 
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
}
conversions_massa = {
    "g": 0.001,
    "kg": 1.0,
}
temp_units = {"c","f","k"}
def conversions_temp_v_kelvin(value:float, unit: str):
        unit = unit.lower()
        if unit == "c":
            return value + 273.15    
        if unit == "f":
            return (value - 32) * 5/9 +273.15
        if unit == "k":
            return value
        else:
            raise ValueError("Error")         

def conversions_temp(value:float, unit: str):
        unit = unit.lower()
        if unit == "c":
            return value - 273.15
        if unit == "f":
            return (value -273.15) * 9/5 + 32
        if unit == "k":
            return value
        else:
            raise ValueError("Error")
def get_group(unit:str):
        unit = unit.lower()
        if unit in conversions_dlina: 
            return "dlina"
        if unit in conversions_massa:
            return "massa"
        if unit in temp_units:
            return "temp"
        return None

def convert(value: float, from_unit: str, to_unit:str):
    try:
        value = float(value)
    except (TypeError, ConverterError):
        raise ConverterError("Неверное числовое значение")

    group_from = get_group(from_unit)
    group_to = get_group(to_unit)

    if group_from is None or group_to is None:
        raise ConverterError("Неизвестная единица измерения")
    
    if group_from != group_to:
        raise ConverterError("Конвертация между разными группами единиц запрещена")
    
    frmunt = from_unit.lower()
    tunt = to_unit.lower()

    
    if group_from == "dlina":
        value_in_meters = value * conversions_dlina[frmunt]
        result = value_in_meters / conversions_dlina[tunt]
        return result
    
    elif group_from == "massa":
        value_in_kg = value * conversions_massa[frmunt]
        result = value_in_kg / conversions_massa[tunt]
        return result
    
    elif group_from == "temp":
        kelvin = conversions_temp_v_kelvin(value, frmunt )
        if kelvin < 0:
            raise ConverterError("Температура ниже абсолютного нуля запрещена")
        result = conversions_temp(kelvin, tunt)
        return result
    raise ConverterError("Не удалось выполнить конвертацию")


