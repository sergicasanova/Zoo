{
    'name': 'Zoo',
    'version': '1.8',
    'category': 'Operations/Zoo',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/zoo_views.xml',
        'views/zoo_animal_views.xml',
        'views/zoo_especie_views.xml',
        'views/zoo_habitat_views.xml',
        'views/zoo_menu.xml',
    ],
}