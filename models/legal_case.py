from odoo import models, fields, api

class LegalCase(models.Model):
    _name = 'legal.case'
    _description = 'Legal Case'

    name = fields.Char(string='Case Reference', default='New')
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    responsible_lawyer_id = fields.Many2one('res.partner', string='Lawyer', required=True)
    case_type = fields.Selection([
        ('civil', 'Civil'),
        ('criminal', 'Criminal'),
        ('family', 'Family'),
        ('corporate', 'Corporate'),
    ], string='Case Type', required=True)
    stage = fields.Selection([
        ('intake', 'Intake'),
        ('active', 'Active'),
        ('closed', 'Closed'),
    ], string='Stage', default='intake')
    open_date = fields.Date(string='Open Date', default=fields.Date.today)
    close_date = fields.Date(string='Close Date')
    description = fields.Text(string='Description')
    
    hearing_ids = fields.One2many('legal.hearing', 'case_id', string='Hearings')
    hearing_count = fields.Integer(string='Hearing Count', compute='_compute_hearing_count')

    @api.depends('hearing_ids')
    def _compute_hearing_count(self):
        for case in self:
            case.hearing_count = len(case.hearing_ids)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('legal.case') or 'New'
        return super().create(vals)

    def write(self, vals):
        if 'stage' in vals and vals['stage'] == 'closed':
            vals['close_date'] = fields.Date.today()
        return super().write(vals)
