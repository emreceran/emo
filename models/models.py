# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sorumlu_id = fields.Many2one('res.users', string='Sorumlu Personel', index=True)
    etiketleyen_id = fields.Many2one('res.users', string='Etiketleyen Personel', readonly=True)

    taraf = fields.Selection([
        ('kirmizi', 'Kırmızı'),
        ('mavi', 'Mavi'),
        ('yesil', 'Yeşil'),
        ('beyaz', 'Beyaz (Tarafsız)'), # Yeni seçeneğimiz
    ], string='Taraf Seçimi')

    sicil_no = fields.Char(string='Sicil No', index=True)
    kimlik_no = fields.Char(string='TC Kimlik No')
    kurum_adi = fields.Char(string='Kurum Adı')
    bolge_adi = fields.Char(string='Bölge (Detay)')