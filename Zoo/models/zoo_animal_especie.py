from odoo import fields, models, api

class ZooAnimalEspecie(models.Model):
    _name = 'zoo.animal.especie'
    _description = 'Especie de Animal'

    name = fields.Char(string='Especie', required=True)
    id_especie = fields.Integer(string='id_especie', required=True)
    en_peligro = fields.Boolean(string='En Peligro')
    familia = fields.Char(string='Familia')
    nombre_vulgar = fields.Char(string='Nombre Vulgar')
    nombre_cientifico = fields.Char(string='Nombre Cientifico')

    # Este estara relacionado con zoo_animal para la obtencion de estos datos genericos de la especie de cada animal