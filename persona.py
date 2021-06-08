class Persona:
    def __init__(self, apellido='', nombre=''):
        self.persona_id = None
        self.apellido = apellido
        self.nombre = nombre

    @property
    def persona_id(self):
        return self.__persona_id

    @persona_id.setter
    def persona_id(self, value):
        self.__persona_id = value

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    def __repr__(self):
        return '{}/{}, {}'.format(self.__persona_id,
                                  self.__apellido,
                                  self.__nombre)
