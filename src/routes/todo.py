from flask import Blueprint

todo = Blueprint('todo', __name__)

@todo.route('/', methods=['GET'])
def get_todos():
    return 'Get all todos'

@todo.route('/<int:id>', methods=['GET'])
def get_todo(id):
    return 'get todo by ID'

@todo.route('/', methods=['POST'])
def create_todo():
    return 'create_todo'

@todo.route('/<int:id>', methods=['PUT'])
def update_todo(id):
    return 'update_todo'

@todo.route('/<int:id>', methods=['DELETE'])
def delete_todo(id):
    return 'delete_todo'

