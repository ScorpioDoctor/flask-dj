from flask import  Blueprint, request, jsonify, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask_dj.globals import admin
from .model import db, SendSMS, ApplyInfo, User
from .utils import send_vcode



app = Blueprint('Base', __name__)


@app.route('/')
def index():
    User.query.all()
    return 'this is flask_dj', 200

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Base.login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('Base/login.html')
    elif request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        if username and password:
            user = User.query.filter_by(username=username).first()
            if user and login_user(user):
                return redirect(url_for('admin.index'))
            else:
                return render_template('Base/login.html', login_status=False)
    return 'not found', 404
def sendsms():
    result = {
        'status': False,
    }
    phone = request.form.get('phone', None)
    db_SendSMS = SendSMS.query.filter_by(phone=phone).first()
    if not db_SendSMS:
        db_SendSMS = SendSMS(phone=phone)
        db.session.add(db_SendSMS)
        db_SendSMS = SendSMS.query.filter_by(phone=phone).first()
    else:
        db_SendSMS = SendSMS.query.filter_by(phone=phone).first()
    
    if db_SendSMS.count > 10:
        result['msg'] = '您的手机今日次数过多'
        return jsonify(result)
    else:
        status, vcode = send_vcode(phone)
        db_SendSMS.vcode = vcode
        db_SendSMS.count +=1
        # 更新数据库
        db.session.commit()
        result['status'] = True
        result['msg'] = '发送成功'
        return jsonify(result)

def apply():
    result = {}
    db_SendSMS = SendSMS.query.filter_by(phone=request.form.get('phone', None), vcode=request.form.get('vcode', None)).first()
    db_write = False
    if db_SendSMS:
        db_ApplyInfo = ApplyInfo.query.filter_by(phone=request.form.get('phone', None)).first()
        if not db_ApplyInfo:
            db_ApplyInfo = ApplyInfo(phone=request.form.get('phone', None))
            db.session.add(db_ApplyInfo)
            db.session.commit()
            db_ApplyInfo = ApplyInfo.query.filter_by(phone=request.form.get('phone', None)).first()
            if db_ApplyInfo:
                db_write = True
        else:
            db_write = True
    else:
        result['msg'] = '提交失败，验证码不正确'

    if db_write:
        db_SendSMS.vcode = '5641'
        db_ApplyInfo.je = request.form.get('je', None)
        db_ApplyInfo.yt = request.form.get('yt', None)
        db_ApplyInfo.name = request.form.get('name', None)
        db_ApplyInfo.city = request.form.get('city', None)
        db.session.commit()
    
    result['status'] = db_write,
    if db_write:
        result['msg'] = '提交成功'
    return jsonify(result)