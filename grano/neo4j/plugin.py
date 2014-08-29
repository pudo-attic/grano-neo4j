from grano.core import app
from grano.interface import Startup, RelationChangeProcessor
from grano.interface import EntityChangeProcessor, ProjectChangeProcessor
from grano.interface import SchemaChangeProcessor
from grano.model import Project, Entity, Relation, Schema

from grano.neo4j.engine import connect


class Plugin(Startup, EntityChangeProcessor, ProjectChangeProcessor,
             RelationChangeProcessor, SchemaChangeProcessor):

    def configure(self, manager):
        connect()
        #app.register_blueprint(interface.blueprint)

    def entity_changed(self, entity_id, operation):
        if operation == 'delete':
            #entities.delete(entity_id)
            pass
        else:
            #entity = Entity.by_id(entity_id)
            #entities.save(entity.to_dict())
            pass

    def relation_changed(self, relation_id, operation):
        if operation == 'delete':
            #relations.delete(relation_id)
            pass
        else:
            #relation = Relation.by_id(relation_id)
            #relations.save(relation.to_dict())
            pass

    def project_changed(self, project_slug, operation):
        if operation == 'delete':
            #projects.delete(project_slug)
            pass
        else:
            #project = Project.by_slug(project_slug)
            #projects.save(project.to_dict())
            pass

    def schema_changed(self, project_slug, schema_name, operation):
        if operation == 'delete':
            #schemata.delete(project_slug, schema_name)
            pass
        else:
            #project = Project.by_slug(project_slug)
            #schema = Schema.by_name(project, schema_name)
            #schemata.save(project_slug, schema.to_dict())
            pass
