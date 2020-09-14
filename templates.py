#los nombres de los archivos y eso puede parecer arcaico pero es para poder usarlo con github pages
from jinja2 import Environment, FileSystemLoader

renderizar = ["index.html","posicion.html"] #es demasiado obtenerlas automaticamente, igual van a ser 5 archivos, no se justifica

templateLoader = FileSystemLoader(searchpath="./templates")
templateEnv = Environment(loader=templateLoader)
for template in renderizar:
    outputText = templateEnv.get_template(template).render()  # this is where to put args to the template renderer
    with open(f"templates_renderizadas\\{template}",mode="w",encoding="utf8") as final:
        final.write(outputText)
print("Templates renderizadas")