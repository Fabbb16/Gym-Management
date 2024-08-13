from odoo import http
from odoo.http import request
import json


class TrainerAssign(http.Controller):
    @http.route('/diet/assign', type='json', auth='public', csrf=False, methods=['POST'])
    def index(self, **kwargs):
        #kerkohet api_key
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api Key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikohet nese api_key eshte i trainerit
        trainer = request.env['wb.trainer'].sudo().search([('api_key', '=', api_key)])
        if not trainer:
            return {'Success': False, 'Message': 'This page can only be accessed by trainers'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        member_id = json_data.get('member_id')
        diet_id = json_data.get('diet_id')


        if not member_id:
            return {'Success': False, 'Message': 'Invalid member id'}

        if not diet_id:
            return {'Success': False, 'Message': 'Invalid diet id'}

        Member = request.env['wb.member'].sudo()
        Diet = request.env['wb.diet'].sudo()

        member = Member.browse(member_id)
        diet = Diet.browse(diet_id)

        if not member.exists():
            return {'Success': False, 'Message': 'Member does not exists'}

        if not diet.exists():
            return {'Success': False, 'Message': 'Diet does not exists'}

        member.diet_id = diet_id

        json_response = {
            'member_name': member.name,
            'diet_name': diet.name
        }

        return {'Success': True, 'Message':'Diet assigned successfully!', 'data': json_response}




    @http.route('/member/assign', type='json', auth='public', csrf=False, methods=['POST'])
    def member(self, **kwargs):
        #kerkohet apiKey
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api Key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikohet nese eshte api key i trajnerit
        trainer = request.env['wb.trainer'].sudo().search([('api_key', '=', api_key)])
        if not trainer:
            return {'Success': False, 'Message': 'This page can only be accessed by trainers'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        class_id = json_data.get('class_id')
        member_id = json_data.get('member_id')

        if not class_id:
            return {'Success': False, 'Message': 'Invalid class id'}

        if not member_id:
            return {'Success': False, 'Message': 'Invalid member id'}

        Gym_class = request.env['gym.class'].sudo()
        Member = request.env['wb.member'].sudo()

        gym_class = Gym_class.browse(class_id)
        member = Member.browse(member_id)

        if not gym_class.exists():
            return {'Success': False, 'Message': 'Gym class does not exists'}

        if not member.exists():
            return {'Success': False, 'Message': 'Member does not exists'}

        gym_class.member_id = [(4, member_id)]

        json_response = {
            'gym_class_name': gym_class.name,
            'member': member.name
        }

        return {'Success': True, 'Message': 'Member assigend successfully', 'data': json_response}


    @http.route('/equipment/assign', type='json', auth='public', csrf=False, methods=['POST'])
    def equipment(self, **kwargs):
        #kerkohet api_key
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api Key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikojm nqs apikey eshte i trajnerit
        trainer = request.env['wb.trainer'].sudo().search([('api_key', '=', api_key)])
        if not trainer:
            return {'Success': False, 'Message': 'This page can only be accessed by trainers'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        class_id = json_data.get('class_id')
        equipments_id = json_data.get('equipments_id')

        if not class_id:
            return {'Success': False, 'Message': 'Class id not found'}

        if not equipments_id:
            return {'Success': False, 'Message': 'Equipment id not found'}

        Gym_class = request.env['gym.class'].sudo()
        Equipments = request.env['wb.equipment'].sudo()

        gym_class = Gym_class.browse(class_id)
        equipments = Equipments.browse(equipments_id)

        if not gym_class.exists():
            return {'Success': False, 'Message': 'Gym Class does not exists'}

        if not equipments.exists():
            return {'Success': False, 'Message': 'Equipment does not exists'}

        gym_class.equipments_id = [(4, equipments_id)]

        json_response = {
            'gym_class_name': gym_class.name,
            'equipment': equipments.name
        }

        return {'Success': True, 'Message': 'Equipment assigned successfully!!', 'data': json_response}