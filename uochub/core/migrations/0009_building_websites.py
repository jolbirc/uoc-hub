from django.db import migrations

WEBSITES = {
    "Exton Park": "https://www.chester.ac.uk/about/our-locations/exton-park-chester/",
    "Creative Campus, Kingsway": "https://www.chester.ac.uk/about/our-locations/creative-campus-kingsway-chester/",
    "Queen's Park": "https://www.chester.ac.uk/about/our-locations/queens-park-chester/",
    "Wheeler": "https://www.chester.ac.uk/about/our-locations/wheeler-chester/",
    "Bache Hall": "https://www.chester.ac.uk/about/our-locations/bache-hall-chester/",
    "Gateway House": "https://www.chester.ac.uk/about/our-locations/gateway-house-chester/",
    "The Hammond": "https://www.chester.ac.uk/about/our-locations/the-hammond/",
}


def set_websites(apps, schema_editor):
    Building = apps.get_model("core", "Building")
    for name, url in WEBSITES.items():
        Building.objects.filter(name=name).update(website=url)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_building_website"),
    ]

    operations = [
        migrations.RunPython(set_websites, migrations.RunPython.noop),
    ]
