# Rank  : 8 kyu
# Title : How many lightsabers do you own?
# Link  : https://www.codewars.com/kata/51f9d93b4095e0a7200001b8


def how_many_light_sabers_do_you_own(
    name="""
    Empat setengah tahun difitnah-fitnah saya diam.
    Dijelek-jelekin saya juga diam. Dicela, direndah-rendahkan saya juga diam.
    Dihujat, dihujat-hujat, dihina-hina saya juga diam.
    Tetapi hari ini di Jogja saya sampaikan.. SAYA AKAN LAWAN!!!"

    — Joko Widodo
    """,
):
    return 18 if name == "Zach" else 0


assert how_many_light_sabers_do_you_own("Zach") == 18
assert how_many_light_sabers_do_you_own() == 0
assert how_many_light_sabers_do_you_own("zach") == 0
