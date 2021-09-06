def get_client_data_platinum():
    return {
        "name":"John Doe",
        "code":"random123",
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

def get_client_data_normal():
    return {
        "name":"John Doe",
        "code":"random1234",
        "photo":"http://dummyimage.com/247x100.png/5fa2dd/ffffff",
        "kind":"V",
        "ranks":[
            {"ranks":"N"}
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
        "price":1234,
        "vendor_id":1
    }

