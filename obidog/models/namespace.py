from dataclasses import dataclass, field
from typing import List, Dict, Union

from obidog.models.base import BaseModel
from obidog.models.classes import ClassModel
from obidog.models.enums import EnumModel
from obidog.models.functions import FunctionModel, FunctionOverloadModel
from obidog.models.globals import GlobalModel
from obidog.models.typedefs import TypedefModel
from obidog.models.flags import ObidogFlagsModel
from obidog.models.urls import URLs


@dataclass
class NamespaceModel(BaseModel):
    name: str = ""
    path: str = ""
    namespace: str = ""
    description: str = ""
    classes: Dict[str, ClassModel] = field(default_factory=lambda: {})
    functions: Dict[str, Union[FunctionModel, FunctionOverloadModel]] = field(
        default_factory=lambda: {}
    )
    enums: Dict[str, EnumModel] = field(default_factory=lambda: {})
    globals: Dict[str, GlobalModel] = field(default_factory=lambda: {})
    namespaces: Dict[str, "NamespaceModel"] = field(default_factory=lambda: {})
    typedefs: Dict[str, TypedefModel] = field(default_factory=lambda: {})
    flags: ObidogFlagsModel = ObidogFlagsModel()
    _type: str = "namespace"
    urls: URLs = field(default_factory=lambda: URLs())
