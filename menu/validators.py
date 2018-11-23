def is_valid_order(model, ordering, custom_fields=None):
    new_ordering = ordering[1:] if ordering.startswith('-') else ordering

    is_valid_custom_field = new_ordering in custom_fields if custom_fields else False

    return hasattr(model, new_ordering) or is_valid_custom_field
