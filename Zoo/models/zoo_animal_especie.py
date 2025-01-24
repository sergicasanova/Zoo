from odoo import fields, models, api

class ZooAnimalEspecie(models.Model):
    _name = 'zoo.animal.especie'
    _description = 'Especie de Animal'

    name = fields.Char(string='Especie', required=True)
    en_peligro = fields.Boolean(string='En Peligro')
    familia = fields.Char(string='Familia')
    nombre_vulgar = fields.Char(string='Nombre Vulgar')
    nombre_cientifico = fields.Char(string='Nombre Cientifico')
    peligrosidad = fields.Selection(
        [('baja', 'Baja'), ('moderada', 'Moderada'), ('alta', 'Alta'), ('critica', 'Critica')], string='Peligrosidad')
    # Este estara relacionado con zoo_animal para la obtencion de estos datos genericos de la especie de cada animal
    animal_ids = fields.One2many('zoo.animal', 'especie', string='Animales')
    
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'El nombre de la especie debe ser unico!'),
    ]   