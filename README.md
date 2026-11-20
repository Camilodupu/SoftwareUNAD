
# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## 1. Descripción del proyecto

Software FJ es un proyecto académico desarrollado para el curso de Programación (213023) de la Universidad Nacional Abierta y a Distancia (UNAD), correspondiente a la Fase 4.

El sistema tiene como propósito gestionar clientes, servicios especializados y reservas mediante la aplicación de los principios de programación orientada a objetos (POO) en Python, con énfasis en el manejo de excepciones.

El programa no utiliza bases de datos. La información se administra mediante objetos y listas en memoria, y se utiliza un archivo de logs para registrar errores y eventos.

## 2. Objetivos

- Aplicar abstracción, herencia, polimorfismo y encapsulación.
- Implementar clases para gestionar clientes, servicios y reservas.
- Incorporar excepciones personalizadas y validaciones.
- Utilizar estructuras `try/except/else/finally` para controlar errores.
- Implementar un registro de eventos y errores mediante archivos de logs.
- Ejecutar pruebas con operaciones válidas e inválidas.
- Integrar colaborativamente los módulos del sistema mediante GitHub.

## 3. Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Git y GitHub
- Programación orientada a objetos

## 4. Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `modulo_clientes.py` | Excepciones base, clase abstracta `EntidadBase`, clases `Cliente` y `GestorClientes`, y configuración del log. |
| `servicios_demo.py` | Clase abstracta `Servicio` y clases especializadas `SalaReunion`, `AlquilerEquipo` y `Asesoria`. |
| `modulo_reservas.py` | Excepciones avanzadas, clase `Reserva` con métodos para confirmar, cancelar y procesar, y clase `GestorReservas`. |
| `simulacion.py` | Simulación de 16 operaciones válidas e inválidas para probar el sistema. |
| `logs_software_fj.log` | Archivo generado durante la ejecución para registrar errores y eventos con fecha y hora. |

## 5. Conceptos de programación orientada a objetos

### Abstracción
Se utilizan las clases abstractas `EntidadBase` y `Servicio`, que establecen características y métodos comunes para las clases derivadas.

### Herencia y polimorfismo
Los servicios especializados heredan de la clase `Servicio` e implementan métodos propios para describir sus características, validar duraciones y calcular costos.

### Encapsulación
Se emplean atributos protegidos o privados y propiedades para controlar el acceso y validación de los datos.

### Sobrecarga simulada
Se utilizan parámetros opcionales para permitir diferentes formas de calcular los costos:

```python
calcular_costo(horas)
calcular_costo(horas, descuento)
calcular_costo(horas, descuento, impuesto)
```

### Excepciones personalizadas
Se implementan excepciones específicas para controlar datos inválidos, servicios no disponibles y problemas relacionados con las reservas.

### Manejo de errores
Se aplican estructuras `try/except/else/finally` y encadenamiento de excepciones mediante `raise ... from`, según la implementación de los módulos.

### Registro de eventos
El sistema contempla la generación de un archivo de logs para almacenar eventos y errores con fecha y hora.

## 6. Estructura del proyecto

```text
Software-FJ-UNAD/
├── README.md
├── modulo_clientes.py
├── servicios_demo.py
├── modulo_reservas.py
├── simulacion.py
└── logs_software_fj.log
```

Nota: `logs_software_fj.log` se genera durante la ejecución y no necesita estar previamente creado.

## 7. Cómo ejecutar el proyecto

Una vez que todos los módulos estén integrados, abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python simulacion.py
```

El sistema realizará las operaciones de prueba definidas y mostrará los resultados en la terminal.

**Importante:** La ejecución completa está pendiente de validación con todos los archivos definitivos del grupo.

## 8. Pruebas del sistema

La simulación contempla 16 operaciones para comprobar diferentes situaciones, incluyendo:

- Registro y validación de clientes.
- Creación de servicios especializados.
- Cálculo de costos, descuentos e impuestos.
- Validación de duración y disponibilidad de servicios.
- Creación, confirmación y cancelación de reservas.
- Control de errores mediante excepciones personalizadas.
- Registro de eventos y errores.

La ejecución y los resultados definitivos deben verificarse después de completar la integración.

## 9. Metodología de trabajo colaborativo

El proyecto se desarrolla mediante la participación de los integrantes del grupo.

GitHub permite organizar el código fuente, registrar los cambios realizados y facilitar la integración de los módulos.

Se propone utilizar ramas individuales para desarrollar y revisar los aportes antes de incorporarlos a la rama principal `main`.

## 10. Estado actual del proyecto

**En proceso de integración y validación.**

- Módulo de servicios especializados: desarrollado individualmente.
- Módulo de reservas: avance recibido.
- Módulo de simulación: avance recibido.
- Módulo de clientes: pendiente de recibir para completar las pruebas integradas.
- Pruebas del sistema completo: pendientes de validación.

## 11. Información académica

**Universidad:** Universidad Nacional Abierta y a Distancia (UNAD)

**Curso:** Programación (213023)

**Actividad:** Fase 4 – Manejo de excepciones en programación orientada a objetos

**Proyecto:** Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ
