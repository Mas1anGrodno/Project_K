
def menu_items(request):
    menu = [{'title': 'Главная', 'url': '/'},
            {'title': 'Проекты', 'url': '/proj', 
             'submenu': [{'title': 'Добавить проект', 'url': '/add_proj'}
    ]},
            {'title': 'Задачи', 'url': '/tasks', 'submenu': [
            {'title': 'Добавить задачу', 'url': '/add_task'},
            {'title': 'Добавить комментарий', 'url': '/add_coment'}
    ]}
]
    return {'menu': menu}
