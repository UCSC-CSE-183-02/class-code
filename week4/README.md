## Project ideas

- room booking application
- cooking recipes
- surevy application
- organize stuff
- invetory
- accounting app
- voting digital content
- voting app
- draw on screen and save drawing
- project proposal management app
  
## Project Proposals:
https://forms.gle/wCFv4EFGLYGyGZVj7

## Free Templates
https://html5up.net/

## Example of a py4web form without database

```
@action("myform", method=["GET", "POST"])
@action.uses("generic.html", auth)
def myform():
    form = Form([
        Field('name'),
        Field('description', 'text'),
    ])
    if form.accepted:
        print(form.vars)
        redirect(URL("index"))
    elif form.errors:
        print(form.errors)
    else:
        print("i made a new form")
    return locals()
```    


