from sqlalchemy.orm import Session
from .database import models
from . import schemas
import logging
log = logging.getLogger(__name__)

# most recent messasge
def get_message(db: Session):
    return db.query(models.Message).order_by(models.Message.id.desc()).first()


def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(message=message.message)
    db.add(db_message)
    try:
        db.commit()
        db.refresh(db_message)
    except Exception as e:
        db.rollback()
        log.error(f'Error creating message: {e}')
        return 'Error'
    return 'Success'