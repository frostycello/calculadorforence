import math
from datetime import datetime, timedelta

def calcular_hora_muerte(Ta, hora_primera_str, T1, hora_segunda_str, T2):
    try:
        # Parsear horas
        hora_primera = datetime.strptime(hora_primera_str, "%H:%M")
        hora_segunda = datetime.strptime(hora_segunda_str, "%H:%M")

        # Calcular intervalo en horas
        delta_t = (hora_segunda - hora_primera).total_seconds() / 3600.0

        if delta_t <= 0:
            return "Error: La segunda toma debe ser después de la primera."

        T0 = 37.0  # temperatura corporal viva

        # Validaciones
        if (T1 - Ta) <= 0 or (T2 - Ta) <= 0:
            return "Error: Las temperaturas del cuerpo deben ser mayores que la temperatura ambiente."
        if T2 >= T1:
            return "Error: La temperatura debe disminuir entre las tomas."

        # Constante k
        ratio = (T2 - Ta) / (T1 - Ta)
        k = -math.log(ratio) / delta_t

        # Tiempo desde la muerte hasta la primera toma
        ratio_t1 = (T1 - Ta) / (T0 - Ta)
        if ratio_t1 <= 0 or ratio_t1 >= 1:
            return "Error: Datos inconsistentes (temperaturas inválidas)."

        t1 = -math.log(ratio_t1) / k

        # Hora de muerte
        hora_muerte = hora_primera - timedelta(hours=t1)
        return f"La hora aproximada de la muerte es: {hora_muerte.strftime('%H:%M')}"

    except ValueError:
        return "Error: Formato de hora incorrecto. Usa HH:MM (ej. 06:00)."
    except Exception as e:
        return f"Error inesperado: {str(e)}"