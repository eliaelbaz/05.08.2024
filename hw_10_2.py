# hw_10_2
def perform_action(action):
    actions = {
        'add': 'Adding item',
        'delete': 'Deleting item',
        'update': 'Updating item'
    };
    return actions.get(action, 'Unknown action');

result = perform_action('add');
print(result);
