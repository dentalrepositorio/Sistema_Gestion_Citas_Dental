import csv
import os
import datetime
from datetime import timedelta

# ==========================================
# CONFIGURACIÓN GLOBAL
# ==========================================
base_datos_citas = []

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_estado(fecha_hora_inicio, duracion_minutos):
    """Calcula si la cita está vigente, en proceso o finalizada"""
    ahora = datetime.datetime.now()
    fecha_fin = fecha_hora_inicio + timedelta(minutes=duracion_minutos)
    
    if ahora < fecha_hora_inicio:
        delta = fecha_hora_inicio - ahora
        # Calculamos formato limpio de tiempo restante
        return "Vigente", f"Faltan {delta.days}d, {delta.seconds // 3600}h"
    elif fecha_hora_inicio <= ahora <= fecha_fin:
        return "En Proceso", "En curso ahora"
    else:
        return "Finalizado", "-"

# ==========================================
# LÓGICA PRINCIPAL (CRUD)
# ==========================================
def agendar_cita():
    print("\n=== AGENDAR NUEVA CITA ===")
    id_cita = input("ID único de cita: ").strip()
    
    # Validación: Verificar si el ID ya existe
    if any(c['id'] == id_cita for c in base_datos_citas):
        print("❌ Error Crítico: ID duplicado. No se puede guardar.")
        input("Presione Enter para volver..."); return

    try:
        paciente = input("Nombre Paciente: ").strip()
        dentista = input("Nombre Dentista: ").strip()
        motivo = input("Motivo Consulta: ").strip()
        print("Formato de fecha: Año-Mes-Dia Hora:Minuto (Ej: 2025-11-28 14:30)")
        fecha_str = input("Fecha y Hora: ")
        
        # Validación: Formato de fecha
        fecha_dt = datetime.datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        duracion = int(input("Duración (minutos): "))
        
        # Guardado en memoria
        base_datos_citas.append({
            'id': id_cita,
            'paciente': paciente,
            'dentista': dentista,
            'motivo': motivo,
            'fecha_obj': fecha_dt,
            'duracion': duracion
        })
        print("✅ Cita registrada exitosamente en el sistema.")
        
    except ValueError:
        print("❌ Error: Formato de fecha o número inválido.")
    except Exception as e:
        print(f"❌ Error del sistema: {e}")
    input("Presione Enter para continuar...")

def mostrar_citas():
    limpiar_pantalla()
    print("=== MONITOR DE CITAS EN TIEMPO REAL ===")
    print(f"{'ID':<6} {'Paciente':<15} {'Fecha':<18} {'Estado':<12} {'Info'}")
    print("-" * 70)
    
    if not base_datos_citas:
        print(" [ NO HAY DATOS REGISTRADOS ]")
    
    for c in base_datos_citas:
        estado, info = obtener_estado(c['fecha_obj'], c['duracion'])
        fecha_fmt = c['fecha_obj'].strftime('%Y-%m-%d %H:%M')
        print(f"{c['id']:<6} {c['paciente'][:14]:<15} {fecha_fmt:<18} {estado:<12} {info}")
    
    input("\nPresione Enter para volver...")

def exportar_csv():
    try:
        filename = "reporte_citas.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Paciente", "Dentista", "Motivo", "Fecha", "Duracion", "Estado_Calculado"])
            for c in base_datos_citas:
                est, _ = obtener_estado(c['fecha_obj'], c['duracion'])
                writer.writerow([c['id'], c['paciente'], c['dentista'], c['motivo'], c['fecha_obj'], c['duracion'], est])
        print(f"✅ Exportación completada: {os.path.abspath(filename)}")
    except Exception as e: 
        print(f"❌ Error al exportar: {e}")
    input("Presione Enter...")

# ==========================================
# MENÚ DEL SISTEMA
# ==========================================
def main():
    while True:
        limpiar_pantalla()
        print("=== SISTEMA DENTAL V1.0 ===")
        print("1. [VER] Monitor de Citas")
        print("2. [NUEVO] Agendar Cita")
        print("3. [DATA] Exportar a CSV")
        print("4. [SALIR] Cerrar Sistema")
        
        op = input("\nSeleccione operación: ")
        
        if op == '1': mostrar_citas()
        elif op == '2': agendar_cita()
        elif op == '3': exportar_csv()
        elif op == '4': break
        else: pass

if __name__ == "__main__":
    main()