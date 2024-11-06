from flask import render_template, request, redirect, url_for, flash, make_response
from flask_smorest import Blueprint
from flask.views import MethodView

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import logging as log

bp = Blueprint('forward', 'forward', url_prefix='/forward', description='Forwarding SendGrid Email Payloads')

@bp.route('/')
class EmailForward(MethodView):
    @bp.doc(description="Return pets based on ID", summary="Find pets by ID")
    @bp.response(200)
    def get(self):
        response = make_response(render_template('form.html'))
        response.headers['Content-Type'] = 'text/html'
        return response
    
    @bp.response(201)
    def post(self):

        text = request.form.get('text')
        html = request.form.get('html')
        from_email = request.form.get('from')
        subject = request.form.get('subject')

        subject = subject + ' [From: ' + from_email + ']'
        message = Mail(
            from_email="inbox@yougao.dev",
            to_emails="yougaowork@gmail.com",
            subject=subject,
            html_content=html,
            plain_text_content=text)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
        
        return make_response('Email Sent', 201)

# @bp.route('/send')
# class SendEmail(MethodView):
#     @bp.doc(description="Return pets based on ID", summary="Find pets by ID")
#     @bp.response(200)
#     def get(self):

#         message = Mail(
#             from_email='henry@yougao.dev',
#             to_emails='yougaowork@gmail.com',
#             subject='Sending with Twilio SendGrid is Fun',
#             html_content='<strong>and easy to do anywhere, even with Python</strong>')
#         try:
#             sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#             response = sg.send(message)
#             print(response.status_code)
#             print(response.body)
#             print(response.headers)
#         except Exception as e:
#             print(e)
                        
#         return make_response('Email Sent')
    
#     @bp.response(201)
#     def post(self):
#         return redirect(url_for('forward.SendEmail'))
    
# @bp.route('/test')
# class TestEmail(MethodView):
#     @bp.doc(description="Return pets based on ID", summary="Find pets by ID")
#     @bp.response(200)
#     def get(self):
#         with open("/tmp/called.txt", "w") as f:
#             f.write("Visited")
#         log.info("Visited")

#         return make_response('Email Sent')
    
#     @bp.response(201)
#     def post(self):
#         with open("/tmp/called.txt", "w") as f:
#             f.write("Posted")
#         log.info("Posted")

#         return make_response('Email Sent', 201)