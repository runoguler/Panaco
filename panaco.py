from app import app, db
from app.models import Medicine

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Medicine': Medicine}

if __name__ == '__main__':
    app.run()
