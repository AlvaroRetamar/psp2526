#%%
def procesar_archivos(*rutas, **acciones) -> list[dict]:
    resultados = []
    for ruta in rutas:
        ruta_dict = {}
        if acciones.get('normalizar', False):
            ruta_dict['ruta'] = ruta.lower().replace(' ', '_')
        else:
            ruta_dict['ruta'] = ruta
        if ruta.split('.')[-1] in acciones.get('permitidas', []):
            ruta_dict['ok'] = True
        else:
            ruta_dict['ok'] = False
        

# %%

# %%
