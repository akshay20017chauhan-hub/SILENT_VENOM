import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'silent_venom_secret_key_12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    invite_code = db.Column(db.String(50), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def init_db():
    with app.app_context():
        db.create_all()
        # default admin as 'admin'
        admin = User.query.filter_by(phone='admin').first()
        if not admin:
            admin = User(
                phone='admin',
                is_admin=True,
                is_blocked=False,
                invite_code='ADMIN001'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()

# Initialize database on startup so Gunicorn creates tables
init_db()

@app.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        phone = request.form.get('phone', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()
        invite_code = request.form.get('invite_code', '').strip()

        if not phone or not password:
            flash('Please fill in the phone number and password.', 'danger')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        existing_user = User.query.filter_by(phone=phone).first()
        if existing_user:
            flash('This phone number is already registered.', 'danger')
            return redirect(url_for('register'))

        new_user = User(
            phone=phone,
            invite_code=invite_code,
            is_admin=False,
            is_blocked=False
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    inv_code = request.args.get('invitationCode', '326503098027')
    return render_template('register.html', invite_code=inv_code)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form.get('phone', '').strip()
        password = request.form.get('password', '').strip()

        user = User.query.filter_by(phone=phone).first()
        if not user or not user.check_password(password):
            flash('Incorrect phone number or password.', 'danger')
            return redirect(url_for('login'))

        if user.is_blocked:
            flash('Your account has been blocked. Please contact support.', 'danger')
            return redirect(url_for('login'))

        login_user(user)
        if user.is_admin:
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        phone = request.form.get('phone', '').strip()
        new_password = request.form.get('new_password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if not phone or not new_password:
            flash('Please fill in the phone number and new password.', 'danger')
            return redirect(url_for('forgot_password'))

        if new_password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('forgot_password'))

        user = User.query.filter_by(phone=phone).first()
        if not user:
            flash('This phone number is not registered.', 'danger')
            return redirect(url_for('forgot_password'))

        user.set_password(new_password)
        db.session.commit()
        flash('Password reset successfully! You can now log in with the new password.', 'success')
        return redirect(url_for('login'))

    return render_template('forgot_password.html')

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_blocked:
        logout_user()
        flash('Your account has been blocked.', 'danger')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Only Admin can access this page.', 'danger')
        return redirect(url_for('dashboard'))
    users = User.query.all()
    return render_template('admin.html', users=users)

@app.route('/admin/toggle_block/<int:user_id>', methods=['POST'])
@login_required
def toggle_block(user_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403

    user = User.query.get_or_404(user_id)
    if user.is_admin:
        return jsonify({'error': 'Admin user cannot be blocked.'}), 400

    user.is_blocked = not user.is_blocked
    db.session.commit()
    return jsonify({'success': True, 'is_blocked': user.is_blocked})

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/deposit')
@login_required
def deposit():
    return render_template('deposit.html')
    @app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
