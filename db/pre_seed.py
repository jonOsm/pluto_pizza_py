from api.crud.product_customizations_crud import read_all_secondary_customization
from db.models import (
    CheeseAmtModel,
    CheeseTypeModel,
    CrustThicknessModel,
    CrustTypeModel,
    SauceAmtModel,
    SauceTypeModel,
    ToppingModel,
)
from db.setup import get_db

session = next(get_db())
# We're passing a session in for toppings b/c
# factory and ToppingModel must use same session
# for orm to work properly -
# TODO: improve efficiency since this read runs for every product cutomization

toppings = lambda session: read_all_secondary_customization(session, ToppingModel)
crust_types = read_all_secondary_customization(session, CrustTypeModel)
crust_thicknesses = read_all_secondary_customization(session, CrustThicknessModel)
cheese_types = read_all_secondary_customization(session, CheeseTypeModel)
cheese_amts = read_all_secondary_customization(session, CheeseAmtModel)
sauce_types = read_all_secondary_customization(session, SauceTypeModel)
sauce_amts = read_all_secondary_customization(session, SauceAmtModel)
session.close()
