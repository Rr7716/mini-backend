def to_serializable(obj):
    if isinstance(obj, list):
        return [to_serializable(i) for i in obj]
    if hasattr(obj, "dict"):   # Pydantic
        return obj.dict()
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    if hasattr(obj, "__dict__"):
        return {k: to_serializable(v) for k, v in obj.__dict__.items()}
    return obj
