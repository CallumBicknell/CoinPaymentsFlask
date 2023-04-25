# CoinPaymentsFlask
Integrating CoinPayments With Flask


### Code Snippets

> Auth hepers
```python
from flask_login import login_required, current_user

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
```