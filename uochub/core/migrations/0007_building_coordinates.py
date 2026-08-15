from django.db import migrations

# Geocoded via OpenStreetMap Nominatim. Kingsway and Wheeler are street-level
# approximations; adjust in the admin if needed.
COORDINATES = {
    "Exton Park": (53.2002643, -2.8993189),
    "Creative Campus, Kingsway": (53.2060104, -2.8743365),
    "Queen's Park": (53.1862498, -2.8847593),
    "Wheeler": (53.1847638, -2.8919826),
    "Bache Hall": (53.2067361, -2.8964745),
    "Gateway House": (53.1927383, -2.8924702),
    "The Hammond": (53.2163648, -2.8553033),
}


def set_coordinates(apps, schema_editor):
    Building = apps.get_model("core", "Building")
    for name, (lat, lng) in COORDINATES.items():
        Building.objects.filter(name=name).update(latitude=lat, longitude=lng)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_building_latitude_building_longitude"),
    ]

    operations = [
        migrations.RunPython(set_coordinates, migrations.RunPython.noop),
    ]
