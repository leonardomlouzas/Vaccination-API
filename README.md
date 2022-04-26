# <center> VACCINATION API</center>

A basic API to train API creation with Flask.

---

### **VACCINATIONS**

## <center>`GET /vaccinations - 200` </center>

Corpo da resposta:

```json
{
  "data": [
    {
      "cpf": "01234567891",
      "name": "Chrystian",
      "first_shot_date": "Fri, 29 Oct 2021 16:30:31 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:30:31 GMT",
      "vaccine_name": "Pfizer",
      "health_unit_name": "Santa Rita"
    },
    {
      "cpf": "19876543210",
      "name": "Cauan",
      "first_shot_date": "Fri, 29 Oct 2021 16:31:30 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:31:30 GMT",
      "vaccine_name": "Coronavac",
      "health_unit_name": "Santa Rita"
    },
    {
      "cpf": "54221194161",
      "name": "Eduardo",
      "first_shot_date": "Fri, 29 Oct 2021 16:35:24 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:35:24 GMT",
      "vaccine_name": "Coronavac",
      "health_unit_name": "Santa Rita"
    }
  ]
}
```

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
  "name": "Chrystian",
  "first_shot_date": "Fri, 29 Oct 2021 16:36:13 GMT",
  "second_shot_date": "Thu, 27 Jan 2022 16:36:13 GMT",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}
```
