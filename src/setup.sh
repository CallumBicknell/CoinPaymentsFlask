echo "[!] Run the following commands in the next shell"
echo "================================================"
echo "from app.extensions import db"
echo "from app.models.user import User"
echo "[OPTIONAL] db.drop_all()"
echo "db.create_all()"

flask shell
