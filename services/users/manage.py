from flask.cli import FlaskGroup
from project import app, db

cli = FlaskGroup(app)

@cli.command("recreate_db")
def recreate_db():
    try:
        print("re-creating the database...")
        db.drop_all()
        db.create_all()
        db.session.commit()
    except Exception as exe:
        print("exception occured while running the command")
        print(exe)
if __name__ == "__main__":
    cli()