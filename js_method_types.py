import re

def detect_js_method_type(js_method_code):
    js_method_code = js_method_code.strip()

    if re.match(r"^static\s+get\s+", js_method_code) or re.match(r"^get\s+", js_method_code):
        return "getter"
    elif re.match(r"^static\s+set\s+", js_method_code) or re.match(r"^set\s+", js_method_code):
        return "setter"
    elif re.match(r"^static\s+", js_method_code):
        return "static"
    else:
        return "normal"

example_methods = [
    "get info() { return this.name; }",
    "set info(value) { this.name = value; }",
    "static createAdult(name) { return new Person(name, 18); }",
    "sayHello() { console.log('Hello'); }"
]

for method in example_methods:
    print(method, "->", detect_js_method_type(method))
