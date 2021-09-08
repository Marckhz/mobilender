def client_vendor_dict():
    return {
        "client":{
            "name":"John Doe",
            "code":"random123",
            "photo":"http://dummyimage.com/247x100.png/5fa2dd/ffffff",
            "kind":"C",
        },
        "vendor":{
            "name":"John Doe",
            "code":"random123",
            "photo":"http://dummyimage.com/247x100.png/5fa2dd/ffffff",
            "kind":"V",
        },
        "ranks":[
            {"ranks":"P"}
        ],
        "address":[{
            "city":"city-of-dreams",
            "state":"miami baby",
            "zipcode":"1234",
            "street":"broken dreams"
        }]
    }

def get_client_data_normal():
    return {
        "name":"John Doe",
        "code":"random1234",
        "photo":"http://dummyimage.com/247x100.png/5fa2dd/ffffff",
        "kind":"V",
        "ranks":[
            {"ranks":"P"}
        ],
        "address":[{
            "city":"city-of-dreams",
            "state":"miami baby",
            "zipcode":"1234",
            "street":"broken dreams"
        }]
    }


def get_person_as_client():
    return {
        "name":"John Doe",
        "code":"random1234",
        "photo":"http://dummyimage.com/247x100.png/5fa2dd/ffffff",
        "kind":"C",
        "ranks":[
            {"ranks":"P"}
        ],
        "address":[{
            "city":"city-of-dreams",
            "state":"miami baby",
            "zipcode":"1234",
            "street":"broken dreams"
        }]
    }

def get_person_as_vendor():
    return {
        "name":"John Doe",
        "code":"random1234",
        "photo":"http://dummyimage.com/247x100.png/5fa2dd/ffffff",
        "kind":"V",
        "ranks":[
            {"ranks":"P"}
        ],
        "address":[{
            "city":"city-of-dreams",
            "state":"miami baby",
            "zipcode":"1234",
            "street":"broken dreams"
        }]
    }


def get_article():
    return {
        "code":"random123",
        "description":"cool-description",
        "price":"1234.00",
        "vendor_id":["1"]
}

def get_site():
    return {
        "kind": "DS",
        "name": "Quimba",
        "reference": "#6b84e4",
        "code": "251.213.230.50",
}

def get_order():
    return {
        "on_request_date": "2021-09-07",
        "on_delivery_date": "2021-06-08",
        "urgent": False,
        "quantity": 50,
        "delivery_to": "DS",
        "person_id":1,
        "site_id":["1"],
        "article_id":"1"
    }