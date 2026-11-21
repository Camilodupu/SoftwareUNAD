
"""Simulación de 16 operaciones de Software FJ (válidas e inválidas).

Ejecutar:  python simulacion.py   -> genera logs_software_fj.log
"""

from modulo_clientes import GestorClientes, ErrorSoftwareFJ, logger
from modulo_reservas import GestorReservas
from servicios_demo import SalaReunion, AlquilerEquipo, Asesoria


def intentar(numero, descripcion, accion):
    """Ejecuta una operación; si falla, lo registra y el programa continúa."""
    print(f"\n--- Operación {numero}: {descripcion}")
    logger.info("Operación %s: %s", numero, descripcion)
    try:
        return accion()
    except ErrorSoftwareFJ as error:               # Error previsto del sistema
        logger.error("Operación %s falló: %s", numero, error)
        print(f"[ERROR] {error}")
    except Exception as error:                     # Error imprevisto: igual no se cae
        logger.critical("Error inesperado en operación %s: %r", numero, error)
        print(f"[CRÍTICO] {error!r}")
    return None


def main():
    clientes, reservas = GestorClientes(), GestorReservas()
    laura = intentar(1, "Registrar cliente válido",
                     lambda: clientes.registrar("Laura Gómez", "1012345678", "laura@correo.com", "3001234567"))
    intentar(2, "Registrar cliente con correo inválido",
             lambda: clientes.registrar("Ana Ruiz", "52111222", "ana-correo.com", "3201234567"))
    carlos = intentar(3, "Registrar segundo cliente válido",
                      lambda: clientes.registrar("Carlos Pérez", "80123456", "carlos@correo.com", "3109876543"))
    sala = intentar(4, "Crear sala de reuniones válida", lambda: SalaReunion("S1", "Sala Torre A", 50000))
    intentar(5, "Crear servicio con tarifa negativa", lambda: AlquilerEquipo("E1", "Portátil", -100))
    equipo = intentar(6, "Crear alquiler de equipo válido", lambda: AlquilerEquipo("E2", "Proyector", 20000))
    asesoria = intentar(7, "Crear asesoría no disponible", lambda: Asesoria("A1", "Asesoría legal", 80000, disponible=False))
    r1 = intentar(8, "Reserva exitosa (sala, 3 h)", lambda: reservas.crear(laura, sala, 3))
    intentar(9, "Confirmar la reserva anterior", lambda: reservas.procesar(r1))
    intentar(10, "Reserva con duración excesiva (sala, 20 h)", lambda: reservas.crear(carlos, sala, 20))
    r2 = intentar(11, "Reserva de servicio no disponible", lambda: reservas.crear(carlos, asesoria, 2))
    intentar(12, "Procesar reserva de servicio no disponible",
             lambda: reservas.procesar(r2) if r2 is not None
             else print("[INFO] Reserva no creada; no se puede procesar"))
    r3 = intentar(13, "Reserva con descuento imposible (150%)", lambda: reservas.crear(carlos, equipo, 10, descuento=1.5))
    intentar(14, "Procesar reserva con cálculo inconsistente",
             lambda: reservas.procesar(r3) if r3 is not None
             else print("[INFO] Reserva no creada; no se puede procesar"))
    intentar(15, "Cancelar dos veces la misma reserva",
             lambda: (reservas.cancelar(r1), reservas.cancelar(r1)))
    intentar(16, "Reserva con cliente inexistente (None)", lambda: reservas.crear(None, sala, 2))

    print(f"\nResumen: {len(clientes.listar())} clientes, {len(reservas.listar())} reservas. "
          "El programa terminó sin caerse. Revisa logs_software_fj.log")


if __name__ == "__main__":
    main()
