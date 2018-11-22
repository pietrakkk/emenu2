def is_valid_order(model, ordering, custom_fields=None):
    new_ordering = ordering[1:] if ordering.startswith('-') else ordering

    return hasattr(model, new_ordering) or new_ordering in custom_fields
