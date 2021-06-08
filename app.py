from persona import Persona
from mail import Mail
from repository import Repository

if __name__ == '__main__':
    r = Repository()
    p1 = r.add_persona(Persona(apellido='Doe', nombre='John'))
    p2 = r.add_persona(Persona(apellido='Doe', nombre='Jane'))
    m1 = r.add_mail(Mail('a@a.com', 'personal', p1.persona_id))
    m2 = r.add_mail(Mail('a@j.com', 'personal', p2.persona_id))
    m3 = r.add_mail(Mail('b@a.com', 'laboral', p1.persona_id))
    m4 = r.add_mail(Mail('b@j.com', 'laboral', p2.persona_id))
    print(r.to_string(persona_id=1))
    print(r.to_string(mail_id=1))
    print(r.to_string(persona_id=2))
    print(r.to_string(mail_id=3))
