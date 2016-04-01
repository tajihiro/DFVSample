from sqlalchemy import Column, Integer, String
from database import Base

class UserAgent(Base):
    def __init__(self, agent_cd, agent_name, category, name, version, os_name, vendor, os_version):
        self.agent_cd = agent_cd
        self.agent_name = agent_name
        self.category = category
        self.name = name
        self.version = version
        self.os_name = os_name
        self.vendor = vendor
        self.os_version = os_version

    def __repr__(self):
        return '<UserAgents %r>' % self.agent_cd + self.agent_name

    __tablename__ = 'user_agents'
    id = Column(Integer, primary_key=True)
    agent_cd = Column(String(40), unique=True)
    agent_name = Column(String(40), unique=False)
    category = Column(String(40), unique=False)
    name = Column(String(40), unique=False)
    version = Column(String(40), unique=False)
    os_name = Column(String(40), unique=False)
    vendor = Column(String(40), unique=False)
    os_version = Column(String(40), unique=False)