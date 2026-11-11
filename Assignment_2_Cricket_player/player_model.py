from sqlalchemy import Column, Integer, String, CheckConstraint
from config.database import Base

class CricketPlayer(Base):

    __tablename__ = "cricketplayer"

    __table_args__ = (
        CheckConstraint("matches_played >= 0"),
        CheckConstraint("total_runs >= 0"),
        CheckConstraint("wickets_taken >= 0"),
        CheckConstraint("balls_faced >= 0"),
        CheckConstraint("catches >= 0"),
    )

    player_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    player_name = Column(
        String(40),
        nullable=False
    )

    team_name = Column(
        String(100),
        nullable=False
    )

    role = Column(
        String(20),
        nullable=False
    )

    matches_played = Column(
        Integer,
        nullable=False
    )

    total_runs = Column(
        Integer,
        nullable=False
    )

    wickets_taken = Column(
        Integer,
        nullable=False
    )

    balls_faced = Column(
        Integer,
        nullable=False
    )

    catches = Column(
        Integer,
        nullable=False
    )