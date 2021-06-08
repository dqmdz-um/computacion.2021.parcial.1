class Mail:
    def __init__(self, mail='', tipo='', persona_id=None):
        if '@' not in mail:
            raise Exception('mail without @')
        self.mail_id = None
        self.mail = mail
        self.tipo = tipo
        self.persona_id = persona_id

    @property
    def mail_id(self):
        return self.__mail_id

    @mail_id.setter
    def mail_id(self, value):
        self.__mail_id = value

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, value):
        self.__mail = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @property
    def persona_id(self):
        return self.__persona_id

    @persona_id.setter
    def persona_id(self, value):
        self.__persona_id = value

    def __repr__(self):
        return '{} - {}/{} - {}'.format(self.__mail_id,
                                        self.__tipo,
                                        self.__mail,
                                        self.__persona_id)
