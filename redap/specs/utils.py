def generate_spec_def(schema_name, config):
    fields = {
        'required': config['required_fields'],
        'properties': {}
    }

    for name, field in config['fields'].items():
        fields['properties'][name] = {
            'type': field['type'],
        }

    return {schema_name: fields}
