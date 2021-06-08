class Repository:
    def __init__(self):
        self.personas = {}
        self.persona_id_auto_increment = 0
        self.mails = {}
        self.mail_id_auto_increment = 0

    def add_persona(self, p):
        if p.persona_id is None:
            self.persona_id_auto_increment += 1
            p.persona_id = self.persona_id_auto_increment
        self.personas[p.persona_id] = p
        return p

    def add_mail(self, m):
        if m.mail_id is None:
            self.mail_id_auto_increment += 1
            m.mail_id = self.mail_id_auto_increment
        self.mails[m.mail_id] = m
        return m

    def to_string(self, persona_id=None, mail_id=None):
        if persona_id is not None:
            mails = ''
            for mail in self.mails.values():
                if persona_id == mail.persona_id:
                    mails += '\n    ' + str(mail)
            return str(self.personas[persona_id]) + mails

        if mail_id is not None:
            persona = ''
            mail = self.mails[mail_id]
            if mail.persona_id is not None:
                persona = str(self.personas[mail.persona_id])
            return str(mail) + '\n    ' + persona
