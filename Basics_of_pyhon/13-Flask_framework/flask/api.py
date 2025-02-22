### put nad delete -HTTP verbs
## working with api's --json


from flask import Flask,jsonify,request

app=Falsk(__name__)
##internal Data in my to do list

items=[
    {'id':1,"name":"Item 1","description":"This is item 1"},
    {'id':2,"name":"item 2","description":"This is item 2"}
]

@app.route('/')
def home():
    return "Welcome to the sample to list"

## Get:retrieve all the items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for items in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

## post 
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id":items[-1]["id"]+1 if item else 1,
        "name":request.json['name'],
        "description":request.json["description"]
    }  
    items.append(new_item)
    return jsonify(new_item)

#Put:Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for items in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})

        
if __name__=='__main__':
    app.run(debug=True)
