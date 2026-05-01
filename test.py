import google.genai as gen

gen.configure(api_key="AIzaSyB1FfNR4lQ5gqoOyg7YPS-EpgdU-ebejK8")

for m in gen.list_models():
    print(m.name, m.supported_generation_methods)