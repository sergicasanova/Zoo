from odoo import fields, models, api

class ZooAnimal(models.Model):
    _name = 'zoo.animal'
    _description = 'Animal'

    raza = fields.Char(string='Raza', required=True)
    id_animal = fields.Integer(string='id_animal', required=True)
    continente_origen_animal = fields.Selection(
        [('africa', 'Africa'), 
         ('america', 'America'), 
         ('asia', 'Asia'), 
         ('europa', 'Europa'), 
         ('oceania', 'Oceania')], 
         string='Continente de Origen')
    pais_origen_animal = fields.Many2one('res.country', string='Pais de Origen')
    sexo = fields.Selection([('macho', 'Macho'), ('hembra', 'Hembra')], string='Sexo')
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    especie = fields.Many2one('zoo.animal.especie', string='Especie', required=True)
    edad = fields.Integer(string='Edad', compute='_compute_edad')
    disponible = fields.Boolean(string='Disponible para la visita')
    descripcion = fields.Text(string='Descripción')

    # animal estara relacionado con zoo, sera una relacion de uno a muchos, puesto que un
    # animal podra estar en un zoo, pero un zoo podra tener muchos animales
    # luego mediante zoo obtendremos el habitat donde estara residiendo dicho animal, es decir
    # la jirafa tal, esta en el zoo tal y reside en el habitat de la sabana.

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for animal in self:
            if animal.fecha_nacimiento:
                edad = (fields.Date.today() - animal.fecha_nacimiento).days / 365
                animal.edad = edad