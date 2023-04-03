from typing import Any
from pydantic.utils import GetterDict

PROXY_FIELDS = ["toppings"]


class ProxyHackGetter(GetterDict):
    """
    Pydantic doesn't play well with SQLAlchemy Proxies (as far as I can tell).
    This getter intercepts proxies and forces them to fetch their values.

    It might be worth looking for a more idomatic way to achieve the same results.
    Add keys you want to intercept to "PROXY_FIELDS" above.
    """

    def get(self, key: str, default: Any) -> Any:
        if key in PROXY_FIELDS:
            fetched_values = [t for t in getattr(self._obj, key, None)]
            return fetched_values
        else:
            return getattr(self._obj, key, default)
