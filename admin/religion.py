from sqladmin import ModelView

from kingdom.models.religion import God, Domain


class DomainAdmin(ModelView, model=Domain):
    column_list = [Domain.id, Domain.name]
    form_columns = [Domain.name]


class GodAdmin(ModelView, model=God):
    column_list = [God.id, God.name]
    form_excluded_columns = [God.characters, God.domain_details]
