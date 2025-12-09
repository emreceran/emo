# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class SahaApi(http.Controller):

    @http.route('/api/login', type='json', auth='public', methods=['POST'], csrf=False)
    def login(self, db, login, password):
        try:
            # Dedektif sonucuna göre çözüm:
            # Fonksiyon (dbname, credential) bekliyor.
            # Biz de login ve password'ü bir sözlük (dictionary) içine paketliyoruz.
            
            my_credentials = {
                'login': login, 
                'password': password,
                'type': 'password'  # Bazı sistemler bunu da ister, eklemekte zarar yok.
            }

            # Artık 3 parça değil, 2 parça (db ve paket) gönderiyoruz.
            uid = request.session.authenticate(db, my_credentials)
            
            if uid:
                return {
                    'status': 'success', 
                    'session_id': request.session.sid, 
                    'user_id': uid,
                    'message': 'Giris Basarili'
                }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
        
        return {'status': 'error', 'message': 'Giris Basarisiz (UID Donmedi)'}
    

    @http.route('/api/musteriler', type='json', auth='user', methods=['POST'], csrf=False)
    def get_musteriler(self, page=0, limit=50):
        offset = page * limit
        user = request.env.user
        domain = []
        if user.partner_id.state_id:
            domain = [('state_id', '=', user.partner_id.state_id.id)]

        data = request.env['res.partner'].search_read(
            domain, 
            ['id', 'name', 'mobile', 'state_id', 'sicil_no', 'kimlik_no', 'kurum_adi', 'bolge_adi'], 
            offset=offset, limit=limit
        )
        
        return {'status': 'success', 'count': len(data), 'data': data}

    @http.route('/api/etiketle', type='json', auth='user', methods=['POST'], csrf=False)
    def etiketle(self, customer_id, oy, taraf):
        try:
            request.env['fr_26.analiz'].create({
                'partner_id': int(customer_id),
                'user_id': request.env.user.id,
                'oy': oy,
                'taraf': taraf
            })
            return {'status': 'success', 'message': 'Kaydedildi'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}