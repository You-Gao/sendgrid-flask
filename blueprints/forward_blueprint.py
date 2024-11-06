from flask import render_template, request, redirect, url_for, flash, make_response
from flask_smorest import Blueprint
from flask.views import MethodView

bp = Blueprint('forward', 'forward', url_prefix='/forward', description='Forwarding SendGrid Email Payloads')

@bp.route('/')
class EmailForward(MethodView):
    @bp.doc(description="Return pets based on ID", summary="Find pets by ID")
    @bp.response(200)
    def get(self):
        response = make_response(render_template('forward.html'))
        response.headers['Content-Type'] = 'text/html'
        return response
    
    
    @bp.response(201)
    def post(self):
        url = request.form['url']
        return redirect(url)
    