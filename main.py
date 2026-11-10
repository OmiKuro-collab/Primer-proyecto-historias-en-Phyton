import random 
nombre=input("dime un nombre: ")
adjetivo=input("dime un adjetivo: ")
nombre2=input("dime otro nombre: ")
historia_1=f"Una linda tarde por el parque,{nombre} caminaba hasta que se encontró con el amor de su vida que se llamaba {nombre2}, era tan {adjetivo} que a la mañana siguiente se casaron y vivieron felices para siempre...hasta que {nombre2} termino en coma porque su celular exploto, todo termino bien pero tuvieron que pagar 332433333 pesos mexicanos por la estadia en el hospital. "
historia_2=f"Cuando despertó, {nombre} estaba en un cuarto oscuro y frío, el momento fue tan extraño y {adjetivo} que {nombre} comenzó a gritar, hasta que se prendieron las luces y vio a {nombre2} con un ramo de flores, {nombre2} que conocia desde los 10 años habia desarrollado fuertes sentimientos románticos hacia {nombre} por lo que penso que seria bueno mostrar sus sentimientos en una ¿cita sorpresa?."
historia_3=f"{nombre},tenia problemas con su tarea así que decidió salir a tomar algo de aire por su balcón, hasta que vio un ovni abduciendo a {nombre2}, de inmediatamente saco la bazuka qué tenia su abuela y disparo, fue un éxito, el ovni exploto y salvo a {nombre2}, que desde ese dia comenzó a ver de una forma distinta a {nombre}."
caja_de_historias=[historia_1, historia_2, historia_3]
historia_elegida=random.choice(caja_de_historias)
print("\n--- TU HISTORIA ALEATORIA ---")
print(historia_elegida)
