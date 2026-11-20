"""Servicios de ejemplo (PLACEHOLDER).

Sirven para probar las reservas. Si tu compañero de servicios ya tiene su
clase abstracta Servicio y sus tres servicios, se reemplaza este archivo
por el suyo (deben tener: calcular_costo, validar_parametros, disponible).
"""

from abc import abstractmethod                      # Para métodos abstractos
from modulo_clientes import EntidadBase, DatoInvalidoError  # Base y error del módulo de clientes


class Servicio(EntidadBase):
    """Clase abstracta de la que heredan todos los servicios."""

    def __init__(self, codigo, nombre, tarifa_hora, disponible=True):
        super().__init__(codigo)                    # El código es el identificador
        if not isinstance(tarifa_hora, (int, float)) or tarifa_hora <= 0:
            raise DatoInvalidoError("La tarifa por hora debe ser un número mayor a 0")
        self.nombre = nombre                        # Nombre del servicio
        self._tarifa_hora = tarifa_hora             # Tarifa protegida
        self.disponible = disponible                # True si se puede reservar

    def calcular_costo(self, horas, descuento=0.0, impuesto=0.19):
        """Sobrecarga simulada con parámetros opcionales:
        calcular_costo(h) | calcular_costo(h, descuento) | calcular_costo(h, descuento, impuesto)
        """
        base = self._tarifa_hora * horas            # Costo antes de descuento e impuesto
        return round(base * (1 - descuento) * (1 + impuesto), 2)

    @abstractmethod
    def validar_parametros(self, horas):
        """Cada servicio define sus propios límites (polimorfismo)."""

    def describir(self):
        return f"{self.nombre} (${self._tarifa_hora:,.0f}/hora)"


class SalaReunion(Servicio):
    def validar_parametros(self, horas):
        if not 1 <= horas <= 8:                     # Una sala se reserva de 1 a 8 horas
            raise DatoInvalidoError("Las salas se reservan entre 1 y 8 horas")


class AlquilerEquipo(Servicio):
    def validar_parametros(self, horas):
        if not 1 <= horas <= 72:                    # Un equipo se alquila hasta 72 horas
            raise DatoInvalidoError("Los equipos se alquilan entre 1 y 72 horas")


class Asesoria(Servicio):
    def validar_parametros(self, horas):
        if not 1 <= horas <= 4:                     # Una asesoría dura de 1 a 4 horas
            raise DatoInvalidoError("Las asesorías duran entre 1 y 4 horas")
