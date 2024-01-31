
# The Bachelor TV API

An API to fetch contestant information for each season of the Bachelor. This is still a work in progress.

Core technologies used:
* Python 
* FastAPI
* Postgres
* Docker Compose


## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
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

