from app.main import bp


@bp.route('/')
def index():
    """Index route of the applcication"""
    return 'This is The Main Blueprint'
