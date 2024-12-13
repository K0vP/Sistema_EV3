import requests as req
from servicios.servicio_url import UrlCompleta

def CrearPostApi(post):
    url = UrlCompleta("1")
    headers = {'Content-Type': 'application/json'}
    data = {'userId': post.user_id, 'title': post.title, 'body': post.body}
    try:
        respuesta = req.post(url, headers=headers, json=data)
        if respuesta.status_code == 201:
            print('Post creado con éxito!')
        else:
            print('Error al crear el post:', respuesta.text)
    except:
        print(f"Error al crear el post, detalles:", respuesta.text)

def CrearCommentApi(comment):
    url = UrlCompleta("2")
    headers = {'Content-Type': 'application/json'}
    data = {'postId': comment.post_id, 'name': comment.name, 'email': comment.email, 'body': comment.body}
    try:
        respuesta = req.post(url, headers=headers, json=data)
        if respuesta.status_code == 201:
            print('Comentario creado con éxito!')
        else:
            print('Error al crear el comentario:', respuesta.text)
    except:
        print(f"Error al crear el comentario, detalles:", respuesta.text)

