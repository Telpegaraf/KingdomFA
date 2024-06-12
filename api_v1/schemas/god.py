


class GodBase(BaseModel):
    name: Annotated[str, MaxLen(100)]
    alias: Annotated[str, MaxLen(100)]
    edict: Annotated[str, MaxLen(300)]
    anathema: Annotated[str, MaxLen(300)]
    areas_of_interest: Annotated[str, MaxLen(300)]
    temples: Annotated[str, MaxLen(300)]
    worship: Annotated[str, MaxLen(300)]
    sacred_animal: Annotated[str, MaxLen(300)]
    sacred_color: Annotated[str, MaxLen(300)]
    chosen_weapon: Annotated[str, MaxLen(300)]
    taro: Annotated[str, MaxLen(300)]
    alignment: Annotated[str, MaxLen(300)]
    domains: List[DomainBase]


class God(DomainBase):
    model_config = ConfigDict(from_attributes=True)

    id: int