from flask import render_template, request, redirect, url_for, flash, make_response
from flask_smorest import Blueprint
from flask.views import MethodView

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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
        headers = request.form.get('headers')
        dkim = request.form.get('dkim')
        content_ids = request.form.get('content-ids')
        to = request.form.get('to')
        text = request.form.get('text')
        html = request.form.get('html')
        from_email = request.form.get('from')
        sender_ip = request.form.get('sender_ip')
        spam_report = request.form.get('spam_report')
        envelope = request.form.get('envelope')
        attachments = request.form.get('attachments')
        subject = request.form.get('subject')
        spam_score = request.form.get('spam_score')
        attachment_info = request.form.get('attachment-info')
        charsets = request.form.get('charsets')
        spf = request.form.get('SPF')

        subject = subject + ' [From: ' + from_email + ']'
        message = Mail(
            from_email="inbox@yougao.dev",
            to_emails=to,
            subject=subject,
            html_content=html)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        
        return redirect(url_for('forward.EmailForward'))

@bp.route('/send')
class SendEmail(MethodView):
    @bp.doc(description="Return pets based on ID", summary="Find pets by ID")
    @bp.response(200)
    def get(self):

        message = Mail(
            from_email='mail@yougao.dev',
            to_emails='djx3rn@virginia.edu',
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong>')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
        except Exception as e:
            print(e.message)
                        
        return make_response('Email Sent')
    
    @bp.response(201)
    def post(self):
        return redirect(url_for('forward.SendEmail'))
    
    @bp.route('/test')
    class TestEmail(MethodView):
        @bp.doc(description="Return pets based on ID", summary="Find pets by ID")
        @bp.response(200)
        def get(self):
            with open("called.txt", "w") as f:
                f.write("Visited")
            return make_response('Email Sent')
        
        @bp.response(201)
        def post(self):
            with open("called.txt", "w") as f:
                f.write("Called")
            return make_response('Email Sent', 201)