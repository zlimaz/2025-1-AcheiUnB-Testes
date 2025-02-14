from django.db import migrations


def create_categories(apps, schema_editor):
    Category = apps.get_model("users", "Category")
    categories = [
        "Celular",
        "Fone de ouvido",
        "Carregador",
        "Notebook",
        "Case Notebook",
        "Case Fone",
        "Tablet",
        "Mouse",
        "Smartwatch",
        "Suporte Notebook",
        "Carregador Portátil",
        "Casaco",
        "Blusa",
        "Camiseta",
        "Brinco",
        "Anel",
        "Óculos",
        "Relógio",
        "Piercing",
        "Boné",
        "Chapéu",
        "Mochila",
        "Carteira",
        "Touca",
        "Chinelo",
        "Colar",
        "Pulseira",
        "Pingente",
        "Presilha de Cabelo",
        "Batom",
        "Gloss",
        "Sombra",
        "Base",
        "Lápis de olho",
        "Blush",
        "Livro",
        "Apostila",
        "Caderno",
        "Lápis",
        "Borracha",
        "Caneta",
        "Lapizeira",
        "Anotações",
        "Grampeador",
        "Estojo",
        "Calculadora",
        "Calculadora Científica",
        "Planner",
        "Stylus",
        "Guarda-chuva",
        "Garrafa de Água",
        "Carteira de Identidade",
        "Carteira de Motorista",
        "Passe Estudantil",
        "Passe de Ônibus",
        "Cartão SUS",
        "Chaves",
        "Nessesair",
        "Outra",
    ]

    # Organize categorias em ordem alfabética, mantendo "Outra" ou "Outro" no final
    categories = sorted(categories)
    categories.remove("Outra")  # Remove "Outra" para adicionar no final
    categories.append("Outra")  # Adiciona "Outra" no final

    for idx, category in enumerate(categories, start=1):
        category_id = "00" if category.lower() in ["outra"] else f"{idx:02d}"
        Category.objects.get_or_create(
            name=category, category_id=category_id
        )  # A ID é '00' para 'Outra'


def create_locations(apps, schema_editor):
    Location = apps.get_model("users", "Location")
    locations = [
        "UAC",
        "Bebedouros - UAC",
        "Biblioteca - UAC",
        "Mesas de Estudos - UAC",
        "Mesas de Dama - UAC",
        "Mesas O Belisco - UAC",
        "Mesanino - UAC",
        "Anfiteatro - UAC",
        "Banheiros - UAC",
        "Estacionamento - UAC",
        "Jardim - UAC",
        "I1 - UAC",
        "I2 - UAC",
        "I3 - UAC",
        "I4 - UAC",
        "I5 - UAC",
        "I6 - UAC",
        "I7 - UAC",
        "I8 - UAC",
        "I9 - UAC",
        "I10 - UAC",
        "S1 - UAC",
        "S2 - UAC",
        "S3 - UAC",
        "S4 - UAC",
        "S5 - UAC",
        "S6 - UAC",
        "S7 - UAC",
        "S8 - UAC",
        "S9 - UAC",
        "S10 - UAC",
        "UED",
        "Bebedouros - UED",
        "Mesa de estudos - UED",
        "Mesanino - UED",
        "Mocap - UED",
        "Banheiros - UED",
        "Mesas Redondas - UED",
        "Sala de Professor - UED",
        "Estacionamento - UED",
        "Laboratórios - UED",
        "LDTEA",
        "Banheiros - LDTEA",
        "Estacionamento - LDTEA",
        "Laboratórios - LDTEA",
        "RU",
        "Banheiros - RU",
        "Mesas - RU",
        "Restaurante - RU",
        "Caixa - RU",
        "Box - RU",
        "Jardim - RU",
        "Diretório Acadêmico - DA",
        "Quadra Poliesportiva",
        "Monumento lado ru",
        "Guarita Estacionamento Sul",
        "Guarita Estacionamento Norte",
        "Outro",
    ]

    # Organize locais em ordem alfabética, mantendo "Outro" no final
    locations = sorted(locations)
    locations.remove("Outro")  # Remove "Outro" para adicionar no final
    locations.append("Outro")  # Adiciona "Outro" no final

    for idx, location in enumerate(locations, start=1):
        location_id = "00" if location.lower() in ["outro"] else f"{idx:02d}"
        Location.objects.get_or_create(
            name=location, location_id=location_id
        )  # A ID é '00' para 'Outro'


def create_colors(apps, schema_editor):
    Color = apps.get_model("users", "Color")
    colors = [
        "Amarelo",
        "Laranja",
        "Verde",
        "Vermelho",
        "Azul",
        "Rosa",
        "Preto",
        "Branco",
        "Marrom",
        "Bege",
        "Cinza",
        "Prata",
        "Dourado",
        "Bronze",
        "Estampado",
        "Outra",
    ]

    # Organize cores em ordem alfabética, mantendo "Outra" no final
    colors = sorted(colors)
    colors.remove("Outra")  # Remove "Outra" para adicionar no final
    colors.append("Outra")  # Adiciona "Outra" no final

    for idx, color in enumerate(colors, start=1):
        color_id = "00" if color.lower() in ["outra"] else f"{idx:02d}"
        Color.objects.get_or_create(name=color, color_id=color_id)  # A ID é '00' para 'Outra'


def create_brands(apps, schema_editor):
    Brand = apps.get_model("users", "Brand")
    brands = [
        "Dell",
        "Asus",
        "Vaio",
        "Sony",
        "Samsung",
        "LG",
        "Lenovo",
        "Apple",
        "Acer",
        "Xiaomi",
        "Huawei",
        "Motorola",
        "JBL",
        "HP",
        "Toshiba",
        "Razer",
        "Kingston",
        "SanDisk",
        "Nokia",
        "Tapaware",
        "Stanley",
        "Bic",
        "Adidas",
        "Nike",
        "New Balance",
        "Puma",
        "Oaklay",
        "Vans",
        "Hay-Ban",
        "Havaianas",
        "Levi's",
        "RRDD",
        "UnB",
        "FGA",
        "FCTE",
        "Avon",
        "O Boticário",
        "Dior",
        "Outra",
    ]

    # Organize marcas em ordem alfabética, mantendo "Outra" no final
    brands = sorted(brands)
    brands.remove("Outra")  # Remove "Outra" para adicionar no final
    brands.append("Outra")  # Adiciona "Outra" no final

    for idx, brand in enumerate(brands, start=1):
        brand_id = "00" if brand.lower() in ["outra"] else f"{idx:02d}"
        Brand.objects.get_or_create(name=brand, brand_id=brand_id)  # A ID é '00' para 'Outra'


class Migration(migrations.Migration):
    dependencies = [
        (
            "users",
            "0010_item_matches_alter_item_status",
        ),  # Substitua pelo nome da última migration
    ]

    operations = [
        migrations.RunPython(create_categories),
        migrations.RunPython(create_locations),
        migrations.RunPython(create_colors),
        migrations.RunPython(create_brands),
    ]
