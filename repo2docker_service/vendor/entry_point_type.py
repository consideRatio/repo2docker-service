from importlib.metadata import entry_points

from traitlets import Type


# This class is copied without modification from jupyterhub/jupyterhub:
# https://github.com/jupyterhub/jupyterhub/blob/3.0.0/jupyterhub/traitlets.py#L116-L159
#
class EntryPointType(Type):
    """Entry point-extended Type

    classes can be registered via entry points
    in addition to standard 'mypackage.MyClass' strings
    """

    _original_help = ""

    def __init__(self, *args, entry_point_group, **kwargs):
        self.entry_point_group = entry_point_group
        super().__init__(*args, **kwargs)

    @property
    def help(self):
        """Extend help by listing currently installed choices"""
        chunks = [self._original_help]
        chunks.append("Currently installed: ")
        for key, entry_point in self.load_entry_points().items():
            chunks.append(f"  - {key}: {entry_point.module}.{entry_point.attr}")
        return "\n".join(chunks)

    @help.setter
    def help(self, value):
        self._original_help = value

    def load_entry_points(self):
        """Load my entry point group

        Returns a dict whose keys are lowercase entrypoint names
        """
        return {
            entry_point.name.lower(): entry_point
            for entry_point in entry_points(group=self.entry_point_group)
        }

    def validate(self, obj, value):
        if isinstance(value, str):
            # first, look up in entry point registry
            registry = self.load_entry_points()
            key = value.lower()
            if key in registry:
                value = registry[key].load()
        return super().validate(obj, value)
