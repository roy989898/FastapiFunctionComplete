# Missing part

~~templete~~  
auth  
mulit router file  
~~i18n in templete~~ 
csrf  
validation i18n  
logging  
email

# Finish Part

### templete

```python
from global_var import templates


@app.get("/")
async def root(request: Request):
    result = {}
    result.update({"request": request})
    return templates.TemplateResponse("index.html", result)
```


### i18n in templete

```html
{{ 'Hello'  |tran('tc') }}
```