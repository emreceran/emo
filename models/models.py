# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Excel'den gelecek sabit alanlar
    sicil_no = fields.Char(string='Sicil No', index=True)
    kimlik_no = fields.Char(string='Kimlik No')
    kurum_adi = fields.Char(string='Kurum')
    bolge_adi = fields.Char(string='Bölge (Detay)')
    
    # Analiz tablosu bağlantısı
    analiz_ids = fields.One2many('fr_26.analiz', 'partner_id', string='Saha Analizleri')

class SahaAnaliz(models.Model):
    _name = 'fr_26.analiz'
    _description = 'Saha Analiz Sonuçları'
    _order = 'create_date desc'

    partner_id = fields.Many2one('res.partner', string='Müşteri', required=True)
    user_id = fields.Many2one('res.users', string='Personel', default=lambda self: self.env.user)
    
    # Mobil uygulamadan gelecek sınırsız metinler
    oy = fields.Char(string='Oy', required=True)
    taraf = fields.Char(string='Taraf', required=True)
    
    create_date = fields.Datetime(string='Tarih', default=fields.Datetime.now)