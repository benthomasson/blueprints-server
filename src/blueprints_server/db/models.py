from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Entity(Base):
    __tablename__ = "entity"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime, server_default=func.now())


class EntityRelationship(Base):
    __tablename__ = "entity_relationship"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime, server_default=func.now())

    relationship_type = Column(String, nullable=False)
    entity_a_uuid = Column(
        UUID(as_uuid=True), ForeignKey("entity.uuid"), nullable=False
    )
    entity_b_uuid = Column(
        UUID(as_uuid=True), ForeignKey("entity.uuid"), nullable=False
    )


class DeletedEntity(Base):
    __tablename__ = "deleted_entity"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, server_default=func.now())


class DeletedEntityRelationship(Base):
    __tablename__ = "deleted_entity_relationship"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, server_default=func.now())

    relationship_type = Column(String, nullable=False)
    entity_a_uuid = Column(UUID(as_uuid=True), nullable=False)
    entity_b_uuid = Column(UUID(as_uuid=True), nullable=False)


class EntityDefinition(Base):
    __tablename__ = "entity_definition"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime, server_default=func.now())

    entity_uuid = Column(UUID(as_uuid=True), ForeignKey("entity.uuid"), nullable=False)
    entity = relationship("Entity", back_populates="entity_definition")

    entity_type = Column(String, nullable=False)
    entity_name = Column(String, nullable=False)
    entity_description = Column(String, nullable=False)


class DeletedEntityDefinition(Base):
    __tablename__ = "deleted_entity_definition"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime, server_default=func.now())

    entity_uuid = Column(UUID(as_uuid=True), nullable=False)

    entity_type = Column(String, nullable=False)
    entity_name = Column(String, nullable=False)
    entity_description = Column(String, nullable=False)
