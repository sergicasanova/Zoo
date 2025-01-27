from odoo import fields, models, api

class ZooAnimal(models.Model):
    _name = 'zoo.animal'
    _description = 'Animal'

    raza = fields.Char(string='Raza', required=True)
    name = fields.Char(string='Nombre', required=True)
    continente_origen_animal = fields.Selection(
        [('africa', 'Africa'), 
         ('america', 'America'), 
         ('asia', 'Asia'), 
         ('europa', 'Europa'), 
         ('oceania', 'Oceania')], string='Continente de Origen')
    pais_id = fields.Many2one('res.country', string='Pais de Origen')
    sexo = fields.Selection([('macho', 'Macho'), ('hembra', 'Hembra')], string='Sexo')
    fecha_nacimiento = fields.Date(string='Fecha Nacimiento')
    edad = fields.Integer(string='Edad', compute='_compute_edad')
    descripcion = fields.Text(string='Descripción')
    enfermo = fields.Boolean(string='Enfermo')
    tipo_de_enfermedad = fields.Char(string='Tipo de Enfermedad')
    dieta = fields.Selection(
        [('carnivoro', 'Carnívoro'), 
         ('herbivoro', 'Herbívoro'), 
         ('omnivoro', 'Omnívoro')], string='Dieta')
    
    zoo_id = fields.Many2one('zoo.zoo', string='Zoo')
    habitat_id = fields.Many2one('zoo.habitat', string='Hábitat')
    especie = fields.Many2one('zoo.animal.especie', string='Especie', required=True)

    # animal estara relacionado con zoo, sera una relacion de uno a muchos, puesto que un
    # animal podra estar en un zoo, pero un zoo podra tener muchos animales
    # luego mediante zoo obtendremos el habitat donde estara residiendo dicho animal, es decir
    # la jirafa tal, esta en el zoo tal y reside en el habitat de la sabana.
    # hacer un sql-constraint para que la fecha de nacimiento no sea mayor a la fecha actual

    _sql_constraints = [
        ('fecha_nacimiento', 'CHECK(fecha_nacimiento <= CURRENT_DATE)', 'La fecha de nacimiento no puede ser mayor a la fecha actual!'),
        ('sexo', 'CHECK(sexo IN (\'macho\', \'hembra\'))', 'El sexo debe ser macho o hembra!'),
    ]

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for animal in self:
            if animal.fecha_nacimiento:
                edad = (fields.Date.today() - animal.fecha_nacimiento).days / 365
                animal.edad = round(edad)
            else:
                animal.edad = 0


    @api.model
    def create(self, vals):
        record = super(ZooAnimal, self).create(vals)
        record.zoo_id._compute_cantidad_animales()
        return record


