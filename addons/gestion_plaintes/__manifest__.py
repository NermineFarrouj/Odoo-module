{
    'name': 'Gestion des Plaintes Internes',
    'version': '1.0',
    'summary': 'Gestion des plaintes internes des employés',
    'author': 'Votre Nom',
    'category': 'Human Resources',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/plainte_views.xml',
    ],
    'installable': True,
    'application': True,
}