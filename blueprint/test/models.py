from myproject.framework._globals import get_globals_object, set_globals_object

db, login_manager = get_globals_object("db", "login_manager")

class LoginUser(db.Model):
    __tablename__ = "LoginUser"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    proxyManager = db.Column(db.Integer, db.ForeignKey("ProxyManager.id"))

class ProxyManager(db.Model):
    __tablename__ = "ProxyManager"
    id = db.Column(db.Integer, primary_key=True)
    proxyName = db.Column(db.String(64))
    allUser = db.relationship("LoginUser", lazy="dynamic")

