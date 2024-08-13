from odoo import http
from odoo.http import request
import json

class RecAssign(http.Controller):
    @http.route('/rec/member', type='json', auth='public', csrf=False, methods=['POST'])
    def index(self, **kwargs):
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api key needed'}

        api_key = api_key.replace('Bearer ', '')

        rec = request.env['wb.rec'].sudo().search([('api_key', '=', api_key)])
        if not rec:
            return {'Success': False, 'Message': 'This page can only be accessed by Receptionists'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        subscription_id = json_data.get('subscription_id')
        member_id = json_data.get('member_id')

        if not subscription_id:
            return {'Success': False, 'Message': 'Invalid subscription id'}

        if not member_id:
            return {'Success': False, 'Message': 'Invalid member id'}

        Subscription = request.env['wb.subscription'].sudo()
        Member = request.env['wb.member'].sudo()

        subscription = Subscription.browse(subscription_id)
        member = Member.browse(member_id)

        if not subscription.exists():
            return {'Success': False, 'Message': 'Subscription does not exist'}

        if not member.exists():
            return {'Success': False, 'Message': 'Member does not exist'}

        subscription.member_id = member_id

        return {'Success': True, 'Message': f'Member {member.name} assigned successfully!!'}


    @http.route('/rec/membership', type='json', auth='public', csrf=False, methods=['POST'])
    def membership(self, **kwargs):
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'Api KEY needed'}

        api_key = api_key.replace('Bearer ', '')

        rec = request.env['wb.rec'].sudo().search([('api_key', '=', api_key)])
        if not rec:
            return {'Success': False, 'Message': 'This page can only be accessed by receptionists'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        subscription_id = json_data.get('subscription_id')
        membership_id = json_data.get('membership_id')

        if not subscription_id:
            return {'Success': False, 'Message': 'Invalid subscription Id'}

        if not membership_id:
            return {'Success': False, 'Message': 'Invalid membership Id'}

        Subscription = request.env['wb.subscription'].sudo()
        Membership = request.env['wb.membership'].sudo()

        subscription = Subscription.browse(subscription_id)
        membership = Membership.browse(membership_id)

        if not subscription.exists():
            return {'Success': False, 'Message': 'Subscription does not exist'}

        if not membership.exists():
            return {'Success': False, 'Message': 'Membership does not exists'}

        subscription.membership_id = membership_id

        return {'Success': True, 'Message': f'Membership {membership.name} assigned successfully!!'}

    @http.route('/rec/schedule', type='json' , auth='public', csrf=False)
    def schedule(self, **kwargs):
        #kerkohet api_key
        api_key = request.httprequest.headers.get('Authorization')
        if not api_key:
            return {'Success': False, 'Message': 'API key needed'}

        api_key = api_key.replace('Bearer ', '')

        #verifikohet nese apiKey eshte i rec
        rec = request.env['wb.rec'].sudo().search([('api_key', '=', api_key)])
        if not rec:
            return {'Success': False, 'Message': 'This page can only be accessed by receptionists'}

        try:
            json_data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return {'Success': False, 'Message': 'Invalid JSON data'}

        schedule_id = json_data.get('schedule_id')
        trainer_id = json_data.get('trainer_id')

        if not schedule_id:
            return {'Success': False, 'Message': 'Schedule id not found'}

        if not trainer_id:
            return {'Success': False, 'Message': 'Trainer id not found'}

        Schedule = request.env['wb.schedule'].sudo()
        Trainer = request.env['wb.trainer'].sudo()

        schedule = Schedule.browse(schedule_id)
        trainer = Trainer.browse(trainer_id)

        if not schedule.exists():
            return {'Success': False, 'Message': 'Schedule does not exists'}

        if not trainer.exists():
            return {'Success': False, 'Message': 'Trainer does not exists'}


        schedule.trainer_id = trainer_id

        return {'Success': True, 'Message': f'Trainer {trainer.name} assigend successfully'}
