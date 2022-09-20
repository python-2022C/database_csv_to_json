# CSV to Json

## Exmaple

```
ID,model,company,price
1,Galaxy S21 Ultra 5G,Samsung,500
```

```Python
{
    "Mobile": {
        "1": {
            "model": "Galsaxy s21",
            "company": "Samsung",
            "price": 500
        }
    }
}