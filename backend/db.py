from sqlalchemy import create_engine
import sqlalchemy.orm as orm

db = create_engine('postgres://zl2683:CS4111@34.73.21.127/proj1part2')
Session = orm.sessionmaker(bind=db)