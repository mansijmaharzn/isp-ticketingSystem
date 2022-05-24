from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Ticket, Notification
from . import db
import json

views = Blueprint('views', __name__)


# User
@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('/support', methods=['GET', 'POST'])
@login_required
def support():
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')

        # Ticket
        new_ticket = Ticket(
            title=title, desc=desc, username=current_user.first_name, status="Pending", user_id=current_user.id)
        db.session.add(new_ticket)
        db.session.commit()
        flash("Ticket Opened! We'll contact you soon.", category='success')
        # Notificaation
        new_notification = Notification(
            message="New Ticket Created!", status="success", user_id=current_user.id)
        db.session.add(new_notification)
        db.session.commit()

        return redirect(url_for('views.tickets'))

    return render_template('support.html', user=current_user)


@views.route('/tickets')
@login_required
def tickets():
    return render_template('tickets.html', user=current_user)


@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


# Admin
@views.route('/admin-dashboard')
@login_required
def adminDashboard():
    allTicket = Ticket.query.all()
    return render_template('admin_dashboard.html', user=current_user, allTicket=allTicket)


# @views.route('/delete-ticket', methods=['POST'])
# @login_required
# def delete_ticket():
#     ticket = json.loads(request.data)
#     ticketId = ticket['ticketId']
#     ticket = Ticket.query.get(ticketId)
#     if ticket:
#         if ticket.user_id == current_user.id:
#             db.session.delete(ticket)
#             db.session.commit()

#     return jsonify({})


@views.route('/close-ticket', methods=['POST'])
@login_required
def close_ticket():
    ticket = json.loads(request.data)
    print(ticket)
    ticketId = ticket['ticketId']
    ticket = Ticket.query.get(ticketId)
    if ticket:
        ticket.status = "Closed"
        db.session.commit()

    return jsonify({})


@views.route('/solve-ticket', methods=['POST'])
@login_required
def solve_ticket():
    ticket = json.loads(request.data)
    print(ticket)
    ticketId = ticket['ticketId']
    ticket = Ticket.query.get(ticketId)
    if ticket:
        ticket.status = "Solved"
        db.session.commit()

    return jsonify({})
