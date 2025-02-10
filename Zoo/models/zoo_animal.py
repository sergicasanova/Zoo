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
    imagen = fields.Binary()
    color = fields.Integer()
    
    zoo_id = fields.Many2one('zoo.zoo', string='Zoo')
    habitat_id = fields.Many2one('zoo.habitat', string='Hábitat')
    especie = fields.Many2one('zoo.animal.especie', string='Especie', required=True)

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

    @api.constrains('habitat_id')
    def _check_zoo_habitat_match(self):
        for animal in self:
            if animal.habitat_id and animal.habitat_id.zoo_id != animal.zoo_id:
                raise models.ValidationError('El hábitat debe pertenecer al mismo zoo que el animal.')

    @api.model
    def create(self, vals):
        record = super(ZooAnimal, self).create(vals)
        record.zoo_id._compute_cantidad_animales()
        return record


