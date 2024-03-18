import json

from genson import SchemaBuilder


def generate_schema(response):
    """
    Сгенерировать json-схему и вернуть ответ в виде теста для Postman.
    К схеме добавляется поле additionalProperties со значение false –
    оно не допускает в ответе значений, кроме указанных в схеме.
    :param response: ответ метода, из которого генерируется схема
    :return: готовый тест для Postman
    """
    builder = SchemaBuilder()
    builder.add_object(response.json())
    schema = builder.to_schema()
    schema.update({"additionalProperties": False})

    result = f'''
    response = pm.response.json()
    
    const schema = {json.dumps(schema)};
    
    pm.test("Validate schema", () => {{
        pm.response.to.have.jsonSchema(schema);
    }});

    const  Ajv = require('ajv');
    ajv = new Ajv({{logger: console}});

    pm.test('Response matches the schema', function() {{
        pm.expect(ajv.validate(schema, response)).to.be.true;
    }});

    if (ajv.errors) {{
    console.log(ajv.errors);
    }};'''
    print('Подготовлен тест на json-схему:')
    return result
