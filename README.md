
# The Bachelor TV API

An API to fetch contestant information for each season of the Bachelor. This is still a work in progress.

Core technologies used:
* Python 
* FastAPI
* Postgres
* Docker Compose

## Development Information
Atlassian Jira Kanban Board

- [Jira](https://softwaredesigns.atlassian.net)
 
In Cloud
Atlassian Confluence Page

- [Confluence](https://softwaredesigns.atlassian.net)
## Usage/Examples

```python
# Sample data for contestants
contestants_data = [
    {"id": 1, "first_name": "Hannah","last_name": "Brown", "age": 24, "occupation": Occupation.interior_designer},
    {"id": 2, "first_name": "Jed","last_name": "Wyatt", "age": 25, "occupation": Occupation.singer},
    {"id": 3, "first_name": "Tyler","last_name": "Cameron", "age": 26, "occupation": Occupation.general_contractor},
]

Run Live server:
uvicorn main:app --reload
Access endpoints at http://127.0.0.1:8000

Example to get all contestants:
http://127.0.0.1:8000/api/v1/contestants

Example to get Hanna Brown information:
http://127.0.0.1:8000/api/v1/contestants/1

```


## API Reference

#### Get all contestants

```http
  GET /api/v1/contestants
```

#### Get a specific contestant based on id

```http
  GET /api/contestants/${contestant_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `contestant_id`      | `int` | **Required**. Id of contestant to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.


## Authors

- [@dchhouen](https://github.com/dchhouen)


## License


This project is licensed under the terms of the MIT license.

Copyright (c) [2024] 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)

