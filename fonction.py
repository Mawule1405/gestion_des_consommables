from PIL import Image

def image_negative(image_path):
    # Charger l'image à partir du chemin spécifié
    image = Image.open(image_path)

    # Obtenir les dimensions de l'image
    largeur, hauteur = image.size

    # Créer une nouvelle image pour stocker l'image négative
    image_negative = Image.new('RGB', (largeur, hauteur))

    # Parcourir chaque pixel de l'image d'origine
    for x in range(largeur):
        for y in range(hauteur):
            # Obtenir la couleur du pixel
            couleur = image.getpixel((x, y))

            # Inverser les valeurs RVB
            nouvelle_couleur = tuple(255 - valeur for valeur in couleur)

            # Mettre à jour la couleur du pixel dans l'image négative
            image_negative.putpixel((x, y), nouvelle_couleur)

    # Renvoyer l'image négative
    return image_negative