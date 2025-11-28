# Sistema_Gestion_Citas_Dental
"Solución de software para gestión de citas odontológicas con persistencia de datos y validación de integridad."
# Proyecto Final: Sistema de Gestión de Citas Dentales
**Asignatura:** INF-4311
**Estudiante:** [FRANKLIN PEREZ MATOS]
## 📋 Descripción del Proyecto
Este repositorio contiene el código fuente de la solución propuesta para la gestión administrativa de un consultorio dental. El sistema permite gestionar el ciclo de vida de las citas mediante una interfaz de consola (CLI).

## ⚙️ Funcionalidades Implementadas
1. **CRUD de Citas:** Registro de nuevas citas con validación de ID único para asegurar la integridad de los datos.
2. **Cálculos Temporales:** Algoritmo que determina el estado de la cita (`Vigente`, `En Proceso`, `Finalizado`) comparando la fecha registrada con la fecha del sistema (`datetime`).
3. **Persistencia de Datos:** Módulo de exportación que genera reportes en formato `.csv` (Excel).
4. **Manejo de Errores:** Implementación de bloques `try-except` para garantizar la robustez del programa ante entradas inválidas del usuario.

## 🚀 Ejecución
Requerimientos: Python 3.x
