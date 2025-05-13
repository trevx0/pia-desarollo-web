#!/usr/bin/env python
#!/usr/bin/env python
# Reemplaza el contenido de manage.py con esto:
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mi_proyecto.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("¿Está instalado Django? ¿Activaste el entorno virtual?") from exc
    execute_from_command_line(sys.argv)