# <center> VACCINATION API</center>

A basic API to train API creation with Flask.

### URL: ` https://api-vaccination.herokuapp.com/`

---

### **VACCINATIONS**

## <center>`POST /vaccinations - 201` </center>

Corpo da requisição:

```json
{
  "cpf": "01234567891",
  "name": "Chrystian",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}
```

Corpo da resposta:

```json
{
  "cpf": "01234567891",
  "first_shot_date": "Tue, 26 Apr 2022 22:33:28 GMT",
  "health_unit_name": "santa rita",
  "name": "chrystian",
  "second_shot_date": "Mon, 25 Jul 2022 22:33:28 GMT",
  "vaccine_name": "pfizer"
}
```

## <center>`GET /vaccinations - 200` </center>

Corpo da resposta:

```json
{
  "data": [
    {
      "cpf": "01234567891",
      "first_shot_date": "Tue, 26 Apr 2022 22:33:28 GMT",
      "health_unit_name": "santa rita",
      "name": "chrystian",
      "second_shot_date": "Mon, 25 Jul 2022 22:33:28 GMT",
      "vaccine_name": "pfizer"
    },
    {
      "cpf": "19876543210",
      "first_shot_date": "Tue, 26 Apr 2022 22:34:03 GMT",
      "health_unit_name": "santa rita",
      "name": "odranoel",
      "second_shot_date": "Mon, 25 Jul 2022 22:34:03 GMT",
      "vaccine_name": "pfizer"
    }
  ]
}
```
