from jinja2 import Environment, FileSystemLoader


def init_theme(info: {str, str, str}, link: {str, str},
               reply: {str, str}, quote_color: str):
    theme = {}
    theme["name"] = info["name"]
    theme["file_name"] = info["file_name"]
    theme["description"] = info["description"]
    theme["link_background"] = link["background"]
    theme["link_color"] = link["color"]
    theme["reply_background"] = reply["background"]
    theme["reply_border_color"] = reply["border_color"]
    theme["quote_color"] = quote_color
    return theme


themes = [
    init_theme(info={"name": "black", "file_name": "black",
                     "description": "Black theme for 4chan"},
               link={"color": "white", "background": "black"},
               reply={"background": "gray", "border_color": "white"},
               quote_color="#789922"),
    init_theme(info={"name": "white", "file_name": "white",
                     "description": "White theme for 4chan"},
               link={"color": "black", "background": "white"},
               reply={"background": "beige", "border_color": "black"},
               quote_color="#789922")
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader, keep_trailing_newline=True)

template = env.get_template('4chan.j2')

for theme in themes:
    output = template.render(theme=theme)
    with open("./themes/{}.user.css".format(theme["file_name"]), "w") as result_file:
        result_file.write(output)
    print(output)
