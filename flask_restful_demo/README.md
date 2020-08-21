# Flask Restful API

参考链接：
- [Python中Flask-RESTful编写API接口](https://blog.csdn.net/chenmozhe22/article/details/82347813) 
- [Flask中endpoint的理解](https://www.cnblogs.com/eric-nirnava/p/endpoint.html)
- [flask文档](http://docs.jinkan.org/docs/flask/)
- [开放API规范3.0](https://github.com/fishead/OpenAPI-Specification/blob/master/versions/3.0.0.zhCN.md#oasDocument)

详细步骤

```python

```


## flask swagger 

Operation Object ： 描述对路径的某个操作
1. `tags` : **string**, 用于控制API文档的标签列表，标签可以用于在逻辑上分组对资源的操作或作为其它用途的先决条件。
2. `summary`: **string**, 对此操作行为的简短描述。
3. `description`: **string**, 对此操作行为的简短描述。
4. `parameters`: **parameter对象**
    - `name`: String 类型，必填，参数名，大小写敏感
    - `in`: String 类型，必填，可能的值有：query、header、path、formData和body。
        - `path`:  和路径模板一起使用，也就是说参数本身是路径的一部分。相对路径。例如：/items/{itemId}中，itemId为参数。
        - `query`: 添加在URL上的查询参数。例如：/items?id=###中，查询参数为id。
        - `header`:  自定义的请求头参数
        - `body`: 附加到HTTP请求的payload。因为一个请求只能有一个payload，所以也只能有一个Body参数。body参数的名称本身并没有什么影响。考虑到Form本身也是一种Body，所以对于同一个操作，Form和Body不能共存。
             - 如果 in 的值为`body`, `schema`	Schema对象必填。Schema对象定义了body参数的类型。
        - `form`: 当请求的contentType为application/x-www-form-urlencoded或者application/form-data或者两者都有时（consumes所描述的媒体类型），用于描述附加在HTTP请求上的payload。这是唯一的一种可以用来上传文件的参数类型。
    - `description`: String 类型，
    - `required` : boolean 类型，参数是否必填。如果说in的值为path，那么required值必须为true。
    - ```python
        parameters: 
            name: id
            in: query
            description: ID of the object to fetch
            required: false
            schema:
              type: array
              items:
                type: string
            style: form
            explode: true
      ```
      
5. `responses` : **responses 对象**
    ```python
        responses:
           '200':
             description: 成功调用
             content:
               application/json:
                 schema:
                   $ref: '#/components/schemas/Pet'
           default:
             description: Unexpected error
             content:
               application/json:
                 schema:
                   $ref: '#/components/schemas/ErrorModel'
   ```  
