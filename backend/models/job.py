from backend.db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, nullable=True)
    job_id = Column(String, index=True)
    status = Column(String)
    error = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    compileted_job = Column(DateTime(timezone=True), nullable=True)
    session_id = Column(String, index=True)
    theme = Column(String)
    