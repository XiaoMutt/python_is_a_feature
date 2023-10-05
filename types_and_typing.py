# Python has no static typing and the typing system behaves like a hack on the language leading to unexpected behavior

# Typing traps

from typing import TypeVar

T = TypeVar("T")


class JsLikeDict(dict[str, T]):
    def __setattr__(self, key, value):
        self[key] = value

    def __getattribute__(self, item):
        if item in self:
            return self[item]
        else:
            return super().__getattribute__(item)


# the type hint below will inject __orig_class__ attribute to the instance and get into the dict
b = JsLikeDict[JsLikeDict]()
print(b)
