from datetime import datetime

from sqlalchemy import Column, BigInteger, ForeignKey, DateTime

from src.schemas.application import ApplicationRead
from settings.database.database_connection import Base


class Application(Base):
    __tablename__ = "Application"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("User.id"), nullable=False)
    insurance_sum = Column(BigInteger)
    total_insurance_premium = Column(BigInteger)
    main_coverage_premium = Column(BigInteger)
    ns_premium = Column(BigInteger)
    disability_premium = Column(BigInteger)
    tt_premium = Column(BigInteger)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_read_model(self) -> ApplicationRead:
        return ApplicationRead(
            id=self.id,
            user_id=self.user_id,
            insurance_sum=self.insurance_sum,
            total_insurance_premium=self.total_insurance_premium,
            main_coverage_premium=self.main_coverage_premium,
            ns_premium=self.ns_premium,
            disability_premium=self.disability_premium,
            tt_premium=self.tt_premium,
            created_at=self.created_at,
        )
