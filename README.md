# neoalpaca-ebook-bot

@neoalpaca_bot EN TWITTER

MÁQUINA COMUNICADORA PARA LA ALPACA DORADA. ESCUCHA LAS PALABRAS DE LA TODOPODEROSA ALPACA DORADA EN @neoalpaca_bot EN TWITTER.

Si quieres usar esto para hacer tu propio bot simplemente no lo hagas, usa [esto](https://github.com/mispy/twitter_ebooks) que está mucho mejor hecho que esta mierda de aquí. Hacemos noise, no programación.

## Tutorial para usar esto si insistes

Instala Python. Luego tweepy: `pip install tweepy`

Haz una cuenta de desarrollador de Twitter, crea una app etc y pilla las claves para autenticarse. (puedes buscar en Google todo esto, es fácil).
Las claves las tienes que poner en las siguientes variables de entorno:
`API_KEY` `API_KEY_SECRET` `ACCESS_TOKEN` `ACCESS_TOKEN_SECRET`

`>>> os.environ['API_KEY'] = 'clave aqui'`

Si no, puedes ponerlas en `config.py`. Y en `main.py` cambiar `USE_ENV_VARIABLES` a `False`

Después para poner el @ de la cuenta fuente lo pones en `SOURCE_ACCOUNT_ID` que por defecto pone Neoalpaca.
