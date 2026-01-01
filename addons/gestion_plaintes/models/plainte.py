from odoo import models, fields

class PlainteInterne(models.Model):
    _name = 'gestion.plainte'
    _description = 'Plainte Interne'

    reference = fields.Char(string="Référence", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employé", required=True)
    type_plainte = fields.Selection([
        ('harcelement', 'Harcèlement'),
        ('discipline', 'Discipline'),
        ('autre', 'Autre')
    ], string="Type de plainte", required=True)

    description = fields.Text(string="Description")
    date_plainte = fields.Date(string="Date", default=fields.Date.today)
    statut = fields.Selection([
        ('nouveau', 'Nouveau'),
        ('encours', 'En cours'),
        ('traite', 'Traité')
    ], string="Statut", default='nouveau')