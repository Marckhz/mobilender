from rest_framework.views import exception_handler



#cool example on how to use custom
def error_handler(status_code):
    status_code = str(status_code)
    errors = {
                '404':{
                    "message": "Instance not found.",  
                    "error": "HTTP_404_NOT_FOUND",  
                },
                '400':{
                    'message':'Please check payload data - Object may not exists',
                    'error':'HTTP_400_BAD_REQUEST',
                },
                '500':{
                    'message':'Server Error',
                    'error':'HTTP_500_INTERNAL_SERVER_ERRROR'
                },
            }
    msg = errors.get(status_code)
    return msg

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data = error_handler(response.status_code)
    return response