from odoo import models, fields, api

class LegalHearing(models.Model):
    _name = 'legal.hearing'
    _description = 'Legal Hearing'

    name = fields.Char(string='Hearing Title', required=True)
    case_id = fields.Many2one('legal.case', string='Case', required=True)
    date_start = fields.Datetime(string='Start Date', required=True)
    date_end = fields.Datetime(string='End Date', required=True)
    location = fields.Char(string='Location')
    status = fields.Selection([
        ('planned', 'Planned'),
        ('held', 'Held'),
        ('adjourned', 'Adjourned'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='planned')
    notes = fields.Text(string='Notes')

