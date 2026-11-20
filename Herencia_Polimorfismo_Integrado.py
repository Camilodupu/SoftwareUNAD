
from abc import abstractmethod
from modulo_clientes import EntidadBase, ErrorSoftwareFJ


# ============================================================
# FASE 4 - SOFTWARECamilo Duenas
# MODULO DE SERVICIOS ESPECIALIZADOS
# HERENCIA Y POLIMORFISMO
# VERSION ADAPTADA PARA INTEGRAR CON MODULO_RESERVAS Y SIMULACION
# Requiere modulo_clientes.py real del equipo en la misma carpeta.
# ============================================================


# ============================================================
# 1. EXCEPCIONES PERSONALIZADAS
# ============================================================

class ErrorServicio(ErrorSoftwareFJ):
    """Esta se crea para representar un error general asociado a un servicio."""
    """ErrorServicio hereda de ErrorSoftwareFJ (definida en modulo_clientes),
    que permite manejar errores de manera más específica y compatible con reservas."""


class DatosInvalidosError(ErrorServicio):
    """esta se crea para representar un error cuando los datos no cumplen las reglas o son inválidos, Ej: poner -3 horas."""


class ServicioNoDisponibleError(ErrorServicio):
    """Esta se crea para representar un error cuando un servicio no está disponible, Ej: sala de reuniones no disponible ya que esta fuera de servicio."""


# La anterior parte del codigo trabaja con clases abstractas: EntidadBase es
# la clase base compartida (derivada de ABC) que viene de modulo_clientes.
# Las excepciones personalizadas ahora heredan indirectamente de ErrorSoftwareFJ,
# permitiendo que el modulo de reservas controle tambien estos errores.
# En donde class servicio que es lo que sigue sera la clase padre para los servicios especializados y las clases hijas seran SalaReunion, AlquilerEquipo y Asesoria, que heredan de la clase Servicio. 




# ============================================================
# 2. CLASE ABSTRACTA SERVICIO
# ============================================================

class Servicio(EntidadBase):

    """Esta clase representa las características generales de los servicios especializados, como el código, el nombre, la tarifa por hora y la disponibilidad.
    Además, define métodos abstractos que deben ser implementados por las clases hijas para calcular el costo y describir el servicio.
    Se utiliza EntidadBase para enlazarse con las entidades del modulo de clientes."""

    def __init__(self, codigo, nombre, tarifa_hora, disponible=True):

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del servicio es obligatorio."
            )

        if isinstance(tarifa_hora, bool) or not isinstance(
            tarifa_hora, (int, float)
        ):
            raise DatosInvalidosError(
                "La tarifa debe ser contener numeros."
            )

        if not 0 < tarifa_hora < float("inf"):
            raise DatosInvalidosError(
                "La tarifa debe ser positiva y tener un numero real y valido."
            )

        if not isinstance(disponible, bool):
            raise DatosInvalidosError(
                "La disponibilidad debe ser Verdadero o Falso."
            )

        # ADAPTACIÓN: el módulo de reservas usa un código por servicio.
        if not isinstance(codigo, str) or not codigo.strip():
            raise DatosInvalidosError("El código del servicio es obligatorio.")
        super().__init__(codigo.strip())
        self.nombre = nombre.strip()
        self._tarifa_hora = float(tarifa_hora)
        self.disponible = disponible

    """Se usa INIT para inicializar los atributos de la clase Servicio, como el codigo, el nombre, la tarifa por hora y la disponibilidad.
Se realizan validaciones para asegurarse de que los datos proporcionados sean válidos, y se lanzan excepciones personalizadas si los datos no cumplen con las reglas establecidas."""


    @property
    def tarifa_hora(self):
        """Se crea para consultar la tarifa del servicio."""
        return self._tarifa_hora

    def validar_parametros(self, duracion):
        """Se crea para realizar validaciones generales de los servicios.
        Por compatibilidad con reservas, se exige una duracion de al menos 1 hora."""

        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"{self.nombre} no esta disponible."
            )

        if isinstance(duracion, bool) or not isinstance(
            duracion, (int, float)
        ):
            raise DatosInvalidosError(
                "La duracion debe ser un numero real y valido."
            )

        if not 1 <= duracion < float("inf"):
            raise DatosInvalidosError(
                "La duracion debe ser un numero real de al menos 1 hora."
            )

    def _validar_porcentajes(self, descuento, impuesto):
        """Esta parte del codigo se crea para validar descuentos e impuestos."""

        for etiqueta, valor in (
            ("descuento", descuento),
            ("impuesto", impuesto)
        ):
            if isinstance(valor, bool) or not isinstance(
                valor, (int, float)
            ):
                raise DatosInvalidosError(
                    f"El {etiqueta} debe ser numerico."
                )

            if not 0 <= valor < float("inf"):
                raise DatosInvalidosError(
                    f"El {etiqueta} debe ser un numero real y no negativo."
                )

        if descuento > 1:
            raise DatosInvalidosError(
                "El descuento no puede superar el 100%."
            )

    def _aplicar_ajustes(self, subtotal, descuento, impuesto):
        """Se crea para aplicar descuento y luego impuesto."""

        self._validar_porcentajes(descuento, impuesto)

        return round(
            subtotal * (1 - descuento) * (1 + impuesto), 2
        )

    # ADAPTACIÓN: impuesto de 19% por defecto, como en el codigo del grupo.
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0.19):
        """ Este es el proceso que las clases hijas deben implementar."""
        """ Esto significa que cada servicio especializado debe definir su propia forma de calcular el costo, teniendo en cuenta sus reglas y restricciones específicas."""
        pass

    @abstractmethod
    def describir(self):
        """Se crea para mostrar la descripcion especifica de cada servicio."""
        pass


# ============================================================
# 3. SERVICIO ESPECIALIZADO: SALA DE REUNION
# ============================================================

# ADAPTACIÓN: capacidad=12 es opcional al crear una sala desde simulacion.py.
class SalaReunion(Servicio):
    """
    Esta clase representa una sala de reuniones y hereda los
    atributos y métodos de la clase base Servicio.

    Adicionalmente, incorpora el atributo capacidad, que
    permite establecer el número máximo de personas que
    pueden utilizar la sala.

    Aquí se aplica el concepto de herencia, ya que SalaReunion
    reutiliza las funcionalidades de Servicio y agrega
    características específicas.
    """

    def __init__(
        self, codigo, nombre, tarifa_hora, capacidad=12, disponible=True
    ):
        super().__init__(codigo, nombre, tarifa_hora, disponible)

        if (
            isinstance(capacidad, bool)
            or not isinstance(capacidad, int)
            or capacidad <= 0
        ):
            raise DatosInvalidosError(
                "La capacidad debe ser un numero entero positivo."
            )

        self.capacidad = capacidad

    def validar_parametros(self, duracion):
        """Esta valida la duracion de reserva de una sala."""

        super().validar_parametros(duracion)

        if duracion > 8:
            raise DatosInvalidosError(
                "La sala se puede reservar maximo 8 horas."
            )

    def calcular_costo(
        self, duracion, descuento=0, impuesto=0.19
    ):
        """Esta calcula el costo de reservar una sala."""

        self.validar_parametros(duracion)

        subtotal = self.tarifa_hora * duracion

        return self._aplicar_ajustes(
            subtotal, descuento, impuesto
        )

    def describir(self):
        """Esta se crea para mostrar las caracteristicas de la sala."""

        return (
            f"Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Tarifa: ${self.tarifa_hora:,.0f}/hora"
        )


# ============================================================
# 4. SERVICIO ESPECIALIZADO: ALQUILER DE EQUIPO
# ============================================================

# ADAPTACIÓN: tipo_equipo tiene valor predeterminado para simulacion.py.
class AlquilerEquipo(Servicio):
    """
    Esta clase representa el servicio de alquiler de equipos
    y hereda los atributos y métodos de la clase base Servicio.

    Su funcionamiento es similar al de SalaReunion, pero
    incorpora características específicas, como el tipo de
    equipo, la duración máxima del alquiler y un descuento
    adicional para alquileres prolongados.

    Aquí se aplican los conceptos de herencia y polimorfismo,
    ya que reutiliza funcionalidades de Servicio y sobrescribe
    métodos para implementar sus propias reglas.
    """

    def __init__(
        self, codigo, nombre, tarifa_hora, tipo_equipo="Equipo general",
        disponible=True
    ):
        super().__init__(codigo, nombre, tarifa_hora, disponible)

        if (
            not isinstance(tipo_equipo, str)
            or not tipo_equipo.strip()
        ):
            raise DatosInvalidosError(
                "El tipo de equipo es obligatorio."
            )

        self.tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self, duracion):
        """Esta valida la duracion del alquiler."""

        super().validar_parametros(duracion)

        if duracion > 72:
            raise DatosInvalidosError(
                "El equipo se puede alquilar maximo 72 horas."
            )

    def calcular_costo(
        self, duracion, descuento=0, impuesto=0.19
    ):
        """Esta calcula el costo del alquiler de equipos."""

        self.validar_parametros(duracion)

        subtotal = self.tarifa_hora * duracion

        # Descuento adicional para alquileres largos
        if duracion >= 24:
            subtotal *= 0.95

        return self._aplicar_ajustes(
            subtotal, descuento, impuesto
        )

    def describir(self):
        """Esta se crea para describir el equipo disponible."""

        return (
            f"Equipo: {self.nombre} | "
            f"Tipo: {self.tipo_equipo} | "
            f"Tarifa: ${self.tarifa_hora:,.0f}/hora"
        )


# ============================================================
# 5. SERVICIO ESPECIALIZADO: ASESORIA
# ============================================================

# ADAPTACIÓN: especialidad tiene valor predeterminado para simulacion.py.
class Asesoria(Servicio):
    """
    Esta clase representa el servicio de asesorías especializadas
    y hereda los atributos y métodos de la clase base Servicio.

    Su estructura es similar a las clases SalaReunion y
    AlquilerEquipo, pero incorpora características específicas,
    como el tipo de especialidad y la duración máxima de la
    asesoría.

    También aplica los conceptos de herencia y polimorfismo,
    permitiendo implementar reglas particulares para calcular
    costos y validar parámetros.
    """

    def __init__(
        self, codigo, nombre, tarifa_hora, especialidad="General",
        disponible=True
    ):
        super().__init__(codigo, nombre, tarifa_hora, disponible)

        if (
            not isinstance(especialidad, str)
            or not especialidad.strip()
        ):
            raise DatosInvalidosError(
                "La especialidad es obligatoria."
            )

        self.especialidad = especialidad.strip()

    def validar_parametros(self, duracion):
        """Esta se crea para validar la duracion permitida de una asesoria."""

        super().validar_parametros(duracion)

        if duracion > 4:
            raise DatosInvalidosError(
                "La asesoria puede durar maximo 4 horas."
            )

    def calcular_costo(
        self, duracion, descuento=0, impuesto=0.19
    ):
        """Esta calcula el costo de una asesoria."""

        self.validar_parametros(duracion)

        subtotal = self.tarifa_hora * duracion

        # Recargo para asesorias de mas de 2 horas
        if duracion > 2:
            subtotal *= 1.10

        return self._aplicar_ajustes(
            subtotal, descuento, impuesto
        )

    def describir(self):
        """Esta se crea para mostrar las caracteristicas de la asesoria."""

        return (
            f"Asesoria: {self.nombre} | "
            f"Especialidad: {self.especialidad} | "
            f"Tarifa: ${self.tarifa_hora:,.0f}/hora"
        )


# ============================================================
# 6. SIMULACION Y PRUEBAS DEL MODULO
# ============================================================

def ejecutar_demo():
    """
    Esta función permite comprobar que las diferentes clases
    de servicios especializados trabajan juntas mediante
    el uso del polimorfismo.
    """

    print("=== SOFTWARE FJ: MODULO DE SERVICIOS ===")

    # Se crea una lista que contiene objetos de diferentes
    # clases hijas: SalaReunion, AlquilerEquipo y Asesoria.
    # Esto permite recorrer los objetos y ejecutar métodos
    # comunes, como describir() y calcular_costo(),
    # demostrando el concepto de polimorfismo.

    servicios = [
        SalaReunion("S1", "Sala Ejecutiva", 50000, 12),
        AlquilerEquipo(
            "E1", "Portatil Lenovo", 15000, "Computador"
        ),
        Asesoria(
            "A1", "Consultoria de sistemas", 80000, "Tecnologia"
        )
    ]

    for servicio in servicios:

        print("\n" + servicio.describir())

        # Costo sin descuento ni impuesto
        print(
            "Costo 2 horas:",
            servicio.calcular_costo(2)
        )

        # Costo con descuento
        print(
            "Con 10% de descuento:",
            servicio.calcular_costo(2, 0.10)
        )

        # Costo con descuento e impuesto
        print(
            "Con 10% de descuento y 19% de impuesto:",
            servicio.calcular_costo(2, 0.10, 0.19)
        )

    # ========================================================
    # 7. PRUEBAS DE EXCEPCIONES
    # ========================================================

    print("\n=== PRUEBAS DE VALIDACIONES ===")

    pruebas = [
        (
            "Duracion negativa",
            lambda: servicios[0].calcular_costo(-2)
        ),
        (
            "Duracion excesiva",
            lambda: servicios[2].calcular_costo(8)
        ),
        (
            "Descuento invalido",
            lambda: servicios[1].calcular_costo(2, 1.5)
        ),
        (
            "Servicio no disponible",
            lambda: SalaReunion(
                "S2", "Sala Cerrada", 40000, 8, False
            ).calcular_costo(1)
        ),
        (
            "Tarifa invalida",
            lambda: AlquilerEquipo(
                "E2", "Impresora", -5000, "Impresora"
            )
        )
    ]

    for etiqueta, prueba in pruebas:
        try:
            prueba()

        except ErrorServicio as error:
            print(
                f"{etiqueta}: error controlado -> {error}"
            )


# ============================================================
# 8. EJECUTAR EL PROGRAMA
# ============================================================

if __name__ == "__main__":
    ejecutar_demo()
