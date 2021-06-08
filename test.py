import unittest
from parameterized import parameterized
from mail import Mail
from persona import Persona
from repository import Repository


class TestApp(unittest.TestCase):

    @parameterized.expand([
        ('Doe',
         'John',
         {'_Persona__apellido': 'Doe',
          '_Persona__nombre': 'John',
          '_Persona__persona_id': None}),
        ('Clayton',
         'Jane',
         {'_Persona__apellido': 'Clayton',
          '_Persona__nombre': 'Jane',
          '_Persona__persona_id': None}),
    ])
    def test_atributos_persona(self, apellido, nombre, atributos):
        object = Persona(apellido, nombre)
        self.assertDictEqual(object.__dict__, atributos)

    @parameterized.expand([
        ('b@b.com',
         'personal',
         {'_Mail__mail_id': None,
          '_Mail__mail': 'b@b.com',
          '_Mail__tipo': 'personal',
          '_Mail__persona_id': None}),
        ('john@doe.org',
         'laboral',
         {'_Mail__mail_id': None,
          '_Mail__mail': 'john@doe.org',
          '_Mail__tipo': 'laboral',
          '_Mail__persona_id': None}),
    ])
    def test_atributos_mail(self, mail, tipo, atributos):
        object = Mail(mail, tipo)
        self.assertDictEqual(object.__dict__, atributos)

    @parameterized.expand([
        ('a@a.com',
         'personal',
         'None - personal/a@a.com - None'),
        ('doctor@strange.com',
         'laboral',
         'None - laboral/doctor@strange.com - None',
         )
    ])
    def test_mail_repr(self, mail, tipo, repr):
        object = Mail(mail, tipo)
        self.assertEqual(str(object), repr)

    def test_valid_mail(self):
        object = Mail('valid@email.com', 'laboral')
        self.assertIsNotNone(object)

    def test_invalid_mail(self):
        object = None
        with self.assertRaises(Exception):
            object = Mail('invalidemail.com', 'laboral')
        self.assertIsNone(object)

    def test_to_string_persona(self):
        r = Repository()
        p1 = r.add_persona(Persona(apellido='Doe', nombre='John'))
        p2 = r.add_persona(Persona(apellido='Doe', nombre='Jane'))
        r.add_mail(Mail('a@a.com', 'personal', p1.persona_id))
        r.add_mail(Mail('a@j.com', 'personal', p2.persona_id))
        r.add_mail(Mail('b@a.com', 'laboral', p1.persona_id))
        r.add_mail(Mail('b@j.com', 'laboral', p2.persona_id))
        self.assertEqual(r.to_string(persona_id=2),
                         '2/Doe, Jane' +
                         '\n    2 - personal/a@j.com - 2' +
                         '\n    4 - laboral/b@j.com - 2'
                         )

    def test_to_string_mail(self):
        r = Repository()
        p1 = r.add_persona(Persona(apellido='Doe', nombre='John'))
        p2 = r.add_persona(Persona(apellido='Doe', nombre='Jane'))
        r.add_mail(Mail('a@a.com', 'personal', p1.persona_id))
        r.add_mail(Mail('a@j.com', 'personal', p2.persona_id))
        r.add_mail(Mail('b@a.com', 'laboral', p1.persona_id))
        r.add_mail(Mail('b@j.com', 'laboral', p2.persona_id))
        self.assertEqual(r.to_string(mail_id=3),
                         '3 - laboral/b@a.com - 1' +
                         '\n    1/Doe, John'
                         )


if __name__ == '__main__':
    unittest.main()
