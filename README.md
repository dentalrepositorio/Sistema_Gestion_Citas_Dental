# Sistema de Gestión de Citas Dentales (CLI)
> "Solución de software para gestión de citas odontológicas con persistencia de datos y validación de integridad."

**Asignatura:** INF-4311
**Desarrollador:** FRANKLIN PEREZ MATOS
**Estado:** Finalizado (v1.0)

## 📋 Descripción del Proyecto
Este repositorio contiene el código fuente de una solución robusta para la gestión administrativa de un consultorio dental. El sistema permite administrar el ciclo de vida completo de las citas a través de una interfaz de línea de comandos optimizada.

## ⚙️ Funcionalidades Implementadas
1. **CRUD de Citas:** Registro de nuevas citas con validación estricta de ID único para asegurar la integridad de los datos.
2. **Lógica Temporal Inteligente:** Algoritmo que determina el estado de la cita (`Vigente`, `En Proceso`, `Finalizado`) comparando la fecha registrada con el reloj del sistema (`datetime`) en tiempo real.
3. **Persistencia de Datos:** Módulo de exportación que genera reportes automáticos en formato `.csv` (compatible con Excel).
4. **Resiliencia (Manejo de Errores):** Implementación de bloques `try-except` para garantizar que el programa no se cierre ante entradas inválidas.

## 🚀 Cómo Ejecutar
**Requisitos:** Python 3.x

1. Clona el repositorio o descarga los archivos.
2. Abre la terminal en la carpeta del proyecto.
3. Ejecuta el siguiente comando:

```bash
python main.py
