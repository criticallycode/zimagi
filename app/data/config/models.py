from django.db import models as django

from settings import Roles
from systems.models import fields, environment, group


class ConfigFacade(
    group.GroupModelFacadeMixin,
    environment.EnvironmentModelFacadeMixin,
):
    pass


class Config(
    group.GroupMixin,
    environment.EnvironmentModel
):
    value = fields.EncryptedDataField(null=True)
    
    class Meta(environment.EnvironmentModel.Meta):
        facade_class = ConfigFacade

    def allowed_groups(self):
        return [ Roles.admin ]
