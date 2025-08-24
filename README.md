# Taller-Retos

init: Es el constructor. Se usa para inicializar el atributo name al crear un objeto.

self.name: Guarda el nombre del animal.

Animal: Clase base para todos los animales. Cada uno tiene un nombre y puede mostrar info y comer (eat()).

Subclases específicas:

Dog: traer objetos (fetch(item)).

Cat: dormir (sleep()).

Bird: Puede piar (chirp()).

Parrot (hereda de Bird): Además puede hablar frases personalizadas (talk(phrase)).

Eagle (hereda de Bird): Tiene atributo extra altitude y muestra a qué altura vuela (show_altitude()).

Owner: Representa a una persona que tiene varias mascotas. Puede agregar animales (add_pet) y alimentarlos a todos (feed_animals).

Zoo: Guarda varios animales en una lista y los muestra con show_animals().
