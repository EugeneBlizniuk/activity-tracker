"""Service to handle all operations with categories"""
from typing import List, NamedTuple, Dict

import db


class Category(NamedTuple):
    """Category structure"""
    name: str
    is_base_activity: bool
    aliases: List[str]


class CategoryService:
    def __init__(self):
        self._categories = self._load_categories()

    def _load_categories(self) -> List[Category]:
        """Load all existing categories"""
        categories = db.get_all(
            "category", "name is_base_activity aliases".split()
        )
        categories = self._fill_aliases(categories)
        return categories

    def _fill_aliases(self, categories: List[Dict]) -> List[Category]:
        """Fill up every category with its aliases"""
        filled_up_categories = []
        for index, category in enumerate(categories):
            aliases = category["aliases"].split(",")
            aliases = list(filter(None, map(str.strip, aliases)))
            aliases.append(category["name"])
            filled_up_categories.append(Category(
                name=category["name"],
                is_base_activity=category["is_base_activity"],
                aliases=aliases
            ))
        return filled_up_categories

    def get_all_categories(self) -> List[Category]:
        """Return a dictionary of categories"""
        return self._categories

    def get_category(self, name: str) -> Category:
        """Return a category by a category name"""
        found = None
        other_category = None
        for category in self._categories:
            if category.name == "other":
                other_category = category
            for alias in category.aliases:
                if name in alias:
                    found = category
        if not found:
            found = other_category
        return found
