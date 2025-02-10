from odoo import fields, models

class ZooTags(models.Model):
    _name = "zoo.tags"
    _description = "Zoo Tags"

    name = fields.Char(required=True, unique=True)
    color = fields.Integer()
    icon = fields.Char(string='Icono', default="fa fa-tag")
    _sql_constraints = [
        ('check_name', 'unique(name)', 'The property name shall be unique !')
    ]